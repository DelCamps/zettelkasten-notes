"""Check a Morning Brief edition before it is published.
Usage: python3 -I validate_brief.py <brief.json> [--sources DIR] [--log DIR]
  brief.json   the edition document (bare, or wrapped as {"data": {...}})
  --sources    directory of <item id>.json files from extract_source.py (enables the figure check)
  --log        directory of log documents (<doc id>.json) to catch stories already covered on earlier days
Prints ERRORS (must be fixed before publishing) and CHECKS (review each one: fix it, or make sure it is
deliberate, e.g. a figure calculated from numbers in the source). Exit code: 0 clean, 2 checks only, 1 errors.
Standard library only, so it runs under any python3."""
import sys, os, re, json, glob, datetime, unicodedata

args = sys.argv[1:]
if not args or args[0].startswith("-"):
    sys.exit(__doc__)
def opt(name):
    return args[args.index(name) + 1] if name in args else None
raw = json.load(open(args[0]))
doc = raw.get("data", raw) if isinstance(raw.get("data"), dict) else raw
SRC, LOG = opt("--sources"), opt("--log")
errors, checks = [], []
def E(where, msg): errors.append(f"{where}: {msg}")
def C(where, msg): checks.append(f"{where}: {msg}")
def nonempty(v):
    if isinstance(v, str): return bool(v.strip())
    if isinstance(v, list): return bool(v) and all(isinstance(x, str) and x.strip() for x in v)
    return False

# ---------- edition-level fields ----------
date = doc.get("date", "")
if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(date)): E("date", f"not YYYY-MM-DD: {date!r}")
if not isinstance(doc.get("generatedAt"), int): E("generatedAt", "missing or not epoch milliseconds")
if not isinstance(doc.get("reminders", []), list) or not all(isinstance(r, str) for r in doc.get("reminders", [])):
    E("reminders", "must be a list of strings")

cond = doc.get("conditions")
STAT = {"ok", "delays", "disrupted", "unknown"}
if not isinstance(cond, dict): E("conditions", "missing")
else:
    if not re.fullmatch(r"\d{2}:\d{2}", str(cond.get("checkedAt", ""))): E("conditions.checkedAt", "not HH:MM")
    w = cond.get("weather")
    if w is not None:
        for k in ("high", "low", "rain"):
            if not isinstance(w.get(k), (int, float)): E(f"conditions.weather.{k}", "not a number")
        if not nonempty(w.get("summary", "")): E("conditions.weather.summary", "empty")
        if not isinstance(w.get("warning", ""), str): E("conditions.weather.warning", "must be a string ('' if none)")
    for k in ("train", "car"):
        t = cond.get(k) or {}
        if t.get("status") not in STAT: E(f"conditions.{k}.status", f"must be one of {sorted(STAT)}")
        if not nonempty(t.get("text", "")): E(f"conditions.{k}.text", "empty")
    for i, c in enumerate(cond.get("commute", [])):
        if not all(nonempty(c.get(k, "")) for k in ("when", "text", "url")): E(f"conditions.commute[{i}]", "needs when, text and url")

# ---------- items ----------
items = doc.get("items", [])
SECTIONS = {"AI", "World", "Spain", "Culture", "Buzz"}
AI_KEYS = ["Problem", "Method", "Results", "Caveats", "For your work"]
NEWS_KEYS = ["Background", "What happened", "What's next"]
ids = set()
for n, it in enumerate(items):
    iid = it.get("id", f"#{n}")
    w = f"item {iid}"
    if iid in ids: E(w, "duplicate id")
    ids.add(iid)
    if not re.fullmatch(rf"{re.escape(str(date))}-[A-Za-z0-9-]+", str(iid)): E(w, "id must be <date>-<slug> with letters, digits and hyphens only")
    sec = it.get("section")
    if sec not in SECTIONS: E(w, f"section {sec!r} not in {sorted(SECTIONS)}")
    if sec == "AI" and it.get("kind") not in ("paper", "news"): E(w, "AI items need kind 'paper' or 'news'")
    if sec != "AI" and "kind" in it: E(w, "kind is only for AI items")
    if it.get("importance") not in ("High", "Med", "Low"): E(w, "importance must be High, Med or Low")
    for k in ("title", "text", "source"):
        if not nonempty(it.get(k, "")): E(w, f"{k} is empty")
    if not str(it.get("url", "")).startswith("http"): E(w, "url missing or not http(s)")
    if "update" in it and it["update"] is not True: E(w, "update must be true or omitted")
    cs = it.get("concepts")
    if not isinstance(cs, list) or not 1 <= len(cs) <= 3 or not nonempty(cs): E(w, "needs 1-3 concepts")
    det = it.get("details")
    keys = AI_KEYS if sec == "AI" else NEWS_KEYS
    if not isinstance(det, dict): E(w, "details missing (every item needs a Details panel)")
    else:
        for k in keys:
            if not nonempty(det.get(k)): E(w, f"details['{k}'] missing or empty")
        extra = set(det) - set(keys)
        if extra: E(w, f"unexpected details keys {sorted(extra)} (expected {keys})")
    if sec == "AI" and it.get("kind") == "paper" and "arxiv.org" in str(it.get("url", "")) and "arXiv" not in str(it.get("source", "")):
        C(w, "arXiv paper whose source label does not say 'arXiv <id>'")

