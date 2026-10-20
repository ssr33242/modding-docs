# Minecraft Modding Reference

Рабочий справочник по созданию контента для Minecraft с нуля: моды, плагины,
аддоны. Матрица совместимости, проверенные шаблоны и пошаговые инструкции.

Всё здесь **проверено реальной сборкой** — версии и требования не выдуманы.
Справочные материалы опираются на **официальные источники** (Mojang, Microsoft,
MinecraftForge, NeoForged, FabricMC, PaperMC).

## Что покрывает

- **Java-моды**: Fabric, NeoForge, Forge, Quilt
- **Серверные плагины**: Bukkit, Spigot, Paper
- **Аддоны**: Java-аддоны, аддоны-плагины, Bedrock-аддоны
- **Bedrock Edition**: поведенческие и ресурсные пакеты, Script API, меню,
  JSON UI, команды, площадки
- **Серверы Bedrock**: Geyser, Floodgate, Nukkit, PocketMine, Dragonfly

## Структура

- `COMPATIBILITY.md` — матрица «версия Minecraft ↔ ядро ↔ Gradle ↔ JDK»
- `knowledge/knowledge-map.md` — **начни отсюда**: что где лежит и как выбрать
- `docs/` — справочники по конкретным темам (официальные источники):
  - `docs/java/versions.md` — актуальные версии Minecraft и загрузчиков
  - `docs/java/commands.md` — команды через `/` (Brigadier, регистрация)
  - `docs/java/events.md` — события (Forge/NeoForge)
  - `docs/java/menus-gui.md` — экраны и меню (Screen, AbstractContainerScreen)
  - `docs/java/registries.md` — регистрация блоков, предметов и прочего
  - `docs/bedrock/addon-structure.md` — структура аддона, манифесты, UUID
  - `docs/bedrock/commands.md` — команды Bedrock через `/` + свои команды
  - `docs/bedrock/forms-menus.md` — меню: формы, диалоги NPC, JSON UI
  - `docs/bedrock/json-ui.md` — JSON UI: экраны и элементы
  - `docs/bedrock/scripting.md` — скрипты `@minecraft/server`
  - `docs/bedrock/validation.md` — проверка аддона перед сборкой (чек-лист)
  - `docs/programming/repos.md` — официальные репозитории по программированию
- `templates/` — шаблоны проектов:
  - `fabric/`, `neoforge/`, `forge/`, `quilt/` — Java-моды
  - `plugin/` — плагин Paper (Maven + Gradle)
  - `addon-plugin/` — аддон-плагин
  - `bedrock/` — аддон Bedrock (behavior pack + resource pack + скрипт)
- `guides/` — пошаговые инструкции от пустой папки до готового файла
- `guides/repos-catalog.md` — **большой каталог репозиториев** по всем темам
- `guides/tools.md` — инструменты моддинга: сборка, модели, датапаки, отладка
- `guides/resources.md` — справочник ссылок: документация, API версий, комьюнити
- `versions.json` — зафиксированные рабочие комбинации версий + живые версии

## Быстрый старт

1. Определи платформу: Java (мод/плагин) или Bedrock (аддон).
2. Открой `knowledge/knowledge-map.md` — выбери ядро/тип.
3. Скопируй шаблон из `templates/<тип>/`.
4. Подставь свои `MOD_ID`/`group`, версии и пакет.
5. Собери (`gradle build` / `mvn package` / zip).
6. Готовый файл — в `build/libs/`, `target/` или `.mcaddon`.

## Важно про версии

- Minecraft: Java Edition сменил нумерацию: после `1.21.11` идут `26.1`,
  `26.2`, `26.3`. Актуальный релиз — **26.3**.
- Bedrock Edition: актуальная версия — **1.26.50.4**.
- Всегда проверяйте версии в живых источниках (см. `docs/java/versions.md`),
  а не по памяти.

## Проверено реальной сборкой

Эти комбинации не «документация по слухам», а результат настоящей сборки:

- **Java-мод, NeoForge 26.3** — собрано `mysticmod-1.0.0.jar`: JDK 25,
  Gradle 9.2.1, ModDevGradle 2.0.148, `neo_version=26.3.0.95`.
  Шаблон — официальный `github.com/NeoForgeMDKs/MDK-26.3-ModDevGradle`.
- **Java-мод, Fabric** — собран `modid-1.0.0.jar` на MC 1.21 (Loom 1.18.4,
  Gradle 9.7.1). Важно: Loom 1.18.x требует **JDK 25**, не 21.
- **Плагин, Paper 26.3** — собран `exampleplugin-1.0.0.jar`
  (`paper-api 26.3.build.207-stable`, Maven 3.9.9, JDK 25).
- **Аддон Bedrock** — `mystic_amulet.mcaddon` (предмет) и
  `mystic_creatures.mcaddon` (сущность + блок + скрипт): валидны по
  чек-листу `docs/bedrock/validation.md`.

Важно про поддержку версий: **Fabric пока не поддерживает MC 26.x** — маппинги
Yarn останавливаются на `1.21.11`. NeoForge/Forge и Paper идут следом за
Minecraft с разной задержкой — проверяйте каждое ядро отдельно.

## Официальная документация

- Fabric: https://docs.fabricmc.net/
- NeoForge: https://docs.neoforged.net/
- Forge: https://docs.minecraftforge.net/
- Quilt: https://wiki.quiltmc.org/
- Paper: https://docs.papermc.io/
- Bedrock (Creator): https://learn.microsoft.com/minecraft/creator/
- Bedrock-схемы: https://github.com/MicrosoftDocs/minecraft-creator
- Bedrock-примеры: https://github.com/Mojang/bedrock-samples
- Brigadier (команды): https://github.com/Mojang/brigadier
- Minecraft Wiki: https://minecraft.wiki/

## Первоисточники (форки в этом аккаунте)

- Fabric — https://github.com/ssr33242/fabric-docs
- NeoForge — https://github.com/ssr33242/neoforge-docs
- Forge — https://github.com/ssr33242/forge-docs
