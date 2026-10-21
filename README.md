# Minecraft Modding Reference

Рабочий справочник по созданию контента для Minecraft с нуля: моды, плагины,
аддоны. Матрица совместимости, проверенные шаблоны и пошаговые инструкции.

Всё здесь **проверено реальной сборкой** — версии и требования не выдуманы.
Справочные материалы опираются на **официальные источники** (Mojang, Microsoft,
MinecraftForge, NeoForged, FabricMC, PaperMC).

> **Состояние на 21 октября 2026**
>
> | | |
> |---|---|
> | Minecraft (релиз / снапшот) | **26.3** / 26.4-snapshot-5 |
> | Fabric | ✅ поддерживает 26.x (API `0.163.0+26.3`, Loader `0.19.5`, Loom `1.18-SNAPSHOT`) |
> | NeoForge | ✅ `26.3.0.95` (ModDevGradle `2.0.148`) |
> | Forge | ✅ `26.3-66.0.13` (ForgeGradle `6.0.54`, **только Gradle 8.x**) |
> | Quilt | ❌ нет маппингов под 26.x (последняя рабочая — 1.20.6) |
> | Paper | ✅ `26.3` |
> | JDK для 26.x | **25** |
>
> Главное изменение ветки 26.x: Minecraft **больше не обфусцируется**, Yarn
> больше не выпускается → Fabric-моды под 26.x собираются на **официальных
> маппингах Mojang**. Гайд по переносу — [`docs/java/migration-26x.md`](docs/java/migration-26x.md).

## Что покрывает

- **Java-моды**: Fabric, NeoForge, Forge, Quilt
- **Серверные плагины**: Bukkit, Spigot, Paper
- **Аддоны**: Java-аддоны, аддоны-плагины, Bedrock-аддоны
- **Bedrock Edition**: поведенческие и ресурсные пакеты, Script API, меню,
  JSON UI, команды, площадки
- **Серверы Bedrock**: Geyser, Floodgate, Nukkit, PocketMine, Dragonfly

## Структура

- [`COMPATIBILITY.md`](COMPATIBILITY.md) — матрица «версия Minecraft ↔ ядро ↔ Gradle ↔ JDK ↔ маппинги»
- [`knowledge/knowledge-map.md`](knowledge/knowledge-map.md) — **начни отсюда**: что где лежит и как выбрать
- [`versions.json`](versions.json) — машиночитаемый реестр версий (обновляется автоматически)
- `docs/` — справочники по конкретным темам (официальные источники):
  - `docs/java/versions.md` — актуальные версии Minecraft и загрузчиков
  - `docs/java/loaders.md` — обзор загрузчиков: кто есть кто и что поддерживает
  - `docs/java/toolchain.md` — Gradle, JDK, плагины сборки и грабли
  - `docs/java/mappings.md` — Mojang mappings vs Yarn vs Parchment
  - `docs/java/migration-26x.md` — **перенос мода с 1.21.x на 26.x**
  - `docs/java/unsupported.md` — **что не собирается и почему** (Quilt на 26.x, пустой jar, обходы)
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
- `releases/` — готовые аддоны Bedrock (`.mcaddon`) для проверки

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
  а не по памяти. В репозитории версии **обновляются автоматически**:
  `scripts/refresh_versions.py` → `versions.json` (CI: ежедневно).

## Проверено реальной сборкой

Эти комбинации не «документация по слухам», а результат настоящей сборки:

- **Java-мод, Fabric 26.3** — официальный шаблон `FabricMC/fabric-example-mod`
  (ветка `26.3`): JDK 25, Loom 1.18-SNAPSHOT, Gradle 9.x, Loader 0.19.5,
  Fabric API 0.163.0+26.3 → `modid-1.0.0.jar`.
- **Java-мод, NeoForge 26.3** — собрано `mysticmod-1.0.0.jar`: JDK 25,
  Gradle 9.2.1, ModDevGradle 2.0.148, `neo_version=26.3.0.95`.
  Шаблон — официальный `github.com/NeoForgeMDKs/MDK-26.3-ModDevGradle`.
- **Java-мод, Forge 26.3** — `26.3-66.0.13`, ForgeGradle 6.0.54, **Gradle 8.x**, JDK 21.
- **Java-мод, Fabric 1.21** — собран `modid-1.0.0.jar` на MC 1.21 (Loom 1.18.4,
  Gradle 9.7.1). Важно: Loom 1.18.x требует **JDK 25**, не 21.
- **Плагин, Paper 26.3** — собран `exampleplugin-1.0.0.jar`
  (`paper-api 26.3.build.207-stable`, Maven 3.9.9, JDK 25).
- **Мод, Quilt 1.20.6** — собран `example_mod-1.0.0+1.20.6.jar` (Quilt Loom
  1.7.4, Gradle 8.9, JDK 21). Важно: Quilt требует полного набора библиотек
  (quilt-mappings + loader + QSL + quilted-fabric-api), иначе `remapJar`
  выдаёт **пустой** jar без классов.
- **Аддон Bedrock** — `mystic_amulet.mcaddon` (предмет) и
  `mystic_creatures.mcaddon` (сущность + блок + скрипт): валидны по
  чек-листу `docs/bedrock/validation.md`.

Разбор всех неподдерживаемых случаев — в [`docs/java/unsupported.md`](docs/java/unsupported.md).

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

## Зеркала официальной документации (в этом аккаунте)

Полные копии официальных доков, синхронизируются автоматически
(GitHub Actions, ежедневно):

| Документация | Зеркало | Источник |
|---|---|---|
| Fabric | [`ssr33242/fabric-docs`](https://github.com/ssr33242/fabric-docs) | [FabricMC/fabric-docs](https://github.com/FabricMC/fabric-docs) |
| NeoForge | [`ssr33242/neoforge-docs`](https://github.com/ssr33242/neoforge-docs) | [neoforged/Documentation](https://github.com/neoforged/Documentation) |
| Forge | [`ssr33242/forge-docs`](https://github.com/ssr33242/forge-docs) | [MinecraftForge/Documentation](https://github.com/MinecraftForge/Documentation) |

В зеркале Fabric есть гайд по портированию (`develop/porting/`), в зеркале
NeoForge — миграционные primers.

## Лицензия

MIT — см. [`LICENSE`](LICENSE). Документация и шаблоны свободны для
использования и изменения.
