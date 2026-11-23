"""Erstellt 04-content/kanal/INDEX.md: Übersicht aller Skripte mit
Status, Wortzahl und geschätzter Sprechdauer.

Aufruf: python 05-automation/kanal/skript_index.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
SKRIPTE = ROOT / "04-content" / "kanal" / "skripte"
INDEX = ROOT / "04-content" / "kanal" / "INDEX.md"
WOERTER_PRO_MIN = 140  # ruhige KI-Stimme


def front_matter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    data = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                data[k.strip()] = v.strip()
    return data


def sprechtext(text):
    m = re.search(r"## Sprechtext\n(.*?)(\n## |\Z)", text, re.S)
    return m.group(1) if m else ""


def main():
    rows = []
    for f in sorted(SKRIPTE.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        fm = front_matter(text)
        words = len(sprechtext(text).split())
        sek = round(words / WOERTER_PRO_MIN * 60)
        hinweis = "⚠️ unter 1 Min." if sek < 62 else ("⚠️ zu lang" if sek > 110 else "✅")
        rows.append(
            f"| {fm.get('nr', '?')} | [{fm.get('titel', f.stem)}](skripte/{f.name}) "
            f"| {fm.get('format', '')} | {fm.get('status', '')} | {words} | ~{sek} s {hinweis} |"
        )
    out = [
        "# Skript-Übersicht",
        "",
        "Automatisch erzeugt – nicht von Hand bearbeiten.",
        f"Dauer geschätzt mit {WOERTER_PRO_MIN} Wörtern/Min.",
        "",
        "| Nr. | Titel | Format | Status | Wörter | Dauer |",
        "|---|---|---|---|---|---|",
        *rows,
        "",
    ]
    INDEX.write_text("\n".join(out), encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    main()
