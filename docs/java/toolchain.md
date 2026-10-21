# Toolchain: Gradle, JDK и плагины сборки

> Проверено 2026-10-21. Главное правило: **версия Gradle и версия JDK зависят от
> плагина загрузчика**, а не только от версии Minecraft.

## Что на чём собирается

| Загрузчик | MC | Плагин | Gradle | JDK | Маппинги |
|---|---|---|---|---|---|
| Fabric | 26.x | Loom 1.18-SNAPSHOT / 1.19.2 | 9.x | 25 | mojang |
| Fabric | 1.21.x | Loom 1.18.x / 1.19.x | ≥ 9.8.0 | ≥ 25 | yarn / mojang |
| NeoForge | 26.x | ModDevGradle 2.0.148 | 8.8+ / 9.x | 21 / 25 | mojang |
| NeoForge | 1.21.x | ModDevGradle 2.x | 8.8+ / 9.x | 21 | mojang |
| Forge | 26.x | ForgeGradle 6.0.54 | **8.x** | 21 | mojang |
| Forge | 1.21.x | ForgeGradle 6.x | 8.x | 21 | mojang |
| Forge | 1.20.1 | ForgeGradle 6.x | 8.x | 17 | mojang |
| Forge | 1.19–1.20 | ForgeGradle 5.x/6.x | 7.6–8.x | 17 | mojang |
| Forge | 1.16.5–1.18.2 | ForgeGradle 5.x | 7.x | 8/16/17 | mojang |
| Forge | 1.12.2 | ForgeGradle 2.3 | 4.10.3 | 8 | mojang |
| Quilt | 1.20.6 | Quilt Loom 1.7.4 | 8.9 | 21 | quilt |
| Paper (плагин) | любая | — | Maven 3.9+ / Gradle | 25 | — |

## Грабли (проверено на практике)

| Симптом | Причина | Что делать |
|---|---|---|
| Сборка Forge падает на Gradle 9 | ForgeGradle 6.x не поддерживает Gradle 9 | Держать Gradle 8.x для Forge |
| Сборка Fabric падает на Gradle 8 | Loom 1.18/1.19 требует Gradle ≥ 9.8.0 | Держать Gradle 9.x для Fabric |
| «Unsupported class file major version» | Плагин требует JDK 25, а запущен JDK 21 | Поставить JDK 25 и обновить toolchain |
| Loom падает на старте | Loom 1.18+ требует JDK 25 | То же |
| `BUILD SUCCESSFUL`, но jar ~261 байт | нет ни одной `modImplementation` → ремапится 0 модов | Добавить зависимости; в логе должно быть `:remapping N mods from modImplementation` |
| `Could not find com.mojang:minecraft:26.3` | опечатка в версии | сверить с `version_manifest_v2.json` |
| `mappings ... not found` | запрошен Yarn для версии без Yarn | убрать строку `mappings` |

> **Вывод:** для Fabric и Forge на одной машине нужны **разные** версии Gradle
> (например 9.8.0 и 8.12) — это нормально и так и задумано.

## Как выбрать JDK

- **26.x → JDK 25.** Это официальная рекомендация Fabric (в шаблоне
  `it.options.release = 25`) и требование Loom 1.18+.
- **1.21.x → JDK 21** достаточно для NeoForge; Fabric с Loom 1.19+ всё равно
  просит 25.
- **1.20.1 / 1.19–1.20 → JDK 17.**
- **1.12.2 → JDK 8.**

В Gradle это фиксируется явно:

```groovy
java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(25)
    }
}
```

или в `gradle.properties`:

```properties
org.gradle.java.installations.paths=C:\\Program Files\\Eclipse Adoptium\\jdk-25.0.2.10-hotspot
```

## Как обновить Gradle

```bash
./gradlew wrapper --gradle-version latest
```

После смены версии — сбросить кэш зависимостей:

```bash
./gradlew --refresh-dependencies
```

## Локальные инструменты на этой машине

### JDK

| Версия | Путь |
|---|---|
| 8 | отдельная установка (только Forge 1.12.2) |
| 17 | `C:\Program Files\Eclipse Adoptium\jdk-17.0.20.101-hotspot` |
| 21 | `C:\Program Files\Eclipse Adoptium\jdk-21.0.11.10-hotspot` |
| 25 | `C:\Program Files\Eclipse Adoptium\jdk-25.0.2.10-hotspot` |

### Gradle

- Локальные дистрибутивы: `C:\Users\satda\Desktop\Modding\.tools\gradle-<версия>`
- Установлены: **8.10.2**, **8.12**, **9.8.0**

## Минимальные настройки проекта

### Fabric (26.x)

```groovy
plugins {
    id 'net.fabricmc.fabric-loom' version "${loom_version}"
    id 'maven-publish'
}

loom {
    splitEnvironmentSourceSets()
    mods {
        "modid" {
            sourceSet sourceSets.main
            sourceSet sourceSets.client
        }
    }
}

dependencies {
    minecraft "com.mojang:minecraft:${project.minecraft_version}"
    implementation "net.fabricmc:fabric-loader:${project.loader_version}"
    implementation "net.fabricmc.fabric-api:fabric-api:${project.fabric_api_version}"
}

tasks.withType(JavaCompile).configureEach {
    it.options.release = 25
}
```

### NeoForge (26.3)

```groovy
plugins {
    id 'net.neoforged.moddev' version '2.0.148'
}

neoForge {
    version = project.neo_version
    parchment {
        mappingsVersion = project.parchment_mappings_version
        minecraftVersion = project.parchment_minecraft_version
    }
    runs {
        client { client() }
        server { server() }
    }
    mods {
        "${mod_id}" {
            sourceSet sourceSets.main
        }
    }
}

java {
    toolchain.languageVersion = JavaLanguageVersion.of(25)
}
```

### Forge (26.x)

```groovy
plugins {
    id 'net.minecraftforge.gradle' version '6.0.54'
}

minecraft {
    mappings channel: 'official', version: '1.21.11'
    copyIdeResources = true
}

dependencies {
    minecraft "net.minecraftforge:forge:${minecraft_version}-${forge_version}"
}
```

> Forge собирается **только на Gradle 8.x** — на 9-м падает.

### Paper (плагин, Maven)

```xml
<repository>
  <id>papermc</id>
  <url>https://repo.papermc.io/repository/maven-public/</url>
</repository>
<dependency>
  <groupId>io.papermc.paper</groupId>
  <artifactId>paper-api</artifactId>
  <version>26.3-R0.1-SNAPSHOT</version>
  <scope>provided</scope>
</dependency>
```

Плагин **нельзя** собрать одним `javac`: `paper-api` тянет транзитивные
зависимости (adventure и др.) — нужна Maven или Gradle.

## Полезные ссылки

- Loom: <https://docs.fabricmc.net/develop/loom>
- ModDevGradle: <https://docs.neoforged.net/docs/gettingstarted/moddevgradle/>
- ForgeGradle: <https://docs.minecraftforge.net/en/latest/gettingstarted/>
- Quilt Loom: <https://quiltmc.org/en/develop/loom/>
- Paper: <https://docs.papermc.io>
- Gradle toolchains: <https://docs.gradle.org/current/userguide/toolchains.html>

Связанные документы: [`mappings.md`](mappings.md) · [`loaders.md`](loaders.md) ·
[`migration-26x.md`](migration-26x.md) · [`unsupported.md`](unsupported.md)
