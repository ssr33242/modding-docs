# Forge — пошагово от пустой папки до `.jar`

Forge — старейшее ядро моддинга Minecraft. Использует **ForgeGradle** и манифест
`META-INF/mods.toml`. Ниже — рабочий процесс для двух актуальных веток.

## Живые версии (проверено по maven)

- **Forge 1.21.1** — `1.21.1-52.1.20` (ветка 52.x)
- **Forge 1.21.8** — `1.21.8-58.1.26` (ветка 58.x)
- **Forge 1.21.11** — `1.21.11-61.2.4` (ветка 61.x)
- **Forge 1.20.1** — `1.20.1-47.4.28` (ветка 47.x, самая популярная для модов)
- **Forge 1.12.2** — `1.12.2-14.23.5.2864` (легаси, ForgeGradle 2.3)
- Актуализировать: `https://maven.minecraftforge.net/net/minecraftforge/forge/maven-metadata.xml`

## Соответствие «версия Forge ↔ ForgeGradle ↔ Gradle ↔ JDK»

- **Forge 1.21.x (52–61.x)** → ForgeGradle **6.x** → Gradle **8.x** → JDK **21**
- **Forge 1.20.1 (47.x)** → ForgeGradle **6.x** → Gradle **8.x** → JDK **17**
- **Forge 1.19.x–1.20.x (41–46.x)** → ForgeGradle **5.x/6.x** → Gradle **7.6–8.x** → JDK **17**
- **Forge 1.16.5–1.18.2 (36–40.x)** → ForgeGradle **5.x** → Gradle **7.x** → JDK **8/16/17**
- **Forge 1.12.2 (14.23.5.286x)** → ForgeGradle **2.3** → Gradle **4.10.3** → JDK **8**

## Структура проекта (Forge 1.20.1+)

1. `settings.gradle` — подключение плагина ForgeGradle:
   - `pluginManagement { repositories { maven { url = 'https://maven.minecraftforge.net/' } ; gradlePluginPortal() } }`
2. `build.gradle` — плагин `net.minecraftforge.gradle` версии `[6.0,6.2)`.
3. `gradle.properties` — `minecraft_version`, `forge_version`, `mapping_channel`, `mapping_version`.
4. `src/main/java/<пакет>/<Класс>.java` — главный класс с аннотацией `@Mod("mod_id")`.
5. `src/main/resources/META-INF/mods.toml` — манифест мода.
6. `src/main/resources/META-INF/pack.mcmeta` — метаданные ресурспака.
7. `src/main/resources/assets/<mod_id>/` — текстуры, модели, языки.
8. `src/main/resources/data/<mod_id>/` — рецепты, теги, лут-таблицы.

## Ключевые поля `mods.toml`

- `modLoader = "javafml"` — для Java-модов.
- `loaderVersion = "[47,)"` — диапазон версий Forge (для 1.20.1 — ветка 47).
- `license` — лицензия мода.
- `[[mods]]` — блок с `modId`, `version`, `displayName`, `description`.
- `[[dependencies.<mod_id>]]` — зависимости: `forge`, `minecraft` с `versionRange`
  и `mandatory = true`.

## Главный класс (Forge 1.20.1)

- Аннотация `@Mod("mod_id")` на классе.
- Конструктор принимает `FMLJavaModLoadingContext` (1.20.1) — в новых версиях
  принимает `IEventBus` и `ModContainer`.
- Регистрация через `DeferredRegister.create(...)` для блоков, предметов, сущностей.
- `@SubscribeEvent` для обработчиков событий на нужной шине.

## Сборка

1. Запусти `gradlew build` (или `gradlew.bat build` на Windows).
2. Первая сборка скачивает Minecraft, mappings и декомпилирует — это долго
   (5–20 минут) и требует интернета.
3. Результат — `build/libs/<mod_id>-<версия>.jar`.
4. Для запуска в dev-режиме — `gradlew runClient`.

## Частые ошибки

- **`Could not find net.minecraftforge:forge:<версия>`** — неверный `forge_version`
  в `gradle.properties` или неподключён репозиторий `maven.minecraftforge.net`.
- **`Unsupported class file major version`** — JDK не тот. Для 1.20.1 нужен JDK 17,
  для 1.21.x — JDK 21. Проверь `JAVA_HOME`.
- **ForgeGradle требует Gradle 8.x** — на Gradle 9 сборка падает с ошибкой
  несовместимости. Откатись на 8.10.2 или 8.12.
- **Мод не грузится, «Missing or unsupported mods.toml»** — файл должен лежать
  строго в `META-INF/mods.toml` внутри jar.
- **Класс не найден при загрузке** — `modId` в `@Mod` и в `mods.toml` не совпадают.
- **Долгая первая сборка** — это нормально (декомпиляция). Не прерывай.
- **`mapping_channel`/`mapping_version`** — для 1.20.1 используется `official`
  с версией вида `1.20.1`. Для старых версий может быть `snapshot` + `20210309-1.16.5`.

## Проверка результата

Готовый `.jar` — это zip. Внутри должны быть:

- скомпилированные `.class` файлы;
- `META-INF/mods.toml`;
- `META-INF/pack.mcmeta`;
- папки `assets/<mod_id>/` и `data/<mod_id>/`.

Проверить можно любым архиватором или командой `jar tf <файл>.jar`.
