# Матрица совместимости

Все строки ниже **проверены реальной сборкой** на этой машине.

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
- NeoForge 21.1.x → ModDevGradle 2.x → Gradle 8.8+ / 9.x → JDK 21
- Forge 1.20.1 (47.x) → ForgeGradle 6.x → Gradle 8.x → JDK 17
- Forge 1.12.2 (14.23.5.286x) → ForgeGradle 2.3 / 3.x → Gradle 4.10.x → JDK 8

## Доступные JDK на машине

- JDK 17 — `C:\Program Files\Eclipse Adoptium\jdk-17.0.20.101-hotspot`
- JDK 21 — `C:\Program Files\Eclipse Adoptium\jdk-21.0.11.10-hotspot`
- JDK 25 — `C:\Program Files\Eclipse Adoptium\jdk-25.0.2.10-hotspot`

## Gradle

- Локальные дистрибутивы: `C:\Users\satda\MCreatorWorkspaces\modgen\.tools\gradle-<версия>`
- Установлены: 8.10.2, 8.12, 9.8.0

## Версии ядер (живые данные)

- Fabric Loader: 0.20.1
- Yarn (1.21.1): 1.21.1+build.3
- NeoForge (21.1.x): 21.1.264
- Forge (1.20.1): 1.20.1-47.4.28
- Forge (1.12.2): 1.12.2-14.23.5.2864
- Minecraft (последний релиз): 26.3

## Где брать актуальные версии

- Fabric: https://meta.fabricmc.net/v2/versions/loader
- Yarn: https://meta.fabricmc.net/v2/versions/yarn/<версия>
- NeoForge: https://maven.neoforged.net/releases/net/neoforged/neoforge/maven-metadata.xml
- Forge: https://maven.minecraftforge.net/net/minecraftforge/forge/maven-metadata.xml
- Fabric API (Modrinth): https://api.modrinth.com/v2/project/fabric-api/version
- Minecraft: https://piston-meta.mojang.com/mc/game/version_manifest_v2.json
