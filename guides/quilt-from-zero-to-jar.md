# Quilt — пошагово от пустой папки до `.jar`

Quilt — форк Fabric, близкий к нему по API. Использует **Quilt Loom** (форк Fabric Loom)
и манифест `quilt.mod.json`. Многие Fabric-моды совместимы, но у Quilt свои
стандартные библиотеки (QSL/QFAPI).

## Живые версии (проверено по meta.quiltmc.org)

- **Quilt Loader (стабильные)** — `0.30.1`, `0.30.0`, `0.29.2`, `0.29.1`, `0.29.0`
- **Quilt Loader (бета)** — `0.31.0-beta.4` и новее
- **Актуальные версии игры** — до `26.3` включительно
- Актуализировать: `https://meta.quiltmc.org/v3/versions/loader`

## Библиотеки

- **QSL** (Quilt Standard Libraries) — основной набор API Quilt.
- **QFAPI** (Quilted Fabric API) — совместимость с Fabric API.
- Пакет называется `org.quiltmc:quilted-fabric-api` на Modrinth — проект `qsl`.
- Держится в основном на ветке `1.20.1` (`7.7.0+0.92.2-1.20.1`);
  для 1.21 — только альфы (`11.0.0-alpha.x`).
- Актуализировать: `https://api.modrinth.com/v2/project/qsl/version`

## Соответствие «версия ↔ Quilt Loom ↔ Gradle ↔ JDK»

- **Quilt Loom 1.9–1.10** → Gradle **8.11–8.12** → JDK **21**
- **Quilt Loom 1.19.x** → Gradle **≥ 9.8.0** → JDK **≥ 25** (как у Fabric Loom)
- Quilt Loom синхронизирован с версиями Fabric Loom, плагин называется `org.quiltmc.loom`.

## Структура проекта

1. `settings.gradle` — `pluginManagement` с `https://maven.quiltmc.org/repository/release`
   и `https://maven.fabricmc.net/`.
2. `build.gradle` — плагин `org.quiltmc.loom` версии `1.9-SNAPSHOT` или `1.10-SNAPSHOT`.
3. `gradle.properties` — `minecraft_version`, `quilt_loader_version`, `quilt_mappings`,
   `quilted_fabric_api_version`.
4. `src/main/java/<пакет>/<Класс>.java` — точка входа (`ModInitializer`).
5. `src/main/resources/quilt.mod.json` — манифест Quilt.
6. `src/main/resources/assets/<mod_id>/` — ресурсы (структура как в Fabric).

## Ключевые поля `quilt.mod.json`

- `schema_version` — `1`.
- `quilt_loader.id` — id мода (совпадает с `MOD_ID`).
- `quilt_loader.group` — группа/пакет.
- `quilt_loader.version` — версия мода.
- `quilt_loader.entrypoints.init` — список классов-инициализаторов.
- `quilt_loader.depends` — зависимости: `quilt_loader`, `minecraft`, `quilted_fabric_api`.
- `minecraft.environment` — `*` (обе стороны) или `client`/`dedicated_server`.

## Точка входа

- Интерфейс `org.quiltmc.loader.api.ModInitializer`.
- Метод `onInitialize(ModContainer mod)`.
- Регистрация — как в Fabric: `Registry.register(Registries.BLOCK, id, block)`.
- Если мод написан под Fabric и не использует Fabric-специфичных API, он обычно
  работает и на Quilt без изменений (`quilt.mod.json` можно сгенерировать).

## Сборка

1. `gradlew build` — результат в `build/libs/<mod_id>-<версия>.jar`.
2. `gradlew runClient` — запуск dev-клиента.
3. Манифест `quilt.mod.json` должен лежать в корне jar.

## Частые ошибки

- **Не подключён репозиторий Quilt** — `maven.quiltmc.org`, иначе плагин не найдётся.
- **`quilt.mod.json` не найден** — файл должен быть в корне `resources/`, не в подпапке.
- **`schema_version` обязателен** — без него манифест невалиден.
- **Конфликт QFAPI и Fabric API** — не подключай обе библиотеки одновременно.
- **Мод Fabric не запускается на Quilt** — проверь, не используются ли
  Fabric-специфичные entrypoints и API; для совместимости нужен QFAPI.
- **`entrypoints.init` пустой** — загрузчик не найдёт класс, мод не инициализируется.

## Проверка результата

Внутри jar должны быть:

- скомпилированные `.class`;
- `quilt.mod.json` в корне;
- `assets/<mod_id>/`.

Quilt Loader умеет ставить как Quilt-, так и Fabric-моды (через QFAPI).
