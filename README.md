# Minecraft Modding Reference

Рабочий справочник по созданию контента для Minecraft с нуля: моды, плагины,
аддоны. Матрица совместимости, проверенные шаблоны и пошаговые инструкции.

Всё здесь **проверено реальной сборкой** — версии и требования не выдуманы.

## Что покрывает

- **Java-моды**: Fabric, NeoForge, Forge, Quilt
- **Серверные плагины**: Bukkit, Spigot, Paper
- **Аддоны**: Java-аддоны, аддоны-плагины, Bedrock-аддоны
- **Bedrock Edition**: поведенческие и ресурсные пакеты, Script API, площадки
- **Серверы Bedrock**: Geyser, Floodgate, Nukkit, PocketMine, Dragonfly

## Структура

- `COMPATIBILITY.md` — матрица «версия Minecraft ↔ ядро ↔ Gradle ↔ JDK»
- `knowledge/knowledge-map.md` — **начни отсюда**: что где лежит и как выбрать
- `templates/` — шаблоны проектов:
  - `fabric/`, `neoforge/`, `forge/`, `quilt/` — Java-моды
  - `plugin/` — плагин Paper (Maven + Gradle)
  - `addon-plugin/` — аддон-плагин
  - `bedrock/` — аддон Bedrock (behavior pack + resource pack + скрипт)
- `guides/` — пошаговые инструкции от пустой папки до готового файла
- `versions.json` — зафиксированные рабочие комбинации версий

## Быстрый старт

1. Определи платформу: Java (мод/плагин) или Bedrock (аддон).
2. Открой `knowledge/knowledge-map.md` — выбери ядро/тип.
3. Скопируй шаблон из `templates/<тип>/`.
4. Подставь свои `MOD_ID`/`group`, версии и пакет.
5. Собери (`gradle build` / `mvn package` / zip).
6. Готовый файл — в `build/libs/`, `target/` или `.mcaddon`.

## Официальная документация

- Fabric: https://docs.fabricmc.net/
- NeoForge: https://docs.neoforged.net/
- Forge: https://docs.minecraftforge.net/
- Quilt: https://wiki.quiltmc.org/
- Paper: https://docs.papermc.io/
- Bedrock (Creator): https://learn.microsoft.com/minecraft/creator/
- Minecraft Wiki: https://minecraft.wiki/

## Первоисточники (форки в этом аккаунте)

- Fabric — https://github.com/ssr33242/fabric-docs
- NeoForge — https://github.com/ssr33242/neoforge-docs
- Forge — https://github.com/ssr33242/forge-docs
- Bedrock-примеры Mojang — https://github.com/Mojang/bedrock-samples
