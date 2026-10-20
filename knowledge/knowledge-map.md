# Карта знаний по моддингу Minecraft

Этот файл — точка входа для быстрого понимания, **где что искать**. Пользуйся им
перед тем, как читать длинные гайды.

## Сначала определи платформу

- **Minecraft Java Edition** → моды (Fabric, NeoForge, Forge, Quilt) и плагины
  (Bukkit, Spigot, Paper).
- **Minecraft Bedrock Edition** (мобильные, консоли, Windows Bedrock) → **аддоны**
  (behavior pack + resource pack + скрипты).

## Как выбрать Java-ядро

- **Максимальная совместимость с новыми версиями и снапшотами** → Fabric.
- **Современный Forge-подобный API (1.20.2+)** → NeoForge.
- **Мод для старой популярной сборки (1.12.2, 1.20.1)** → Forge.
- **Fabric, но с собственными стандартами, либо запуск Fabric-модов** → Quilt.

## Как выбрать между модом и плагином

- Новый блок/предмет/моб/измерение, изменение клиента → **мод**.
- Команды, права, регионы, экономика, чат, мини-игры на сервере → **плагин**.

## Где что лежит

- Матрица версий и требований → `COMPATIBILITY.md`
- Машиночитаемые версии → `versions.json`
- Гайды (пошагово) → `guides/`
  - `guides/from-zero-to-jar.md` — Fabric и NeoForge
  - `guides/forge-from-zero-to-jar.md` — Forge
  - `guides/quilt-from-zero-to-jar.md` — Quilt
  - `guides/plugins-from-zero-to-jar.md` — плагины Bukkit/Spigot/Paper
  - `guides/addons-overview.md` — что такое аддоны на всех платформах
  - `guides/bedrock-from-zero-to-addon.md` — аддоны Bedrock
  - `guides/bedrock-build.md` — сборка и упаковка аддона
  - `guides/bedrock-repos.md` — репозитории и площадки Bedrock
  - `guides/bedrock-servers.md` — Geyser, Floodgate, Nukkit, PocketMine
  - `guides/toolchain-setup.md` — JDK, Gradle, кэш
- Шаблоны проектов → `templates/<тип>/`
  - `templates/fabric/`, `templates/neoforge/`, `templates/forge/`, `templates/quilt/`
  - `templates/plugin/` — плагин Paper (Maven и Gradle)
  - `templates/addon-plugin/` — аддон-плагин (расширение другого плагина)
  - `templates/bedrock/` — аддон Bedrock (BP + RP + скрипт)

## Чем Java-ядра отличаются друг от друга

- **Имя плагина сборки**: Fabric → `fabric-loom`; Quilt → `org.quiltmc.loom`;
  NeoForge → `net.neoforged.moddev`; Forge → `net.minecraftforge.gradle`.
- **Файл манифеста**: Fabric → `fabric.mod.json`; Quilt → `quilt.mod.json`;
  NeoForge → `META-INF/neoforge.mods.toml`; Forge → `META-INF/mods.toml`.
- **Точка входа**: Fabric/Quilt → интерфейс `ModInitializer` (`onInitialize`);
  NeoForge/Forge → класс с аннотацией `@Mod("mod_id")` и конструктором.
- **Регистрация контента**: Fabric/Quilt → `Registry.register(...)`;
  NeoForge/Forge → `DeferredRegister.create(...)`.
- **Ресурсы**: у всех одинаковая схема — `assets/<mod_id>/` и `data/<mod_id>/`.

## Чем плагины отличаются

- **Манифест**: `plugin.yml` в корне ресурсов.
- **Обязательные поля**: `name`, `version`, `main`, **`api-version`** (обязателен!).
- **Главный класс**: наследует `JavaPlugin`.
- **Команда работает только при двух шагах**: объявлена в `plugin.yml` **и**
  зарегистрирована в `onEnable()` через `setExecutor`.
- **Зависимости**: `depend` (жёсткая) и `softdepend` (мягкая).
- **Репозиторий**: `https://repo.papermc.io/repository/maven-public/` (Paper).
- **JDK**: 1.21.x → 21; 1.19.4–1.20.4 → 17; 1.16.5 → 8/11/16; 1.12.2 → 8.

## Чем Bedrock-аддоны отличаются

- **Нет кода игры** — только данные (JSON) и опционально JavaScript.
- **Два пакета**: behavior pack (логика) + resource pack (графика/звук).
- **Манифест**: `manifest.json` в корне каждого пакета.
- **version и min_engine_version — массивы** `[1, 0, 0]`, не строки.
- **UUID должны быть разными**: header.uuid и каждый modules[].uuid.
- **Упаковка**: `.mcaddon` (оба пакета) или `.mcpack` (один пакет).
- **Структура .mcaddon**: в корне zip папки `behavior_packs/` и `resource_packs/`.
- **Скрипты** требуют включённых **Beta APIs** в мире.

## Минимальный чек-лист «собирается и запускается»

**Java-мод:**
1. Манифест по правильному пути, `id`/`modId` совпадает с `MOD_ID`.
2. Точка входа указывает на существующий класс с точным пакетом.
3. Версия Gradle соответствует плагину сборки (см. `COMPATIBILITY.md`).
4. `JAVA_HOME` указывает на нужный JDK.
5. Для блоков/предметов есть модель, текстура и языковые записи.

**Плагин:**
1. `plugin.yml` в корне, `main` точно совпадает с классом.
2. `api-version` указан под версию сервера.
3. Команды объявлены в `plugin.yml` и зарегистрированы в `onEnable()`.
4. `paper-api` подключён как `provided`/`compileOnly`.

**Bedrock-аддон:**
1. `manifest.json` валиден, UUID уникальны и различны.
2. `version`/`min_engine_version` — массивы.
3. Все идентификаторы (`example:ruby`) совпадают между BP и RP.
4. Для скриптов объявлен модуль и включены Beta APIs.

## Типовые грабли (проверено на практике)

- Сборка проходит, а мод падает при загрузке → рассинхрон `entrypoint`/`@Mod`
  и реального имени класса.
- Имя `.jar` не совпадает с ожидаемым → `archivesBaseName` не переименован.
- Forge не собирается на Gradle 9 → нужен Gradle 8.x.
- Fabric Loom 1.19.x не собирается на Gradle 8 → нужен Gradle ≥ 9.8.0.
- Плагин не грузится → пропущен `api-version` в `plugin.yml`.
- Команда плагина молчит → забыта регистрация `setExecutor` в `onEnable()`.
- Bedrock-пакет не импортируется → `version` записан строкой вместо массива.
- Bedrock-аддон не виден в игре → одинаковые UUID или неверная структура zip.
