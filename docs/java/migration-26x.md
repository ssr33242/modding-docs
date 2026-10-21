# Миграция на 26.x: с 1.21.x на новую ветку

> Проверено 2026-10-21. Источники: [Fabric — Porting to 26.2](https://github.com/FabricMC/fabric-docs/blob/main/develop/porting/index.md),
> [Fabric — Migrating Mappings](https://github.com/FabricMC/fabric-docs/blob/main/develop/porting/mappings/index.md),
> [Fabric: Removing Obfuscation from Fabric](https://fabricmc.net/2025/10/31/obfuscation.html).

## Главное, что изменилось

1. **Minecraft 26.1+ больше не обфусцирован.** Mojang выпустила первую версию
   с открытым кодом — [Removing Obfuscation in Java Edition](https://www.minecraft.net/en-us/article/removing-obfuscation-in-java-edition).
   Значит, обфусцированных имён больше нет, и отдельные маппинги стали не нужны.
2. **Fabric прекратил вести сторонние маппинги** (Yarn). Это решение объявлено
   в [fabricmc.net/2025/10/31/obfuscation.html](https://fabricmc.net/2025/10/31/obfuscation.html);
   Yarn — проект 2016–2025.
3. Значит, для 26.x **обязателен переход с Yarn на официальные маппинги Mojang**
   (в 26.1+ это просто имена из игры).
4. **Java 25** — новый базовый JDK для 26.x (в официальном шаблоне Fabric:
   `it.options.release = 25`).

## Шаг 1. Обновить сборку

```bash
./gradlew wrapper --gradle-version latest
```

В `gradle.properties` (пример — официальный шаблон `fabric-example-mod`, ветка `26.3`):

```properties
minecraft_version=26.3
loader_version=0.19.5
loom_version=1.18-SNAPSHOT
fabric_api_version=0.163.0+26.3
```

В `build.gradle` **уберите строку `mappings`** — Loom по умолчанию возьмёт
официальные маппинги:

```groovy
dependencies {
    minecraft "com.mojang:minecraft:${project.minecraft_version}"
    implementation "net.fabricmc:fabric-loader:${project.loader_version}"
    implementation "net.fabricmc.fabric-api:fabric-api:${project.fabric_api_version}"
    // mappings "net.fabricmc:yarn:..." — УДАЛИТЬ
}
```

После правки — обновить кэш зависимостей:

```bash
./gradlew --refresh-dependencies
```

## Шаг 2. Перевести маппинги

Официальный Fabric предлагает два пути:

| Способ | Как | Kotlin | Когда брать |
|---|---|---|---|
| **Loom, задача `migrateMappings`** | `./gradlew migrateMappings` | ❌ не поддерживается | Java-моды, быстрый старт |
| **Ravel (плагин для IntelliJ IDEA)** | GUI-мастер в IDE | ✅ поддерживается | Kotlin-моды и сложные проекты |

> Fabric API сам мигрировал на mojmap через Ravel — см. [PR #4690](https://github.com/FabricMC/fabric/pull/4960).

Ни один из способов не делает всё идеально: **результат надо вычитать и доправить
вручную, особенно Mixin-ы** (в `@Shadow`, `@Inject`, `@At` имена полей/методов
меняются по официальным именам).

### Что именно переименуется

Yarn-имена → официальные имена Mojang:

| Yarn | Mojang (26.x) |
|---|---|
| `net.minecraft.entity.Entity` | `net.minecraft.world.entity.Entity` |
| `net.minecraft.util.math.Vec3d` | `net.minecraft.world.phys.Vec3` |
| `net.minecraft.item.ItemStack` | `net.minecraft.world.item.ItemStack` |
| `net.minecraft.util.Identifier` | `net.minecraft.resources.ResourceLocation` |
| `net.minecraft.server.MinecraftServer` | `net.minecraft.server.MinecraftServer` (без изменений) |

Полные таблицы переименований — в гайде Fabric
[`develop/porting/mappings/`](https://github.com/FabricMC/fabric-docs/tree/main/develop/porting/mappings).

## Шаг 3. Поправить код

Порядок работы (рекомендация Fabric):

1. Обновить build-скрипт, убедиться, что проект **собирается** (пусть даже с
   ошибками компиляции).
2. Прогнать `migrateMappings` / Ravel и разобрать автозамены.
3. Чинить компиляцию сверху вниз: сначала импорты, потом сигнатуры методов,
   потом логика.
4. Отдельно проверить **Mixins** — там строковые имена полей не подсказываются
   компилятором.
5. Проверить **datagen** и **ресурсы**: JSON-пути вида
   `data/<modid>/recipes/...` в 26.x менялись вместе с переездом registry-каталогов.

## Шаг 4. Проверить, что мод реально работает

`BUILD SUCCESSFUL` **не значит**, что мод рабочий:

- распаковать `build/libs/*.jar` и убедиться, что внутри есть `.class`;
- запустить клиент и сервер, проверить регистрацию блоков/предметов/рецептов;
- проверить, что datagen-ресурсы попали в jar.

Подробно — в [`unsupported.md`](../java/unsupported.md) (раздел про пустой jar).

## Официальные гайды под каждую версию

| Версия | Гайд |
|---|---|
| 26.2 | [Fabric — Porting to 26.2](https://github.com/FabricMC/fabric-docs/blob/main/develop/porting/index.md) |
| 26.1 → 26.2 | [NeoForge Migration Primer 26.2](https://docs.neoforged.net/primer/docs/26.2/) |
| Обзоры изменений | [fabricmc.net/2026/06/15/262.html](https://fabricmc.net/2026/06/15/262.html) |
| Что нового в игре | [minecraft.net — Java Edition 26.2](https://www.minecraft.net/en-us/article/minecraft-java-edition-26-2) |
| Нейтральный обзор | [minecraft.wiki — Java Edition 26.2](https://minecraft.wiki/w/Java_Edition_26.2) |

В зеркале документации Fabric эти гайды лежат локально:
`fabric-docs/develop/porting/` и `fabric-docs/versions/26.1.2/`.

## Итого: чек-лист

- [ ] `./gradlew wrapper --gradle-version latest`
- [ ] `minecraft_version` → 26.x, `loader_version`, `loom_version`, `fabric_api_version` обновлены
- [ ] строка `mappings` (Yarn) удалена
- [ ] `migrateMappings` или Ravel выполнены
- [ ] импорты и сигнатуры исправлены
- [ ] Mixin-цели переименованы вручную
- [ ] JDK 25
- [ ] сборка успешна **и** jar непустой
- [ ] мод проверен в игре
