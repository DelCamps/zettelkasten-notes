"""Build Obsidian notes for the Morning Brief into <vault>/Notes/Daily Knowledge/.
Usage: python3 make_notes.py <vault_dir> <briefs_dir> <log_dir> <concepts_json>
Never overwrites an existing note's '# My notes' section."""
import json, os, re, sys, glob

vault, briefs_dir, log_dir, concepts_path = sys.argv[1:5]
ROOT = os.path.join(vault, "Notes", "Daily Knowledge")
CONCEPTS = json.load(open(concepts_path))  # {item_id: [concept, ...]}

def clean(s):
    s = re.sub(r'[\\/:*?"<>|#^\[\]]', "", s).strip()
    return re.sub(r"\s+", " ", s)[:90].rstrip(" .")

def note_name(it):
    t = re.sub(r"^Update:\s*", "", it["title"])
    return clean(t)

items = {}
for f in sorted(glob.glob(os.path.join(briefs_dir, "*.json"))):
    d = json.load(open(f)); d = d.get("data", d)
    for it in d.get("items", []):
        items[it["id"]] = dict(it, date=d["date"])
for f in sorted(glob.glob(os.path.join(log_dir, "*.json"))):
    d = json.load(open(f)); d = d.get("data", d)
    iid = os.path.basename(f)[:-5]
    if iid not in items and d.get("by", "brief") == "brief":
        items[iid] = {"id": iid, "section": d.get("section", "AI"), "importance": "", "title": d["title"],
                      "text": "", "url": d.get("url", ""), "source": "", "date": d.get("sent") or iid[:10]}

def folder(it):
    if it["section"] != "AI": return "News"
    return "Papers" if "arxiv.org" in it.get("url", "") else "AI"

concept_links = {}
by_day = {}
for iid, it in sorted(items.items()):
    name = note_name(it)
    sub = folder(it)
    path = os.path.join(ROOT, sub, name + ".md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    concepts = it.get("concepts") or CONCEPTS.get(iid, [])
    for c in concepts: concept_links.setdefault(c, []).append((it["date"], name))
    by_day.setdefault(it["date"], []).append((it, name))
    mine = ""
    if os.path.exists(path):
        old = open(path).read()
        if "# My notes" in old: mine = old.split("# My notes", 1)[1].split("\n---\n# References", 1)[0].strip("\n")
    section = "Culture" if it["section"] == "Culture" else it["section"]
    tags = " ".join(["#daily-knowledge", "#" + section.lower()] + (["#update"] if it.get("update") else []))
    fm = ["---", f"date: {it['date']}", f"section: {section}", f"importance: {it.get('importance') or 'n/a'}",
          f"source: \"{it.get('source') or ''}\"", f"url: {it.get('url','')}", "status: unread", f"id: {iid}", "---"]
    body = [*fm, f"{it['date']} 07:16", f"Tags: {tags}", "", "---",
            f"# {name}", "", it.get("text") or "_(Headline only; see the source.)_", "",
            "**Concepts:** " + (" · ".join(f"[[{c}]]" for c in concepts) if concepts else "_none yet_"),
            f"**From:** [[{it['date']}]]", "", "# My notes", mine, "", "---", "# References",
            f"[{it.get('source') or 'Source'}]({it.get('url','')})", ""]
    open(path, "w").write("\n".join(body))

# Concept hubs: keep anything the user wrote above the auto list
for c, links in concept_links.items():
    path = os.path.join(ROOT, "Concepts", clean(c) + ".md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    head = f"Tags: #concept #daily-knowledge\n\n---\n# {c}\n\n"
    if os.path.exists(path):
        old = open(path).read()
        head = old.split("## Linked from the brief", 1)[0]
    lst = "\n".join(f"- {d} · [[{n}]]" for d, n in sorted(set(links), reverse=True))
    open(path, "w").write(head + "## Linked from the brief\n" + lst + "\n")

# Daily notes
order = {"High": 0, "Med": 1, "Low": 2}
for day, lst in by_day.items():
    path = os.path.join(ROOT, "Daily", day + ".md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    out = [f"{day} 07:16", "Tags: #daily-knowledge #daily", "", "---", f"# Morning Brief {day}", ""]
    for sec in ["AI", "World", "Spain", "Culture", "Buzz"]:
        s = sorted([x for x in lst if x[0]["section"] == sec], key=lambda x: order.get(x[0].get("importance"), 3))
        if s:
            out.append(f"## {sec}")
            out += [f"- [[{n}]]" + (f" ({it['importance']})" if it.get("importance") else "") for it, n in s]
            out.append("")
    open(path, "w").write("\n".join(out))

# Index
idx = os.path.join(ROOT, "Daily Knowledge.md")
open(idx, "w").write("""Tags: #daily-knowledge

---
# Daily Knowledge

Notes written automatically from the Morning Brief, one per story or paper.
- **Daily/**: one note per edition
- **Papers/** and **AI/**: research, releases and safety findings
- **News/**: World, Spain and pop culture
- **Concepts/**: hub notes that link everything on a topic (open the graph view to see clusters)

Write your own thoughts under "# My notes" in any note and set `status: read`. The brief never overwrites that section.
""")
print(len(items), "notes,", len(concept_links), "concepts,", len(by_day), "days")
