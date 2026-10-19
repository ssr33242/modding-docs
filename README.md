# Minecraft Modding Reference

Рабочий справочник по созданию модов Minecraft с нуля: матрица совместимости,
проверенные шаблоны проектов и пошаговые инструкции.

Всё здесь **проверено реальной сборкой** — версии и требования не выдуманы.

## Структура

- `COMPATIBILITY.md` — матрица «версия Minecraft ↔ ядро ↔ Gradle ↔ JDK», проверенная сборками
- `templates/fabric/` — шаблон Fabric-мода (собирается в .jar)
- `templates/neoforge/` — шаблон NeoForge-мода (собирается в .jar)
- `guides/` — пошаговые инструкции: от пустой папки до готового .jar
- `versions.json` — зафиксированные рабочие комбинации версий

## Быстрый старт

1. Выбери ядро и версию по `COMPATIBILITY.md`.
2. Скопируй шаблон из `templates/<ядро>/`.
3. Подставь свои `MOD_ID`, версии и пакет.
4. Собери: `gradle build`.
5. Готовый `.jar` — в `build/libs/`.

## Официальная документация

- Fabric: https://docs.fabricmc.net/
- NeoForge: https://docs.neoforged.net/
- Forge: https://docs.minecraftforge.net/
- Minecraft Wiki: https://minecraft.wiki/
