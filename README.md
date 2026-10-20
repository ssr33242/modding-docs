# Minecraft Modding Reference

Рабочий справочник по созданию модов Minecraft с нуля: матрица совместимости,
проверенные шаблоны проектов и пошаговые инструкции.

Всё здесь **проверено реальной сборкой** — версии и требования не выдуманы.

## Структура

- `COMPATIBILITY.md` — матрица «версия Minecraft ↔ ядро ↔ Gradle ↔ JDK»
- `templates/fabric/` — шаблон Fabric-мода (собирается в .jar)
- `templates/neoforge/` — шаблон NeoForge-мода (собирается в .jar)
- `templates/forge/` — шаблон Forge-мода
- `templates/quilt/` — шаблон Quilt-мода
- `guides/` — пошаговые инструкции: от пустой папки до готового .jar
- `knowledge/` — карта знаний: что где лежит, как устроены ядра
- `versions.json` — зафиксированные рабочие комбинации версий

## Быстрый старт

1. Выбери ядро и версию по `COMPATIBILITY.md`.
2. Скопируй шаблон из `templates/<ядро>/`.
3. Подставь свои `MOD_ID`, версии и пакет.
4. Собери: `gradle build`.
5. Готовый `.jar` — в `build/libs/`.

## Ядра и их особенности

- **Fabric** — лёгкое ядро, Loom, `fabric.mod.json`, быстрая сборка, моды для версий
  «последний релиз + снапшоты».
- **NeoForge** — форк Forge для 1.20.2+, ModDevGradle, `neoforge.mods.toml`.
- **Forge** — классика, ForgeGradle, `mods.toml`; для 1.20.1 и 1.12.2 — самые
  популярные сборки модов.
- **Quilt** — форк Fabric, Quilt Loom, `quilt.mod.json`, QSL/QFAPI; умеет запускать
  Fabric-моды.

## Официальная документация

- Fabric: https://docs.fabricmc.net/
- NeoForge: https://docs.neoforged.net/
- Forge: https://docs.minecraftforge.net/
- Quilt: https://wiki.quiltmc.org/
- Minecraft Wiki: https://minecraft.wiki/

## Первоисточники (форки в этом аккаунте)

- Fabric — https://github.com/ssr33242/fabric-docs
- NeoForge — https://github.com/ssr33242/neoforge-docs
- Forge — https://github.com/ssr33242/forge-docs
