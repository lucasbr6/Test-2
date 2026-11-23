"""Wandelt Produkt-Markdown aus 04-content/produkte/ in druckfertige PDFs.

Aufruf: python build_pdf.py <eingabe.md> [<weitere.md> ...]
Ausgabe: 04-content/pdf/<name>.pdf
"""
import pathlib
import re
import sys

import markdown
from weasyprint import HTML

ROOT = pathlib.Path(__file__).resolve().parents[2]
CSS = (pathlib.Path(__file__).parent / "style.css").read_text(encoding="utf-8")
OUT = ROOT / "04-content" / "pdf"


def strip_front_matter(text: str) -> str:
    return re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)


def build(md_path: pathlib.Path) -> pathlib.Path:
    body = markdown.markdown(
        strip_front_matter(md_path.read_text(encoding="utf-8")),
        extensions=["extra", "sane_lists"],
    )
    html = f"<!doctype html><html lang='de'><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>"
    OUT.mkdir(parents=True, exist_ok=True)
    pdf = OUT / (md_path.stem + ".pdf")
    HTML(string=html, base_url=str(md_path.parent)).write_pdf(pdf)
    return pdf


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print("PDF erstellt:", build(pathlib.Path(arg).resolve()))
