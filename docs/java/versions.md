# Версии Minecraft и загрузчиков (актуально на 21 октября 2026)

> **Важно:** нумерация Minecraft: Java Edition изменилась. После `1.21.11`
> Mojang перешла на новую схему: `26.1`, `26.2`, `26.3` и так далее (год +
> номер релиза в году). Всё, что раньше было «1.21.x», теперь продолжается
> как «26.x». Если в гайде написано `1.21.1`, это уже **не** самая свежая
> версия.
>
> **Вторая новость 26.x:** Minecraft больше **не обфусцируется**
> ([Removing Obfuscation in Java Edition](https://www.minecraft.net/en-us/article/removing-obfuscation-in-java-edition)),
> поэтому Fabric прекратил вести Yarn — под 26.x используются **официальные
> маппинги Mojang**. Подробности: [`mappings.md`](mappings.md),
> [`migration-26x.md`](migration-26x.md).

## Где брать данные (официальные источники)

| Что | Адрес |
|---|---|
| Minecraft | `https://piston-meta.mojang.com/mc/game/version_manifest_v2.json` |
| Forge | `https://maven.minecraftforge.net/net/minecraftforge/forge/maven-metadata.xml` |
| ForgeGradle | `https://maven.minecraftforge.net/net/minecraftforge/gradle/ForgeGradle/maven-metadata.xml` |
| NeoForge | `https://maven.neoforged.net/releases/net/neoforged/neoforge/maven-metadata.xml` |
| ModDevGradle | `https://maven.neoforged.net/releases/net/neoforged/moddev-gradle/maven-metadata.xml` |
| Fabric Loader | `https://meta.fabricmc.net/v2/versions/loader` |
| Fabric — версии игры | `https://meta.fabricmc.net/v2/versions/game` |
| Yarn | `https://meta.fabricmc.net/v2/versions/yarn` |
| Fabric API | `https://api.modrinth.com/v2/project/fabric-api/version` |
| Fabric Loom | `https://maven.fabricmc.net/net/fabricmc/fabric-loom/maven-metadata.xml` |
| Quilt Loader | `https://meta.quiltmc.org/v3/versions/loader` |
| Paper | `https://fill.papermc.io/v3/projects/paper` |
| Architectury | `https://api.modrinth.com/v2/project/architectury-api/version` |
| Bedrock | `https://github.com/Mojang/bedrock-samples` (файл `version.json`) |

## Актуальные версии Java Edition

- **Последний релиз:** `26.3`
- **Последний снапшот:** `26.4-snapshot-5`

Релизы по порядку (от новых к старым):

1. `26.3`
2. `26.2`
3. `26.1.2`, `26.1.1`, `26.1`
4. `1.21.11`, `1.21.10`, `1.21.9`, `1.21.8`, `1.21.7`, `1.21.6`, `1.21.5`,
   `1.21.4`, `1.21.3`, `1.21.2`, `1.21.1`, `1.21`

## Сводка по поддержке 26.x (проверено 2026-10-21)

| Ядро | Поддержка 26.x | Версия под 26.3 | Последняя поддерживаемая без 26.x |
|---|---|---|---|
| NeoForge | ✅ да | `26.3.0.95` | — |
| Forge | ✅ да | `26.3-66.0.13` | — |
| Fabric | ✅ да (на mojmap) | API `0.163.0+26.3`, Loader `0.19.5` | — |
| Paper | ✅ да | `26.3` | — |
| Architectury | ✅ да | `22.0.5+fabric` / `+neoforge` | — |
| Quilt | ❌ нет | — | `1.20.6` (маппинги Quilt кончились на `1.21.11`) |

> Quilt-загрузчик **версии 26.3 существует** (`0.30.1`), и meta-сервис отдаёт `26.3`,
> но **маппингов Quilt под 26.x нет** → сборка невозможна. Поддержку определяют
> маппинги, а не список версий ядра. См. [`unsupported.md`](unsupported.md).

## Версии загрузчиков для 26.x

- **Forge:** `26.3-66.0.13` (Minecraft `26.3`), `26.2-65.1.5`, `26.1.2-64.1.5`
  → документация в ветке **FG/6.x**
- **NeoForge:** `26.3.0.95` (Minecraft `26.3`), `26.1.2.122`
- **Fabric:** Loader `0.19.5` (в шаблонах; последний в meta — `0.20.1`),
  API `0.163.0+26.3` (в официальном шаблоне; на Modrinth — `0.164.0+26.3`,
  `0.164.1+26.4`), Loom `1.18-SNAPSHOT` (последний релиз — `1.19.2`)
- **Quilt:** Loader `0.30.1` (и `0.31.0-beta.4`) — **без маппингов под 26.x**
- **Paper:** `26.3` (сборки 20x, канал STABLE)
- **Architectury API:** `22.0.5+fabric` / `22.0.5+neoforge`

Проверенные сборки (реально собраны, не «по слухам»):

- **Fabric 26.3** — JDK 25, Loom 1.18-SNAPSHOT, Gradle 9.x, loader 0.19.5,
  API 0.163.0+26.3. Шаблон: `FabricMC/fabric-example-mod`, ветка `26.3`.
- **NeoForge 26.3** — JDK 25, Gradle 9.2.1, ModDevGradle 2.0.148,
  `neo_version=26.3.0.95`. Шаблон: `NeoForgeMDKs/MDK-26.3-ModDevGradle`.
- **Forge 26.3** — JDK 21, Gradle **8.x**, ForgeGradle 6.0.54.
- **Fabric 1.21** — JDK 25, Loom 1.18.4, Gradle 9.7.1, loader 0.19.5.
  Важно: Loom 1.18.x **требует JDK 25**.
- **Forge 1.20.1** — JDK 17, Gradle 8.8, Forge 47.4.28.
- **Paper 26.3** — `paper-api 26.3.build.207-stable`, Maven 3.9.9, JDK 25.

Разные ядра догоняют Minecraft с разной задержкой: проверяйте поддержку
версии **для каждого ядра отдельно**, а не «в целом для Minecraft».

## Версии загрузчиков для 1.21.x (для старых сборок)

- **Forge:** `1.21.11-61.2.4`, `1.21.8-58.1.26`, `1.21.4-54.1.22`,
  `1.21.1-52.1.20`
- **NeoForge:** `21.4.77-beta` (для `1.21.4`), `21.1.264` (для `1.21.1`)
- **Fabric:** Loader `0.20.1`, Loom `1.19.2`, Yarn — последняя сборка
  `1.21.11+build.6` (всего 3412 билдов в истории)

## Как сопоставить версию загрузчика и Minecraft

- У **Forge** номер сборки составлен из версии игры и версии самого Forge:
  `26.3-66.0.13` — первая часть (`26.3`) это Minecraft, вторая (`66.0.13`)
  это Forge.
- У **NeoForge** версия начинается с версии Minecraft: `26.3.0.95` — для
  Minecraft `26.3`; `21.4.x` — для `1.21.4`.
- У **Fabric** загрузчик и API независимы: сначала ставится версия самой
  игры, потом loader, потом Fabric API.
- У **Paper** версия совпадает с версией Minecraft: `26.3`.

## Что писать в конфигах сборки

Gradle для Fabric (`gradle.properties`), Minecraft `26.3` — как в официальном шаблоне:

```properties
minecraft_version=26.3
loader_version=0.19.5
loom_version=1.18-SNAPSHOT
fabric_api_version=0.163.0+26.3
```

Gradle для NeoForge (`gradle.properties`), Minecraft `26.3`:

```properties
minecraft_version=26.3
minecraft_version_range=[26.3]
neo_version=26.3.0.95
```

Gradle для Forge (`gradle.properties`), Minecraft `26.3`:

```properties
minecraft_version=26.3
forge_version=26.3-66.0.13
```

Требования: Loom 1.18+ требует **JDK 25** и Gradle 9.x;
ForgeGradle 6.x требует **Gradle 8.x** и JDK 21.

Bedrock — версия аддона берётся из манифеста и указывается в
`min_engine_version` (это версия формата, а не игры):

```json
{
  "format_version": 2,
  "header": {
    "min_engine_version": [1, 26, 50]
  }
}
```

## Правила работы с версиями

- **Нельзя доверять памяти модели**: версии меняются постоянно, их нужно
  проверять в живых источниках (список выше). В этом репозитории версии
  обновляются автоматически: `scripts/refresh_versions.py` → `versions.json`.
- Прежде чем писать код под версию, уточните у пользователя, какая у него
  версия Minecraft и загрузчика — API между версиями ломается.
- Между крупными версиями (например, `1.21` и `26.3`) меняются имена
  методов, пакеты и рейстры. Код, написанный под `1.21.1`, **не соберётся**
  под `26.3` без правок — и не только из-за имён: с 26.1 поменялись маппинги.
- Для Bedrock версия аддона — это `min_engine_version` в манифесте, и она
  отдельная от версии скриптового API (`@minecraft/server`).

## Связанные документы

[`loaders.md`](loaders.md) — обзор загрузчиков ·
[`toolchain.md`](toolchain.md) — Gradle/JDK/плагины ·
[`mappings.md`](mappings.md) — маппинги ·
[`migration-26x.md`](migration-26x.md) — портирование ·
[`unsupported.md`](unsupported.md) — что не собирается ·
[`../COMPATIBILITY.md`](../../COMPATIBILITY.md) — матрица совместимости
