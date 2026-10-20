# Матрица совместимости

Строки с пометкой «проверено сборкой» **реально собраны** на этой машине.
Остальные — соответствие версий ядер и инструментов (по официальным источникам).

## Проверенные комбинации

- **Fabric 1.21.1** — собирается в `.jar`
  - Gradle: 9.8.0
  - Fabric Loom: 1.19.1 (требует Gradle ≥ 9.8.0 и JDK ≥ 25)
  - JDK: 25
  - Yarn mappings: `1.21.1+build.3`
  - Fabric Loader: `0.16.9`
  - Fabric API: `0.116.17+1.21.1`
  - Результат: `examplemod-1.0.0.jar`

- **NeoForge 1.21.1** — собирается в `.jar`
  - Gradle: 9.8.0
  - ModDevGradle: 2.0.148
  - NeoForge: `21.1.264`
  - JDK: 21 (toolchain `JavaLanguageVersion.of(21)`)
  - Результат: `examplenm-1.0.0.jar`

## Правила зависимости версий

- Loom **1.19.x** → Gradle **≥ 9.8.0** → JDK **≥ 25** (при сборке самим Gradle)
- Loom **1.9–1.10** → Gradle **8.11–8.12** → JDK 21
- Quilt Loom **1.9–1.10** → Gradle **8.11–8.12** → JDK 21
- Quilt Loom **1.19.x** → Gradle **≥ 9.8.0** → JDK **≥ 25**
- NeoForge 21.1.x → ModDevGradle 2.x → Gradle 8.8+ / 9.x → JDK 21
- Forge 1.21.x (52–61.x) → ForgeGradle **6.x** → Gradle **8.x** → JDK **21**
- Forge 1.20.1 (47.x) → ForgeGradle 6.x → Gradle 8.x → JDK 17
- Forge 1.19.x–1.20.x (41–46.x) → ForgeGradle 5.x/6.x → Gradle 7.6–8.x → JDK 17
- Forge 1.16.5–1.18.2 (36–40.x) → ForgeGradle 5.x → Gradle 7.x → JDK 8/16/17
- Forge 1.12.2 (14.23.5.286x) → ForgeGradle 2.3 → Gradle 4.10.3 → JDK 8

## Важное предупреждение

- **ForgeGradle 6.x не работает на Gradle 9** — сборка падает. Для Forge нужен Gradle 8.x.
- **Fabric/Quilt Loom 1.19.x не работает на Gradle 8.x** — нужен Gradle ≥ 9.8.0.
  Поэтому для Fabric и Forge держим **разные** версии Gradle (9.8.0 и 8.12).

## Доступные JDK на машине

- JDK 8 — отдельная установка (для Forge 1.12.2)
- JDK 17 — `C:\Program Files\Eclipse Adoptium\jdk-17.0.20.101-hotspot`
- JDK 21 — `C:\Program Files\Eclipse Adoptium\jdk-21.0.11.10-hotspot`
- JDK 25 — `C:\Program Files\Eclipse Adoptium\jdk-25.0.2.10-hotspot`

## Gradle

- Локальные дистрибутивы: `C:\Users\satda\Desktop\Modding\.tools\gradle-<версия>`
- Установлены: 8.10.2, 8.12, 9.8.0

## Версии ядер (живые данные, проверено по API)

- Fabric Loader: `0.20.1` (ветка стабильных)
- Yarn (1.21.1): `1.21.1+build.3`
- Fabric API (1.21.1): `0.116.17+1.21.1`; последняя стабильная — `0.164.0+26.3`
- NeoForge (21.1.x): `21.1.264`
- Forge (1.20.1): `1.20.1-47.4.28`
- Forge (1.21.1): `1.21.1-52.1.20`
- Forge (1.12.2): `1.12.2-14.23.5.2864`
- Quilt Loader (стабильные): `0.30.1`, `0.30.0`, `0.29.2`
- QSL/QFAPI: `7.7.0+0.92.2-1.20.1` (для 1.21 — только альфы)
- Minecraft (последний релиз): `26.3`

## Где брать актуальные версии

- Fabric Loader: https://meta.fabricmc.net/v2/versions/loader
- Yarn: https://meta.fabricmc.net/v2/versions/yarn/<версия>
- NeoForge: https://maven.neoforged.net/releases/net/neoforged/neoforge/maven-metadata.xml
- Forge: https://maven.minecraftforge.net/net/minecraftforge/forge/maven-metadata.xml
- Quilt Loader: https://meta.quiltmc.org/v3/versions/loader
- QSL/QFAPI: https://api.modrinth.com/v2/project/qsl/version
- Fabric API (Modrinth): https://api.modrinth.com/v2/project/fabric-api/version
- Minecraft: https://piston-meta.mojang.com/mc/game/version_manifest_v2.json