highs = [i for i in items if i.get("importance") == "High"]
if highs and items and items[0].get("importance") != "High": E("items", "the first item must be the most important High story (the page leads with it)")

def count(f): return sum(1 for i in items if f(i))
papers = count(lambda i: i.get("kind") == "paper")
ainews = count(lambda i: i.get("section") == "AI" and i.get("kind") == "news")
world, spain = count(lambda i: i.get("section") == "World"), count(lambda i: i.get("section") == "Spain")
if papers < 6: C("items", f"only {papers} papers (target 6-8): only OK if no more eligible papers exist; say so in the push")
if not 3 <= ainews <= 5: C("items", f"{ainews} AI news items (target 3-5, more only on a big day)")
if not 3 <= world <= 7 and world: C("items", f"{world} World items (target 3-7)")
if spain > 4: E("items", f"{spain} Spain items (max 4)")
for s in ("Culture", "Buzz"):
    if count(lambda i: i.get("section") == s) > 3: E("items", f"more than 3 {s} items")
if doc.get("quiet") is not (world == 0 and spain == 0): E("quiet", "must be true exactly when there are no World and no Spain items")
GENERIC = {"Elections", "Markets", "Global health", "Extreme weather", "Middle East", "Europe", "Asia", "Africa", "Latin America", "Conflicts"}
story = {}
for i in items:
    if i.get("section") == "World":
        for c in i.get("concepts", []):
            if c not in GENERIC: story.setdefault(c, []).append(i.get("id"))
for c, v in story.items():
    if len(v) > 2: C("items", f"{len(v)} World items share the story '{c}' (max 2 per ongoing story)")

# ---------- podcast ----------
pod = doc.get("podcast")
if not isinstance(pod, dict) or not pod.get("segments"): E("podcast", "missing script")
else:
    segs = pod["segments"]
    words = 0
    for n, s in enumerate(segs):
        w = f"podcast.segments[{n}]"
        if s.get("host") not in ("A", "B") or s.get("name") != {"A": "Marta", "B": "Leo"}.get(s.get("host")): E(w, "host A must be Marta, host B Leo")
        t = s.get("text", "")
        if not t.strip(): E(w, "empty text"); continue
        words += len(t.split())
        if len(t.split()) > 60: C(w, f"{len(t.split())} words (keep segments under about 60)")
        if re.search(r"https?://|www\.|arxiv|\[\[|\*\*|`|#", t, re.I): E(w, "contains a URL, arXiv id or markdown")
        dig = [d for d in re.findall(r"(?<![\w-])\d[\d.,]*\b", t) if not re.search(r"\b[A-Z][\w-]*\s" + re.escape(d) + r"\b", t)]
        if dig: C(w, f"numbers written as digits {dig[:4]} (write them as spoken)")
    if not 600 <= words <= 1050: C("podcast", f"{words} words (target 600-1050)")
    if "audio" in pod:
        if not isinstance(pod.get("duration"), (int, float)): E("podcast.duration", "missing")
        if len(pod.get("starts", [])) != len(segs): E("podcast.starts", "needs one start time per segment (re-render the audio after changing the script)")

# ---------- Sunday review ----------
try: sunday = datetime.date.fromisoformat(str(date)).weekday() == 6
except ValueError: sunday = False
if sunday:
    wk = doc.get("weekly")
    if not isinstance(wk, dict) or not nonempty(wk.get("intro", "")): E("weekly", "Sunday edition needs weekly.intro")
    else:
        n = len(wk.get("items", []))
        if not 4 <= n <= 6: C("weekly", f"{n} weekly items (target 4-6)")
        for i in wk.get("items", []):
            if not all(nonempty(i.get(k, "")) for k in ("id", "title", "text", "url")): E(f"weekly {i.get('id')}", "needs id, title, text and url")

