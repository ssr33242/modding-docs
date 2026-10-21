#!/ coding: utf-8 -*-
"""Собирает сайт: раскладывает содержимое репозитория в .site-src/ и запускает mkdocs.

Зачем: mkdocs требует, чтобы docs_dir был подкаталогом конфига, а материалы
репозитория лежат в нескольких папках (docs/, guides/, knowledge/). Скрипт
собирает их в одном месте и запускает сборку.

    python scripts/build_site.py            # обычная сборка
    python scripts/build_site.py --strict   # строгий режим (как в CI)
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGE = ROOT / ".site-src"
SITE = ROOT / "site"

# что копируем в staging-каталог: (источник, назначение)
PAYLOAD = [
    ("docs", "docs"),
    ("guides", "guides"),
    ("knowledge", "knowledge"),
    ("index.md", "index.md"),
    ("COMPATIBILITY.md", "COMPATIBILITY.md"),
    ("versions.json", "versions.json"),
]


def stage():
    if STAGE.exists():
        shutil.rmtree(STAGE)
    STAGE.mkdir(parents=True)
    for src, dst in PAYLOAD:
        s = ROOT / src
        if not s.exists():
            print(f"  пропущено (нет {src})")
            continue
        target = STAGE / dst
        if s.is_dir():
            shutil.copytree(s, target)
        else:
            shutil.copy2(s, target)
        print(f"  + {src} -> {dst}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="строгая сборка (ошибки — как ошибки)")
    args = ap.parse_args()

    print("Подготовка содержимого сайта:")
    stage()

    cmd = [sys.executable, "-m", "mkdocs", "build"]
    if args.strict:
        cmd.append("--strict")
    cmd += ["--site-dir", str(SITE)]

    print("\nСборка:", " ".join(cmd))
    r = subprocess.run(cmd, cwd=ROOT)
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
