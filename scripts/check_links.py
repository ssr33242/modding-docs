#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Проверяет внутренние ссылки в markdown-файлах репозитория.

    python scripts/check_links.py            # только внутренние
    python scripts/check_links.py --external # + внешние (медленно, с таймаутом)
"""
import argparse
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", ".venv", "site", "__pycache__"}
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SKIP_SCHEMES = ("http://", "https://", "mailto:", "tel:", "#", "data:")


def md_files():
    for p in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        yield p


def check_internal():
    broken = []
    total = 0
    for f in md_files():
        text = f.read_text(encoding="utf-8", errors="replace")
        for m in MD_LINK.finditer(text):
            target = m.group(1).strip()
            if target.startswith(SKIP_SCHEMES):
                continue
            target = target.split("#")[0].split("?")[0]
            if not target:
                continue
            total += 1
            dest = (f.parent / target).resolve()
            if not dest.exists():
                broken.append(f"{f.relative_to(ROOT)} -> {target}")
    return total, broken


def check_external(timeout=12):
    broken = []
    total = 0
    seen = set()
    for f in md_files():
        text = f.read_text(encoding="utf-8", errors="replace")
        for m in MD_LINK.finditer(text):
            target = m.group(1).strip()
            if not target.startswith(("http://", "https://")):
                continue
            if target in seen:
                continue
            seen.add(target)
            total += 1
            try:
                req = urllib.request.Request(target, method="HEAD",
                                             headers={"User-Agent": "modding-docs-linkcheck/1.0"})
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    if r.status >= 400:
                        broken.append(f"{target} -> HTTP {r.status}")
            except urllib.error.HTTPError as e:
                if e.code not in (403, 405, 501):  # многие сайты режут HEAD
                    broken.append(f"{target} -> HTTP {e.code}")
            except Exception as e:
                broken.append(f"{target} -> {type(e).__name__}")
    return total, broken


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--external", action="store_true", help="проверять и внешние ссылки")
    args = ap.parse_args()

    total, broken = check_internal()
    print(f"Внутренние ссылки: проверено {total}, битых {len(broken)}")
    for b in broken:
        print("  БИТАЯ:", b)

    if args.external:
        etotal, ebroken = check_external()
        print(f"Внешние ссылки: проверено {etotal}, недоступных {len(ebroken)}")
        for b in ebroken:
            print("  недоступна:", b)

    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
