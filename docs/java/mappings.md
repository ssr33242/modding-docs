# Маппинги: Mojang, Yarn, Parchment и кто что использует

> Проверено 2026-10-21. Главный факт: **Yarn остановился на 1.21.11**, поэтому
> начиная с **26.x** Fabric-моды собираются на **официальных маппингах Mojang**.

## Что такое маппинг

Маппинг — это таблица переименований: obfuscated-имя класса/метода/поля
(`a`, `b`, `c`) → человекочитаемое (`Entity`, `tick`, `health`). Minecraft
поставляется обфусцированным, и без маппингов в IDE невозможно читать код.

| Вид | Что это | Кто использует |
|---|---|---|
| **Mojang official (mojmap)** | имена прямо от Mojang, лежат в манифесте версий | NeoForge, Forge, Fabric (на 26.x), Quilt (в режиме mojang) |
| **Yarn** | отдельный проект FabricMC, «человеческие» имена поверх Mojang | Fabric до 1.21.11 |
| **Parchment** | только аннотации/документация поверх официальных имён | Quilt ( quilt mappings = Parchment + mojmap ), Forge (в паре с official) |
| **SRG / official-to-srg** | промежуточные имена Forge | Forge (внутренне) |

## Кто что использует сейчас

| Загрузчик | MC 1.21.x | MC 26.x |
|---|---|---|
| Fabric | Yarn (`1.21.11+build.6` и старше) **или** mojmap | **только mojmap** |
| NeoForge | mojmap | mojmap |
| Forge | mojmap (official) + Parchment-аннотации | mojmap |
| Quilt | quilt mappings (Parchment + mojmap) | mojmap (см. unsupported.md) |

## Yarn: где конец

- Последняя сборка Yarn: **`1.21.11+build.6`** (`meta.fabricmc.net/v2/versions/yarn`).
- Всего билдов в истории: 3412.
- Под версии **26.1 / 26.2 / 26.3 / 26.4** Yarn **не выпускается**.
- Официальный шаблон Fabric для 26.3 (`fabric-example-mod`, ветка `26.3`) **не содержит
  строки `mappings`** — значит используются официальные маппинги Mojang.

### Что это значит на практике

Код мода, написанный под Yarn, нужно переименовать при переходе на 26.x:
`net.minecraft.entity.Entity` → `net.minecraft.world.entity.Entity` и т.д.
(переименования соответствуют официальным именам Mojang).

Миграция называется **«unmap»/«un-yarn»** — механические замены имён плюс
перенос javadoc-комментариев из Parchment.

## Как выбрать маппинги в Gradle

### Fabric — mojmap (то, что нужно для 26.x)

```groovy
dependencies {
    minecraft "com.mojang:minecraft:${project.minecraft_version}"
    implementation "net.fabricmc:fabric-loader:${project.loader_version}"
    implementation "net.fabricmc.fabric-api:fabric-api:${project.fabric_api_version}"
    // строки mappings НЕТ — Loom по умолчанию берёт официальные маппинги Mojang
}
```

### Fabric — Yarn (для 1.21.x)

```groovy
dependencies {
    minecraft "com.mojang:minecraft:${project.minecraft_version}"
    mappings "net.fabricmc:yarn:${project.yarn_mappings}:v2"
    implementation "net.fabricmc:fabric-loader:${project.loader_version}"
}
```

### Quilt — quilt mappings

```groovy
dependencies {
    minecraft "com.mojang:minecraft:${project.minecraft_version}"
    mappings "org.quiltmc:quilt-mappings:${project.quilt_mappings}:intermediary"
}
```

### NeoForge / Forge

Маппинги приходят вместе с ядром — отдельно подключать **не нужно**:

```groovy
// NeoForge
neoForge "net.neoforged:neoforge:${neo_version}"
// Forge
minecraft "net.minecraftforge:forge:${forge_version}"
```

## Частые ошибки

| Симптом | Причина | Решение |
|---|---|---|
| `mappings ... not found` | Запрошен Yarn для версии без Yarn | Убрать строку `mappings` (mojmap) или сменить версию |
| `Could not find com.mojang:minecraft:26.3` | Опечатка в версии или нет доступа к манифесту | Проверить версию по `version_manifest_v2.json` |
| Классы не находятся после смены маппингов | Остались имена из другого набора | Переименовать импорты (un-yarn) |
| `Cannot apply a mapping to an already mapped name` | В проекте смешаны mojmap и Yarn | Привести к одному набору |

## Где смотреть актуальные маппинги

- Yarn: <https://meta.fabricmc.net/v2/versions/yarn>
- Официальные маппинги Mojang: <https://piston-meta.mojang.com/mc/game/version_manifest_v2.json>
  → в блоке каждой версии `downloads.client_mappings`
- Quilt mappings: <https://meta.quiltmc.org/v3/versions/>
- Parchment (Forge): <https://parchmentmc.org>

Связанные документы: [`toolchain.md`](toolchain.md) · [`migration-26x.md`](migration-26x.md) ·
[`unsupported.md`](unsupported.md)
