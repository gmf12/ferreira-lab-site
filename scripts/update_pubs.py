#!/usr/bin/env python3
"""Sincroniza a lista de publicações de index.html com o ORCID do PI.

Substitui o trecho entre <!-- ORCID-PUBS:START --> e <!-- ORCID-PUBS:END -->.
Uso: python3 scripts/update_pubs.py   (só stdlib, requer rede)
"""
import html, json, re, subprocess, sys, urllib.error, urllib.request
from pathlib import Path

ORCID = "0000-0002-1952-9428"
INDEX = Path(__file__).resolve().parent.parent / "index.html"
START, END = "<!-- ORCID-PUBS:START -->", "<!-- ORCID-PUBS:END -->"


def fetch():
    req = urllib.request.Request(
        f"https://pub.orcid.org/v3.0/{ORCID}/works",
        headers={"Accept": "application/json", "User-Agent": "libnm-site-sync"},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)["group"]
    except urllib.error.URLError:  # ex.: Python do macOS sem certificados; usa curl
        out = subprocess.run(
            ["curl", "-fsS", "-H", "Accept: application/json", req.full_url],
            capture_output=True, check=True, timeout=90,
        ).stdout
        return json.loads(out)["group"]


def clean_title(t):
    t = re.sub(r"</?(i|em)>", lambda m: "\0" + ("/" if "/" in m.group() else "") + "e\0", t, flags=re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.escape(" ".join(t.split()), quote=False)
    return t.replace("\0e\0", "<em>").replace("\0/e\0", "</em>")


def doi_of(group):
    for w in group["work-summary"]:
        for e in (w.get("external-ids") or {}).get("external-id", []):
            if e["external-id-type"] == "doi" and e.get("external-id-value"):
                return e["external-id-value"].strip()
    return None


def tag(title):
    if re.match(r"(correction|erratum|retraction)", title, re.I):
        return ("Errata", "Erratum")
    if re.search(r"review", title, re.I):
        return ("Revisão", "Review")
    return ("Artigo", "Article")


def build(groups):
    rows = []
    for g in groups:
        w = g["work-summary"][0]
        pd = w.get("publication-date") or {}
        year = (pd.get("year") or {}).get("value") or "—"
        raw = w["title"]["title"]["value"]
        journal = (w.get("journal-title") or {}).get("value") or ""
        doi = doi_of(g)
        rows.append((year, raw, journal, doi))
    rows.sort(key=lambda r: r[0], reverse=True)
    out = []
    for year, raw, journal, doi in rows:
        title = clean_title(raw)
        if doi:
            title = f'<a href="https://doi.org/{html.escape(doi, quote=True)}" target="_blank" rel="noopener">{title}</a>'
        pt, en = tag(raw)
        out.append(
            f'      <div class="pub">\n'
            f'        <div class="pub-year">{year}</div>\n'
            f'        <div class="pub-main">\n'
            f'          <div class="pub-title">{title}</div>\n'
            f'          <div class="pub-meta">{html.escape(journal, quote=False)}</div>\n'
            f'        </div>\n'
            f'        <span class="pub-tag" data-pt="{pt}" data-en="{en}">{pt}</span>\n'
            f'      </div>'
        )
    return "\n".join(out), len(rows)


def main():
    groups = fetch()
    if not groups:
        sys.exit("ORCID retornou lista vazia; abortando para não apagar a página.")
    body, n = build(groups)
    s = INDEX.read_text(encoding="utf-8")
    a, b = s.index(START) + len(START), s.index(END)
    new = s[:a] + "\n" + body + "\n      " + s[b:]
    new = re.sub(r'(<span id="pub-count">)\d+(</span>)', rf"\g<1>{n}\g<2>", new)
    if new != s:
        INDEX.write_text(new, encoding="utf-8")
    print(f"{n} publicações; {'atualizado' if new != s else 'sem mudanças'}")


if __name__ == "__main__":
    main()
