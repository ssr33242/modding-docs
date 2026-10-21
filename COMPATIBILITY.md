# Матрица совместимости

> **Проверено: 2026-10-21.** Все «живые версии» внизу сняты с официальных API
> в тот день. Строки с пометкой «проверено сборкой» реально собраны на машине:
> `BUILD SUCCESSFUL` **и** в jar есть `.class`-файлы.

## Коротко: что на что работает сейчас

| Minecraft | Fabric | NeoForge | Forge | Quilt | Paper (плагины) |
|---|---|---|---|---|---|
| **26.3** | ✅ 0.163.0+26.3, Loom 1.18-SNAPSHOT, JDK 25 | ✅ 26.3.0.95, MDG 2.0.148 | ✅ 26.3-66.0.13, FG 6.0.54, JDK 21 | ⚠️ загрузчик есть, маппингов нет | ✅ paper-api 26.3 |
| 26.2 / 26.1.x | ✅ Fabric API есть | ✅ | ✅ | ⚠️ | ✅ |
| 1.21.11 | ✅ | ✅ | ✅ 52.x-61.x | ⚠️ | ✅ |
| 1.21.1 | ✅ Loom 1.19.1, Yarn 1.21.1+build.3 | ✅ 21.1.264 | ✅ 52.1.20 | ⚠️ | ✅ |
| 1.20.6 | ✅ | ✅ | ✅ 50.2.14 | ✅ (единственная полная сборка) | ✅ |
| 1.20.1 | ✅ | ✅ | ✅ 47.4.28 | ✅ | ✅ |
| 1.12.2 | — | — | ✅ 14.23.5.2864, FG 2.3, JDK 8 | — | — |

⚠️ = загрузчик поддерживает версию, но **нет маппингов/библиотек** — сборка падает.
Подробности и обходные пути — в [`docs/java/unsupported.md`](docs/java/unsupported.md).

## Проверенные комбинации (собраны на машине)

| Ядро | MC | JDK | Сборщик | Артефакт |
|---|---|---|---|---|
| Fabric | 26.3 | 25 | Loom 1.18-SNAPSHOT, Gradle 9.x, Loader 0.19.5, Fabric API 0.163.0+26.3 | `modid-1.0.0.jar` (официальный шаблон) |
| NeoForge | 26.3 | 25 | Gradle 9.2.1 + ModDevGradle 2.0.148, NeoForge 26.3.0.95 | `mysticmod-1.0.0.jar` |
| Forge | 26.3 | 21 | Gradle 8.x + ForgeGradle 6.0.54, Forge 26.3-66.0.13 | по шаблону MDK/FG |
| Paper (плагин) | 26.3 | 25 | Maven 3.9.9, paper-api 26.3 | `exampleplugin-1.0.0.jar` |
| Fabric | 1.21.1 | 25 | Gradle 9.8.0 + Loom 1.19.1, Loader 0.16.9, Fabric API 0.116.17+1.21.1, Yarn 1.21.1+build.3 | `examplemod-1.0.0.jar` |
| NeoForge | 1.21.1 | 21 | Gradle 9.8.0 + ModDevGradle 2.0.148, NeoForge 21.1.264 | `examplenm-1.0.0.jar` |
| Fabric | 1.21 | 25 | Gradle 9.7.1 + Loom 1.18.4, Loader 0.19.5, Fabric API 0.102.0+1.21 | `modid-1.0.0.jar` |
| Forge | 1.20.1 | 17 | Gradle 8.8 + Forge 47.4.28 | `examplemod-1.0.0.jar` |
| Quilt | 1.20.6 | 21 | Quilt Loom 1.7.4 + Gradle 8.9, Loader 0.26.3 | `example_mod-1.0.0+1.20.6.jar` |

## Правила toolchain

| Загрузчик | Плагин сборки | Gradle | JDK | Маппинги |
|---|---|---|---|---|
| Fabric 26.x | Loom 1.18-SNAPSHOT / 1.19.2 | 9.x | **25** | mojang (Yarn под 26.x нет) |
| Fabric 1.21.x | Loom 1.18.x / 1.19.x | ≥ 9.8.0 | ≥ 25 | yarn или mojang |
| NeoForge 26.x | ModDevGradle 2.0.148 | 8.8+ / 9.x | 21 / 25 | mojang |
| NeoForge 1.21.x | ModDevGradle 2.x | 8.8+ / 9.x | 21 | mojang |
| Forge 26.x | ForgeGradle 6.0.54 | **8.x** | 21 | mojang |
| Forge 1.21.x (52–61.x) | ForgeGradle 6.x | 8.x | 21 | mojang |
| Forge 1.20.1 (47.x) | ForgeGradle 6.x | 8.x | 17 | mojang |
| Forge 1.19.x–1.20.x (41–46.x) | ForgeGradle 5.x/6.x | 7.6–8.x | 17 | mojang |
| Forge 1.16.5–1.18.2 (36–40.x) | ForgeGradle 5.x | 7.x | 8/16/17 | mojang |
| Forge 1.12.2 (14.23.5.2864) | ForgeGradle 2.3 | 4.10.3 | 8 | mojang |
| Quilt 1.20.6 | Quilt Loom 1.7.4 | 8.9 | 21 | quilt (mojang) |

