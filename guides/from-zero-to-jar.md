# От пустой папки до готового .jar

## Общий порядок

1. Определи версию Minecraft и ядро.
2. Возьми шаблон из `templates/<ядро>/`.
3. Скопируй его в рабочую папку.
4. Замени `MOD_ID`, название, пакет, версии на свои.
5. Подбери Gradle и JDK по `COMPATIBILITY.md`.
6. Запусти `gradle build`.
7. Забери `.jar` из `build/libs/`.

## Fabric — пошагово

1. Структура проекта:
   - `settings.gradle` — pluginManagement с `https://maven.fabricmc.net/`
   - `build.gradle` — плагин `fabric-loom`
   - `gradle.properties` — версии Minecraft, Yarn, Loader, Fabric API
   - `src/main/java/<пакет>/<Класс>.java` — точка входа (`ModInitializer`)
   - `src/main/resources/fabric.mod.json` — манифест мода
   - `src/main/resources/assets/<mod_id>/` — текстуры, модели, языки

2. Ключевые поля `fabric.mod.json`:
   - `id` — совпадает с `MOD_ID`
   - `entrypoints.main` — полное имя главного класса
   - `depends` — loader, minecraft, java, fabric-api

3. Сборка: `gradle build`, результат — `build/libs/<mod_id>-<версия>.jar`

## NeoForge — пошагово

1. Структура проекта:
   - `settings.gradle` — repository `https://maven.neoforged.net/releases`
   - `build.gradle` — плагин `net.neoforged.moddev`
   - `src/main/java/<пакет>/<Класс>.java` — класс с аннотацией `@Mod`
   - `src/main/resources/META-INF/neoforge.mods.toml` — манифест
   - `src/main/resources/assets/<mod_id>/`

2. Ключевые поля `neoforge.mods.toml`:
   - `modId` — совпадает с `MOD_ID`
   - `loaderVersion` — `[4,)` для NeoForge 1.21.x
   - `[[dependencies.<mod_id>]]` — neoforge и minecraft с versionRange

3. Сборка: `gradle build`, результат — `build/libs/<mod_id>-<версия>.jar`

## Частые ошибки

- **`requires at least Gradle X`** — версия плагина (Loom/ModDevGradle) новее, чем твой Gradle.
  Решение: поднять Gradle или взять более старый плагин.
- **`requires at least JVM runtime version X`** — плагину нужен более новый JDK.
  Решение: запускать сборку с `JAVA_HOME`, указывающим на нужный JDK.
- **`Could not resolve ... minecraft:1.21.1`** — неверный идентификатор версии.
- **Класс не найден в игре** — `entrypoints`/`modId` не совпадают с реальными именами.
- **Пустой язык/модели** — не хватает файлов в `assets/<mod_id>/`.

## Проверка результата

Готовый `.jar` — это zip. Внутри должны быть:
- скомпилированные `.class` файлы;
- `fabric.mod.json` (Fabric) или `META-INF/neoforge.mods.toml` (NeoForge);
- папка `assets/<mod_id>/`.
