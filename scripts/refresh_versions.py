#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Обновляет versions.json живыми данными с официальных источников.

Запускается вручную или по расписанию (GitHub Actions:
.github/workflows/refresh-versions.yml). При недоступности сети файл не
 трогается — скрипт завершится с кодом 0 и предупреждением.

    python scripts/refresh_versions.py            # обновить versions.json
    python scripts/refresh_versions.py --check    # только проверить и вывести
"""
import argparse
import json
import re
import ssl
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSIONS = ROOT / "versions.json"

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
UA = {"User-Agent": "modding-docs-refresh/1.0"}


def get(url, timeout=45):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        return r.read().decode("utf-8", "replace")


def jget(url, timeout=45):
    return json.loads(get(url, timeout))


def maven_release(base, path):
    xml = get(f"{base}/{path}/maven-metadata.xml")
    m = re.search(r"<release>([^<]+)</release>", xml)
    return m.group(1) if m else None


def modrinth_first(project, mc_prefix=None):
    d = jget(f"https://api.modrinth.com/v2/project/{project}/version?limit=40")
    for v in d:
        gvs = [g for g in v.get("game_versions", []) if "." in g]
        mc = gvs[0] if gvs else ""
        if mc_prefix and not mc.startswith(mc_prefix):
            continue
        return v["version_number"], mc
    return None, None


def collect():
    out = {}
    errors = []

    # Minecraft
    try:
        man = jget("https://piston-meta.mojang.com/mc/game/version_manifest_v2.json")
        out["minecraft_release"] = man["latest"]["release"]
        out["minecraft_snapshot"] = man["latest"]["snapshot"]
    except Exception as e:
        errors.append(f"minecraft: {e}")

    # Fabric Loader
    try:
        loaders = jget("https://meta.fabricmc.net/v2/versions/loader")
        out["fabric_loader"] = loaders[0]["version"]
        out["fabric_loader_stable"] = loaders[0].get("stable", True)
    except Exception as e:
        errors.append(f"fabric loader: {e}")

    # Fabric API — берём версию под последний релиз
    try:
        out["fabric_api_latest"] = modrinth_first("fabric-api")[0]
    except Exception as e:
        errors.append(f"fabric api: {e}")

    # Yarn — последняя сборка
    try:
        yarn = jget("https://meta.fabricmc.net/v2/versions/yarn")
        if yarn:
            out["yarn_latest"] = yarn[0]["version"]
    except Exception as e:
        errors.append(f"yarn: {e}")

    # Loom
    try:
        out["fabric_loom"] = maven_release(
            "https://maven.fabricmc.net", "net/fabricmc/fabric-loom")
    except Exception as e:
        errors.append(f"loom: {e}")

    # NeoForge + ModDevGradle
    try:
        out["neoforge"] = maven_release(
            "https://maven.neoforged.net/releases", "net/neoforged/neoforge")
    except Exception as e:
        errors.append(f"neoforge: {e}")
    try:
        out["moddevgradle"] = maven_release(
            "https://maven.neoforged.net/releases", "net/neoforged/moddev-gradle")
    except Exception as e:
        errors.append(f"moddevgradle: {e}")

    # Forge + ForgeGradle
    try:
        out["forge"] = maven_release(
            "https://maven.minecraftforge.net", "net/minecraftforge/forge")
    except Exception as e:
        errors.append(f"forge: {e}")
    try:
        out["forgegradle"] = maven_release(
            "https://maven.minecraftforge.net", "net/minecraftforge/gradle/ForgeGradle")
    except Exception as e:
        errors.append(f"forgegradle: {e}")

    # Quilt — берём стабильную (без beta/alpha)
    try:
        q = jget("https://meta.quiltmc.org/v3/versions/loader")
        stable = [x["version"] for x in q if "beta" not in x["version"] and "alpha" not in x["version"]]
        out["quilt_loader"] = stable[0] if stable else q[0]["version"]
        out["quilt_loader_beta"] = next((x["version"] for x in q if "beta" in x["version"]), None)
    except Exception as e:
        errors.append(f"quilt: {e}")

    # Paper
    try:
        p = jget("https://fill.papermc.io/v3/projects/paper")
        vers = p.get("versions", {})
        latest = sorted(vers.keys())[-1] if isinstance(vers, dict) else None
        out["paper"] = latest
    except Exception as e:
        errors.append(f"paper: {e}")

    # Architectury — версия без суффикса загрузчика
    try:
        ver, mc = modrinth_first("architectury-api")
        out["architectury_api"] = ver.split("+")[0] if ver else None
    except Exception as e:
        errors.append(f"architectury: {e}")

    return out, errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="только показать собранные данные, не менять файл")
    args = ap.parse_args()

    data, errors = collect()
    if errors:
        print("Часть источников недоступна:", file=sys.stderr)
        for e in errors:
            print("  -", e, file=sys.stderr)

    print("Собрано:")
    for k, v in data.items():
        print(f"  {k:24} {v}")

    if args.check or not data:
        return 0

    doc = json.loads(VERSIONS.read_text(encoding="utf-8"))
    live = doc.setdefault("live_versions", {})
    mapping = {
        "minecraft_release": "minecraft_release",
        "minecraft_snapshot": "minecraft_snapshot",
        "fabric_loader": "fabric_loader",
        "fabric_api_latest": "fabric_api_latest",
        "yarn_latest": "yarn_latest",
        "fabric_loom": "fabric_loom",
        "neoforge": "neoforge",
        "moddevgradle": "moddevgradle",
        "forge": "forge",
        "forgegradle": "forgegradle",
        "quilt_loader": "quilt_loader",
        "quilt_loader_beta": "quilt_loader_beta",
        "paper": "paper",
        "architectury_api": "architectury_api",
    }
    changed = False
    for src, dst in mapping.items():
        val = data.get(src)
        if val and live.get(dst) != val:
            live[dst] = val
            changed = True
    live["checked_at"] = date.today().isoformat()

    mc = doc.setdefault("minecraft", {})
    if data.get("minecraft_release") and mc.get("latest_release") != data["minecraft_release"]:
        mc["latest_release"] = data["minecraft_release"]
        changed = True
    if data.get("minecraft_snapshot") and mc.get("latest_snapshot") != data["minecraft_snapshot"]:
        mc["latest_snapshot"] = data["minecraft_snapshot"]
        changed = True

    doc["checked_at"] = date.today().isoformat()

    if not changed:
        print("\nИзменений нет — версии в актуальном состоянии.")
        return 0

    VERSIONS.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\nversions.json обновлён ({date.today().isoformat()})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