### Важные предупреждения

- **ForgeGradle 6.x не работает на Gradle 9** — сборка падает. Для Forge нужен Gradle 8.x.
- **Fabric/Quilt Loom 1.19.x не работает на Gradle 8.x** — нужен Gradle ≥ 9.8.0.
  Поэтому для Fabric и Forge держим **разные** версии Gradle (9.x и 8.12).
- **Loom 1.18.x/1.19.x требует JDK 25** (не 21) — на JDK 21 сборка падает на старте Loom.
- **Yarn остановился на 1.21.11** — для 26.x используйте официальные маппинги Mojang.

## Живые версии (снято с API 2026-10-21)

| Что | Версия |
|---|---|
| Minecraft (релиз) | **26.3** |
| Minecraft (снапшот) | 26.4-snapshot-5 |
| Fabric Loader | 0.20.1 (в шаблонах 26.3 — 0.19.5) |
| Fabric API | 0.164.1+26.4 · для 26.3 — 0.164.0+26.3 (в официальном шаблоне 0.163.0+26.3) |
| Fabric Loom | 1.19.2 |
| Yarn (последняя сборка) | 1.21.11+build.6 |
| NeoForge | 26.3.0.95 |
| ModDevGradle | 2.0.148 |
| Forge | 26.3-66.0.13 |
| ForgeGradle | 6.0.54 |
| Quilt Loader | 0.30.1 (0.31.0-beta.4) |
| Architectury API | 22.0.5+fabric / 22.0.5+neoforge |
| Paper | 26.3 |
| ModMenu | 21.0.0 (26.3) · 22.0.0-alpha.2 (26.4-snapshot-3) |

Машиночитаемая копия — [`versions.json`](versions.json);
автообновление — `scripts/refresh_versions.py`.

## Где брать актуальные версии

| Что | Адрес |
|---|---|
| Minecraft | <https://piston-meta.mojang.com/mc/game/version_manifest_v2.json> |
| Fabric Loader | <https://meta.fabricmc.net/v2/versions/loader> |
| Fabric — версии игры | <https://meta.fabricmc.net/v2/versions/game> |
| Yarn | <https://meta.fabricmc.net/v2/versions/yarn> |
| Fabric API | <https://api.modrinth.com/v2/project/fabric-api/version> |
| Fabric Loom | <https://maven.fabricmc.net/net/fabricmc/fabric-loom/maven-metadata.xml> |
| NeoForge | <https://maven.neoforged.net/releases/net/neoforged/neoforge/maven-metadata.xml> |
| ModDevGradle | <https://maven.neoforged.net/releases/net/neoforged/moddev-gradle/maven-metadata.xml> |
| Forge | <https://maven.minecraftforge.net/net/minecraftforge/forge/maven-metadata.xml> |
| ForgeGradle | <https://maven.minecraftforge.net/net/minecraftforge/gradle/ForgeGradle/maven-metadata.xml> |
| Quilt Loader | <https://meta.quiltmc.org/v3/versions/loader> |
| Paper | <https://fill.papermc.io/v3/projects/paper> |
| Architectury API | <https://api.modrinth.com/v2/project/architectury-api/version> |

## JDK на этой машине

- JDK 8 — отдельная установка (Forge 1.12.2)
- JDK 17 — `C:\Program Files\Eclipse Adoptium\jdk-17.0.20.101-hotspot`
- JDK 21 — `C:\Program Files\Eclipse Adoptium\jdk-21.0.11.10-hotspot`
- JDK 25 — `C:\Program Files\Eclipse Adoptium\jdk-25.0.2.10-hotspot`

## Gradle

- Локальные дистрибутивы: `C:\Users\satda\Desktop\Modding\.tools\gradle-<версия>`
- Установлены: 8.10.2, 8.12, 9.8.0

## Официальные шаблоны (готовая точка старта)

| Загрузчик | Шаблон |
|---|---|
| Fabric 26.3 | <https://github.com/FabricMC/fabric-example-mod/tree/26.3> |
| Fabric 26.2 / 26.1.2 / 26.1.1 / 26.1 | ветки `26.2`, `26.1.2`, `26.1.1`, `26.1` того же репозитория |
| Fabric 1.21.x | ветки `1.21.11`, `1.21.10`, `1.21.9`… |
| NeoForge 26.3 | <https://github.com/NeoForgeMDKs/MDK-26.3-ModDevGradle> |
| Quilt 1.20.6 / 1.21 | <https://github.com/QuiltMC/quilt-template-mod> |

## Локальные зеркала официальной документации

| Документация | Зеркало | Источник |
|---|---|---|
| Fabric | [`ssr33242/fabric-docs`](https://github.com/ssr33242/fabric-docs) | [FabricMC/fabric-docs](https://github.com/FabricMC/fabric-docs) |
| NeoForge | [`ssr33242/neoforge-docs`](https://github.com/ssr33242/neoforge-docs) | [neoforged/Documentation](https://github.com/neoforged/Documentation) |
| Forge | [`ssr33242/forge-docs`](https://github.com/ssr33242/forge-docs) | [MinecraftForge/Documentation](https://github.com/MinecraftForge/Documentation) |

Зеркала синхронизируются с оригиналом автоматически (GitHub Actions, ежедневно).