# ---------- already covered (log) ----------
if LOG:
    old = {}
    for f in glob.glob(os.path.join(LOG, "**", "*.json"), recursive=True):
        d = json.load(open(f)); d = d.get("data", d) if isinstance(d.get("data"), dict) else d
        if d.get("sent") and d.get("sent") < str(date):
            old[os.path.basename(f)[:-5]] = d
    urls = {d.get("url"): k for k, d in old.items() if d.get("url")}
    for i in items:
        if i.get("url") in urls and not i.get("update"):
            E(f"item {i.get('id')}", f"same url as already-covered {urls[i['url']]} (drop it, or report only the new development with update: true)")

# ---------- figures and quotes vs. the saved source ----------
WORDNUM = {w: str(n) for n, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split())}
WORDNUM.update({"thirty": "30", "forty": "40", "fifty": "50", "hundred": "100", "thousand": "1000", "dozen": "12",
                "uno": "1", "una": "1", "dos": "2", "tres": "3", "cuatro": "4", "cinco": "5", "seis": "6", "siete": "7", "ocho": "8", "nueve": "9", "diez": "10", "cien": "100", "mil": "1000", "centenar": "100", "docena": "12", "millón": "1000000", "million": "1000000"})
NUM = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)*")

def values(tok):
    """All numeric readings of a token: '1,240' -> 1240 (or 1.24), '2,6' -> 2.6, '1.000' -> 1000 or 1.0."""
    out = set()
    for t in {tok, tok.replace(",", ""), tok.replace(".", "").replace(",", "."), tok.replace(",", ".")}:
        try: out.add(round(float(t), 6))
        except ValueError: pass
    return out

def source_numbers(text):
    vals = set()
    for tok in NUM.findall(text): vals |= values(tok)
    for wd in re.findall(r"[a-zA-Z]+", text.lower()):
        if wd in WORDNUM: vals.add(float(WORDNUM[wd]))
    # scaled forms: '$1.32 trillion' / '235 billion' / '4B' also match 1.32, 235, 4 (already), and per-thousand forms
    # Allow honest rounding: 1.32 -> 1.3, 116.72 -> 117.
    for v in list(vals):
        for nd in (0, 1, 2): vals.add(round(v, nd))
    return vals

def norm(s):
    s = unicodedata.normalize("NFKC", s).casefold()
    s = re.sub(r"[\"'“”‘’«»`´]", "", s)
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s%$€.,-]", " ", s)).strip()

if SRC:
    for i in items:
        iid = i.get("id"); w = f"item {iid}"
        p = os.path.join(SRC, f"{iid}.json")
        if not os.path.exists(p):
            C(w, "no saved source: figures not verified (run extract_source.py, then the page reader if it fails)"); continue
        s = json.load(open(p)); s = s.get("data", s) if isinstance(s.get("data"), dict) else s
        stext = s.get("text", "")
        if len(stext) < 1500 or s.get("ok") is False:
            C(w, f"source text too short ({len(stext)} chars): retry with the page reader; figures not verified"); continue
        svals, snorm = source_numbers(stext), norm(stext)
        # Skip numbers in model/product names and identifiers (GPT-6.1, Qwen3.5-4B, CVE-2026-..., C-8) unless they appear standalone.
        body = f"{i.get('title', '')} \n {i.get('text', '')}"
        missing = []
        for m in NUM.finditer(body):
            tok = m.group(0)
            before, after = body[max(0, m.start() - 1):m.start()], body[m.end():m.end() + 1]
            if before.isalpha() or before == "-" or (after.isalpha() and after.lower() not in "xbmkt"): continue
            if values(tok) & svals: continue
            if re.fullmatch(r"(19|20)\d\d", tok): continue  # years
            if tok.replace(",", "").replace(".", "").isdigit() and float(tok.replace(",", "")) <= 10 and len(tok) == 1: continue
            missing.append(tok)
        if missing:
            C(w, f"figures not found in the source: {sorted(set(missing))} (fix them, or confirm each is a calculation from source figures)")
        for q in re.findall(r"[\"“«]([^\"”»]{12,})[\"”»]", body):
            if len(q.split()) >= 4 and norm(q) not in snorm:
                C(w, f"quote not found verbatim in the source: \"{q[:60]}\"")

print(f"Edition {date}: {len(items)} items ({papers} papers, {ainews} AI news, {world} World, {spain} Spain)")
for e in errors: print("ERROR  ", e)
for c in checks: print("CHECK  ", c)
if not errors and not checks: print("OK: ready to publish")
sys.exit(1 if errors else 2 if checks else 0)
