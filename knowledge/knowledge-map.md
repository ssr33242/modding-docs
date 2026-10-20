# Карта знаний по моддингу Minecraft

Этот файл — точка входа для быстрого понимания, **где что искать**. Пользуйся им
перед тем, как читать длинные гайды.

## Как выбрать ядро

- **Нужна максимальная совместимость с новыми версиями и снапшотами** → Fabric.
- **Хочется современный Forge-подобный API (1.20.2+)** → NeoForge.
- **Мод для старой популярной сборки (1.12.2, 1.20.1)** → Forge.
- **Fabric, но с собственными стандартами, либо запуск Fabric-модов** → Quilt.

## Где что лежит

- Матрица версий и требований → `COMPATIBILITY.md`
- Машиночитаемые версии → `versions.json`
- Гайды (пошагово) → `guides/`
  - `guides/from-zero-to-jar.md` — Fabric и NeoForge
  - `guides/forge-from-zero-to-jar.md` — Forge
  - `guides/quilt-from-zero-to-jar.md` — Quilt
  - `guides/toolchain-setup.md` — JDK, Gradle, кэш
- Шаблоны проектов → `templates/<ядро>/`
  - `templates/fabric/`, `templates/neoforge/`, `templates/forge/`, `templates/quilt/`

## Чем ядра отличаются друг от друга

- **Имя плагина сборки**: Fabric → `fabric-loom`; Quilt → `org.quiltmc.loom`;
  NeoForge → `net.neoforged.moddev`; Forge → `net.minecraftforge.gradle`.
- **Файл манифеста**: Fabric → `fabric.mod.json`; Quilt → `quilt.mod.json`;
  NeoForge → `META-INF/neoforge.mods.toml`; Forge → `META-INF/mods.toml`.
- **Точка входа**: Fabric/Quilt → интерфейс `ModInitializer` (`onInitialize`);
  NeoForge/Forge → класс с аннотацией `@Mod("mod_id")` и конструктором.
- **Регистрация контента**: Fabric/Quilt → `Registry.register(...)`;
  NeoForge/Forge → `DeferredRegister.create(...)`.
- **Ресурсы**: у всех одинаковая схема — `assets/<mod_id>/` (текстуры, модели,
  языки) и `data/<mod_id>/` (рецепты, теги, лут).

## Минимальный чек-лист «мод собирается и запускается»

1. Манифест лежит по правильному пути и его `id`/`modId` совпадает с `MOD_ID`.
2. Точка входа в манифесте указывает на **существующий** класс с точным пакетом.
3. Версия Gradle соответствует плагину сборки (см. `COMPATIBILITY.md`).
4. `JAVA_HOME` указывает на JDK, нужный именно этому ядру.
5. Для блоков/предметов созданы и модель, и текстура, и языковые записи.
6. После сборки проверить содержимое jar (манифест + `.class` + `assets/`).

## Типовые грабли (проверено на практике)

- Сборка проходит, а мод падает при загрузке → рассинхрон `entrypoint`/`@Mod`
  и реального имени класса.
- Имя `.jar` не совпадает с ожидаемым → `archivesBaseName` / `archives_base_name`
  в `gradle.properties` не переименован вместе с модом.
- Forge не собирается на Gradle 9 → нужен Gradle 8.x.
- Fabric Loom 1.19.x не собирается на Gradle 8 → нужен Gradle ≥ 9.8.0.
- Копирование шаблона ломается на Windows → исключать `.gradle`, `build`, `.tools`.
