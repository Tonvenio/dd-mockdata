#!/usr/bin/env python3
"""rename_companies.py - surgical, idempotent rename of the fictional company
and product brands that were too close to real-world businesses.

Mirrors the approach of fix_real_persons.py: a plain string replacement across
all docx/xlsx content and the source files. Machine identifiers (the
roehrig_large/ folder, short codes REA/MMB/BTP, the Python constant ROEHRIG_AG,
and KG URIs like org/rea) are deliberately left intact - only human-readable
names change.

    <surname1> Elektronik AG     -> Brennhagen Elektronik AG   (cf. EP:Roehrig)
    <surname2> Maschinenbau GmbH -> Halbreiter Maschinenbau GmbH
    BioTech Precision GmbH       -> Sentavia Precision GmbH
    OrthoFix Navigator           -> Ostevo Navigator           (cf. Orthofix Medical)
    CardioScan Pro               -> Cardevio Pro                (cf. CardioScan dx)
    DiagnoKit SARS-Flex          -> Veridiq SARS-Flex           (cf. DiagNova)

Run:  python3 regen/rename_companies.py [ROOT ...]   (default: this repo root)
Idempotent: re-running after a successful pass changes nothing. The script
skips itself so the literal mapping table below is never rewritten.
"""
from __future__ import annotations
import io
import sys
import zipfile
from pathlib import Path

# The old brand tokens are assembled from escapes so this very file does not
# contain the literal source strings (belt-and-braces with the self-skip below).
_OE = "ö"  # o-umlaut
_UE = "ü"  # u-umlaut
ROEHRIG_U = "R" + _OE + "hrig"      # umlaut form
ROEHRIG_A = "Roehrig"               # ASCII-folded form
MUELLER_U = "M" + _UE + "ller Maschinenbau"
MUELLER_A = "Mueller Maschinenbau"

# Ordered longest-first so multi-word brands resolve before the bare token.
# DATA map applies to document content (docx/xlsx) and includes lowercase
# domain forms. CODE map applies to source files and excludes the bare
# lowercase roehrig/rohrig token so paths / dict-keys / identifiers stay intact.
_SHARED = [
    (MUELLER_U, "Halbreiter Maschinenbau"),
    (MUELLER_A, "Halbreiter Maschinenbau"),
    ("BioTech Precision", "Sentavia Precision"),
    ("biotech-precision", "sentavia-precision"),
    ("mueller-maschinenbau", "halbreiter-maschinenbau"),
    ("roehrig-elektronik", "brennhagen-elektronik"),
    ("OrthoFix", "Ostevo"),
    ("CardioScan", "Cardevio"),
    ("DiagnoKit", "Veridiq"),
    (ROEHRIG_U, "Brennhagen"),
    (ROEHRIG_A, "Brennhagen"),
]
_DATA_ONLY = [
    ("roehrig", "brennhagen"),
    ("Rohrig", "Brennhagen"),
    ("rohrig", "brennhagen"),
]
MAP_DATA = _SHARED + _DATA_ONLY
MAP_CODE = _SHARED

TEXT_EXT = {".py", ".md", ".ttl", ".cff", ".txt", ".json", ".jsonld", ".csv"}
ZIP_EXT = {".docx", ".xlsx"}
SKIP_DIRS = {".git", "__pycache__", ".venv", "node_modules", ".pytest_cache"}
SELF = Path(__file__).resolve()


def _apply(text: str, mapping) -> str:
    for a, b in mapping:
        text = text.replace(a, b)
    return text


def _rewrite_zip(path: Path) -> bool:
    """Replace brand strings inside the XML parts of a docx/xlsx; return True
    if the file changed."""
    with zipfile.ZipFile(path) as zin:
        items = [(i, zin.read(i.filename)) for i in zin.infolist()]
    changed = False
    out: list[tuple[zipfile.ZipInfo, bytes]] = []
    for info, data in items:
        if info.filename.endswith((".xml", ".rels")):
            try:
                s = data.decode("utf-8")
            except UnicodeDecodeError:
                out.append((info, data)); continue
            ns = _apply(s, MAP_DATA)
            if ns != s:
                changed = True
                data = ns.encode("utf-8")
        out.append((info, data))
    if not changed:
        return False
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zout:
        for info, data in out:
            zout.writestr(info, data)
    path.write_bytes(buf.getvalue())
    return True


def process(root: Path) -> tuple[int, int]:
    docs = code = 0
    for p in root.rglob("*"):
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if not p.is_file() or p.resolve() == SELF:
            continue
        ext = p.suffix.lower()
        if ext in ZIP_EXT:
            if _rewrite_zip(p):
                docs += 1
        elif ext in TEXT_EXT:
            try:
                s = p.read_text(encoding="utf-8")
            except (UnicodeDecodeError, ValueError):
                continue
            ns = _apply(s, MAP_CODE)
            if ns != s:
                p.write_text(ns, encoding="utf-8")
                code += 1
    return docs, code


def main(argv: list[str]) -> int:
    roots = [Path(a) for a in argv[1:]] or [SELF.parent.parent]
    for root in roots:
        docs, code = process(root.resolve())
        print(f"{root}: {docs} docx/xlsx + {code} source files updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
