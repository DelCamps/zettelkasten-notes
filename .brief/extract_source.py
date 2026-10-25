"""Fetch a story's primary source and save its main text as a JSON doc for the brief's 'sources' collection.
Usage: python3 -I extract_source.py <item_id> <url> <out_dir>   (writes <out_dir>/<item_id>.json)
Output: {itemId, url, chars, fetchedAt, text, method, ok}. ok is false (and exit code 2) when no usable text
(at least 1,500 readable characters) could be extracted: retry with the page reader and save that text instead."""
import sys, json, re, subprocess, time, tempfile, os, gzip, zlib, shutil, html as htmlmod
from html.parser import HTMLParser

MIN_CHARS = 1500
iid, url, out = sys.argv[1:4]

def has_trafilatura(py):
    return subprocess.run([py, "-I", "-c", "import trafilatura"], capture_output=True).returncode == 0

# pip may install trafilatura for a different interpreter than `python3` (e.g. 3.13 vs 3.11): re-run under one that has it.
try:
    import trafilatura
except ImportError:
    trafilatura = None
    if not os.environ.get("BRIEF_EXTRACT_REEXEC"):
        for name in ("python3.13", "python3.12", "python3.11", "python3"):
            py = shutil.which(name)
            if py and os.path.realpath(py) != os.path.realpath(sys.executable) and has_trafilatura(py):
                os.environ["BRIEF_EXTRACT_REEXEC"] = "1"
                os.execv(py, [py, "-I", os.path.abspath(__file__)] + sys.argv[1:])

UAS = ["Mozilla/5.0 (MorningBrief)",
       "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"]

def fetch(u, ua):
    r = subprocess.run(["curl", "-sSL", "--compressed", "--max-time", "60", "-A", ua,
                        "-H", "Accept-Language: en,es;q=0.8", "-o", "-", u], capture_output=True)
    data = r.stdout
    # Some servers send gzip/deflate even when not asked; --compressed usually handles it, but be safe.
    if data[:2] == b"\x1f\x8b":
        try: data = gzip.decompress(data)
        except Exception: pass
    elif data[:1] == b"\x78":
        try: data = zlib.decompress(data)
        except Exception: pass
    return data

class Strip(HTMLParser):
    """Stdlib fallback when trafilatura is unavailable: keep text from content tags, drop scripts and chrome."""
    SKIP = {"script", "style", "noscript", "nav", "header", "footer", "aside", "form", "svg"}
    BLOCK = {"p", "h1", "h2", "h3", "h4", "li", "pre", "blockquote", "tr", "div", "section", "article", "br"}
    def __init__(self):
        super().__init__(); self.depth = 0; self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP: self.depth += 1
        elif tag in self.BLOCK: self.parts.append("\n")
    def handle_endtag(self, tag):
        if tag in self.SKIP and self.depth: self.depth -= 1
    def handle_data(self, d):
        if not self.depth: self.parts.append(d)

def html_text(raw):
    page = raw.decode("utf-8", "ignore")
    if trafilatura:
        t = trafilatura.extract(page, include_tables=True, include_formatting=True) or ""
        if t: return t, "trafilatura"
    s = Strip(); s.feed(page)
    lines = [re.sub(r"[ \t]+", " ", l).strip() for l in "".join(s.parts).split("\n")]
    return "\n".join(l for l in lines if len(l) > 40), "html-strip"

def pdf_text(raw):
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f: f.write(raw); p = f.name
    try: return subprocess.run(["pdftotext", "-layout", p, "-"], capture_output=True, text=True).stdout, "pdftotext"
    finally: os.unlink(p)

def readable(t):
    """Share of characters in Latin scripts, general punctuation or currency (catches binary saved as text,
    which decodes to a scatter of control, Armenian, Cyrillic etc. characters)."""
    if not t: return 0.0
    ok = sum(1 for c in t if (c.isprintable() or c in "\n\t") and (ord(c) < 0x250 or 0x2000 <= ord(c) <= 0x20CF))
    return ok / len(t)

def extract(raw):
    if raw[:4] == b"%PDF": return pdf_text(raw)
    return html_text(raw)

def good(t): return len(t) >= MIN_CHARS and readable(t) > 0.97

m = re.search(r"arxiv\.org/(?:abs|html|pdf)/([0-9]{4}\.[0-9]{4,5})(v\d+)?", url)
if m:
    a = m.group(1)
    cands = [f"https://arxiv.org/html/{a}", f"https://arxiv.org/pdf/{a}", f"https://arxiv.org/abs/{a}"]
else:
    cands = [url]

best = ("", url, "none")
for u in cands:
    for ua in UAS:
        raw = fetch(u, ua)
        if not raw: continue
        t, how = extract(raw)
        t = re.sub(r"\n{3,}", "\n\n", htmlmod.unescape(t)).strip()
        if readable(t) > 0.97 and len(t) > len(best[0]): best = (t, u, how)
        if good(t): break
        time.sleep(1)
    if good(best[0]): break

text, used, how = best
text = text[:90000]
ok = good(text)
os.makedirs(out, exist_ok=True)
json.dump({"itemId": iid, "url": used, "chars": len(text), "fetchedAt": int(time.time() * 1000), "text": text,
           "method": how, "ok": ok}, open(os.path.join(out, iid + ".json"), "w"), ensure_ascii=False)
print(iid, len(text), used, how, "OK" if ok else "UNAVAILABLE: retry with the page reader")
sys.exit(0 if ok else 2)
