# Версии Minecraft и загрузчиков (актуально на октябрь 2026)

> **Важно:** нумерация Minecraft: Java Edition изменилась. После `1.21.11`
> Mojang перешла на новую схему: `26.1`, `26.2`, `26.3` и так далее (год +
> номер релиза в году). Всё, что раньше было «1.21.x», теперь продолжается
> как «26.x». Если в гайде написано `1.21.1`, это уже **не** самая свежая
> версия.

## Где брать данные (официальные источники)

- Minecraft: Java Edition — манифест версий Mojang:
  `https://piston-meta.mojang.com/mc/game/version_manifest_v2.json`
- Forge — Maven-метаданные:
  `https://maven.minecraftforge.net/net/minecraftforge/forge/maven-metadata.xml`
- NeoForge — Maven-метаданные:
  `https://maven.neoforged.net/releases/net/neoforged/neoforge/maven-metadata.xml`
- Fabric — официальный meta-сервис:
  `https://meta.fabricmc.net/v2/versions/loader`
  `https://meta.fabricmc.net/v2/versions/game`
- Paper — официальный API (v2 закрыт, используйте v3):
  `https://fill.papermc.io/v3/projects/paper`
- Bedrock — официальные примеры и версия:
  `https://github.com/Mojang/bedrock-samples` (файл `version.json`)

## Актуальные версии Java Edition

- **Последний релиз:** `26.3`
- **Последний снапшот:** `26.4-snapshot-5`

Релизы по порядку (от новых к старым):

1. `26.3`
2. `26.2`
3. `26.1.2`, `26.1.1`, `26.1`
4. `1.21.11`, `1.21.10`, `1.21.9`, `1.21.8`, `1.21.7`, `1.21.6`, `1.21.5`,
   `1.21.4`, `1.21.3`, `1.21.2`, `1.21.1`, `1.21`

## Версии загрузчиков для 26.x

- **Forge:** `26.3-66.0.13` (для Minecraft `26.3`), `26.2-65.1.5`,
  `26.1.2-64.1.5`
- **NeoForge:** `26.3.0.95` (для Minecraft `26.3`), `26.1.2.122`
- **Fabric:** loader `0.20.1`, Fabric API `0.164.1+26.4`
- **Paper:** `26.3` (сборка для `26.3`, есть и `26.3-rc-3`)

## Версии загрузчиков для 1.21.x (для старых сборок)

- **Forge:** `1.21.11-61.2.4`, `1.21.8-58.1.26`, `1.21.4-54.1.22`,
  `1.21.1-52.1.20`
- **NeoForge:** `21.4.77-beta` (для `1.21.4`), `21.1.264` (для `1.21.1`)

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

Gradle для Forge (`gradle.properties`), Minecraft `26.3`:

```properties
minecraft_version=26.3
forge_version=26.3-66.0.13
```

Gradle для NeoForge (`gradle.properties`), Minecraft `26.3`:

```properties
minecraft_version=26.3
neo_version=26.3.0.95
```

Gradle для Fabric (`gradle.properties`), Minecraft `26.3`:

```properties
minecraft_version=26.3
loader_version=0.20.1
fabric_version=0.164.1+26.4
```

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
  проверять в живых источниках (список выше).
- Прежде чем писать код под версию, уточните у пользователя, какая у него
  версия Minecraft и загрузчика — API между версиями ломается.
- Между крупными версиями (например, `1.21` и `26.3`) меняются имена
  методов, пакеты и реестры. Код, написанный под `1.21.1`, часто **не
  соберётся** под `26.3` без правок.
- Для Bedrock версия аддона — это `min_engine_version` в манифесте, и она
  отдельная от версии скриптового API (`@minecraft/server`).
