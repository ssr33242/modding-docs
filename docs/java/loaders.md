# Загрузчики модов: кто есть кто

> Проверено 2026-10-21. Minecraft Java Edition: релиз **26.3**, снапшот
> **26.4-snapshot-5**.

## Сводная таблица

| Загрузчик | Что это | MC 26.x | Плагин сборки | Лицензия/доступ |
|---|---|---|---|---|
| **Fabric** | лёгкий, быстрые обновления, огромная экосистема | ✅ 0.163.0+26.3 | Fabric Loom | MIT (Fabric API), открытый |
| **NeoForge** | форк Forge под новые версии, ModDevGradle | ✅ 26.3.0.95 | ModDevGradle 2.0.148 | LGPL/свободный |
| **Forge** | классический загрузчик от MinecraftForge | ✅ 26.3-66.0.13 | ForgeGradle 6.0.54 | LGPL |
| **Quilt** | форк Fabric, своя экосистема и QSL | ⚠️ загрузчик есть, маппингов нет | Quilt Loom | открытый |
| **Architectury** | мод-мост между Fabric и NeoForge | ✅ 22.0.5 | — | открытый |
| **Paper** | серверная платформа (Bukkit-совместимая) | ✅ 26.3 | Maven/Gradle | GPL (сервер) |

Для серверов: Paper, Purpur, Folia, Velocity — плагины, не моды.

## Fabric

- **Официальные шаблоны:** <https://github.com/FabricMC/fabric-example-mod>
  (ветки `26.3`, `26.2`, `26.1.2`, `26.1.1`, `26.1`, `1.21.11`, …).
- **Документация (зеркало):** [`ssr33242/fabric-docs`](https://github.com/ssr33242/fabric-docs)
  ← [FabricMC/fabric-docs](https://github.com/FabricMC/fabric-docs).
- **Разработка:** <https://fabricmc.net/develop>
- **Живые версии:** Loader `0.20.1` (в шаблонах 26.3 — `0.19.5`), API `0.164.1+26.4`,
  Loom `1.19.2`.
- **Особенность 26.x:** Minecraft больше не обфусцирован, Yarn не выпускается —
  переход на официальные маппинги. См. [`migration-26x.md`](migration-26x.md).

## NeoForge

- **MDK-шаблоны:** <https://github.com/NeoForgeMDKs> (для 26.3 —
  `MDK-26.3-ModDevGradle`).
- **Документация (зеркало):** [`ssr33242/neoforge-docs`](https://github.com/ssr33242/neoforge-docs)
  ← [neoforged/Documentation](https://github.com/neoforged/Documentation).
  В зеркале есть `docs/` (актуальная версия) и `versioned_docs/version-1.21.x` (старые).
- **Миграционные гайды (primers):** <https://docs.neoforged.net/primer/docs/>
  — готовые списки изменений между версиями, очень полезно при портировании.
- **Живые версии:** `26.3.0.95`, ModDevGradle `2.0.148`.

## Forge

- **Документация (зеркало):** [`ssr33242/forge-docs`](https://github.com/ssr33242/forge-docs)
  ← [MinecraftForge/Documentation](https://github.com/MinecraftForge/Documentation).
- **Ветки в зеркале:** `1.12.x` … `1.21.x` плюс **`FG/5.x`** и **`FG/6.x`** —
  последние соответствуют современным поколениям Forge (в т.ч. 26.x).
- **Живые версии:** `26.3-66.0.13`, ForgeGradle `6.0.54`.
- ⚠️ ForgeGradle 6.x **не работает на Gradle 9** — только Gradle 8.x.

## Quilt

- **Шаблон:** <https://github.com/QuiltMC/quilt-template-mod> (ветки 1.18.2 … 1.21, 1.20.6).
- **Мета-API:** <https://meta.quiltmc.org/v3/versions/loader>
- **Живые версии:** Loader `0.30.1` (и `0.31.0-beta.4`).
- ⚠️ Под 26.x **нет маппингов** — сборка невозможна, подробности в
  [`unsupported.md`](unsupported.md).

## Architectury

- **Мод:** <https://modrinth.com/mod/architectury-api> — версии идут парами:
  `22.0.5+fabric` и `22.0.5+neoforge` под один и тот же MC.
- Позволяет писать общий код мода и для Fabric-, и для NeoForge-сборки.

## Paper (серверные плагины)

- **API:** <https://fill.papermc.io/v3/projects/paper> (версии: 26.3, 26.2, 26.1.2, 1.21.11 …).
- **Репозиторий артефактов:** <https://repo.papermc.io/repository/maven-public/>
- **Документация:** <https://docs.papermc.io>
- Плагин обязан указывать `api-version` в `plugin.yml` (например `26.3`).

## Полезные моды под текущие версии (проверено на Modrinth)

| Мод | Версия под 26.3 |
|---|---|
| Architectury API | 22.0.5+fabric / +neoforge |
| ModMenu | 21.0.0 (26.4-snapshot-3 — 22.0.0-alpha.2) |
| Fabric API | 0.164.0+26.3 |

## Связанные документы

[`versions.md`](versions.md) — все версии Minecraft ·
[`toolchain.md`](toolchain.md) — Gradle/JDK/плагины ·
[`mappings.md`](mappings.md) — маппинги ·
[`migration-26x.md`](migration-26x.md) — портирование ·
[`unsupported.md`](unsupported.md) — что не собирается
