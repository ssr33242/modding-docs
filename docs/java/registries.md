# Регистрация контента в Java Edition (Forge / NeoForge)

Регистрация — это процесс «сообщения» игре о ваших объектах (предметы,
блоки, сущности и так далее). Без регистрации игра о них не знает, что
приводит к странному поведению и крашам.

> Источники (официальные):
> - NeoForge: `https://github.com/neoforged/Documentation/blob/main/docs/concepts/registries.md`
> - MinecraftForge: `https://github.com/MinecraftForge/Documentation`
> - Fabric: `https://docs.fabricmc.net/`

## Что такое реестр

- Реестр — это обёртка над картой «имя → объект».
- Имя называется **registry name** и представлено `ResourceLocation`
  (в NeoForge — `Identifier`, исторически `ResourceLocation`).
- Имена уникальны внутри одного реестра.
- Часто один объект есть в нескольких реестрах: блок в `BLOCKS` и его
  предметная форма в `ITEMS` имеют **одинаковое** registry name.
- Реестры хранят **синглтоны**: каждый объект существует ровно один раз.
  Все блоки камня в мире — один и тот же зарегистрированный экземпляр.
- Registry name ванильного блока земли — `minecraft:dirt`, зомби —
  `minecraft:zombie`. У модов вместо `minecraft` стоит их mod id.

## Как устроена регистрация в ваниле

- Minecraft регистрирует все блоки в классе `Blocks` через
  `Registry#register()`, указывая `BuiltInRegistries.BLOCK`.
- После регистрации игра выполняет проверки (например, что у всех блоков
  есть модель).
- Это работает, потому что `Blocks` загружается классом достаточно рано.
- Моды так не могут — их классы не загружаются автоматически, поэтому нужны
  обходные пути (см. ниже).

## Два способа регистрации (NeoForge)

- `DeferredRegister` — класс-обёртка (рекомендуется).
- `RegisterEvent` — событие регистрации (более низкоуровневый способ).
- `DeferredRegister` построен **поверх** `RegisterEvent`.

### `DeferredRegister`

Создание регистратора:

```java
public static final DeferredRegister<Block> BLOCKS = DeferredRegister.create(
        // Реестр, в который регистрируем.
        // Ванильные реестры — в BuiltInRegistries,
        // реестры NeoForge — в NeoForgeRegistries.
        BuiltInRegistries.BLOCK,
        // Идентификатор мода.
        ExampleMod.MOD_ID
);
```

Регистрация объектов как статических полей:

```java
public static final DeferredHolder<Block, Block> EXAMPLE_BLOCK_1 = BLOCKS.register(
        "example_block",           // registry name
        () -> new Block(...)       // поставщик объекта
);

public static final DeferredHolder<Block, SlabBlock> EXAMPLE_BLOCK_2 = BLOCKS.register(
        "example_block_2",
        registryName -> new SlabBlock(...)  // функция от имени
);
```

Разбор:

- `DeferredHolder<R, T>` держит объект. `R` — тип реестра, `T` — тип
  объекта (может быть подклассом).
- `DeferredHolder` наследует `Supplier<T>`, поэтому поле можно объявить как
  `Supplier<Block>`.
- Объект достаётся через `#get()`.
- Некоторые места требуют именно `Holder`/`DeferredHolder`, а не любой
  `Supplier` — тогда используйте соответствующий тип.

Подключение к событиям в конструкторе мода:

```java
public ExampleMod(IEventBus modBus) {
    ExampleBlocksClass.BLOCKS.register(modBus);
    // остальное
}
```

Есть специализированные варианты `DeferredRegister`:

- `DeferredRegister.Blocks` — для блоков.
- `DeferredRegister.Items` — для предметов.
- `DeferredRegister.DataComponents` — для компонентов данных.
- `DeferredRegister.Entities` — для сущностей.

### `RegisterEvent`

Событие, срабатывающее для каждого реестра, после конструкторов модов и
до загрузки конфигов. Публикуется на **mod-шине**:

```java
@SubscribeEvent
public static void register(RegisterEvent event) {
    event.register(
            // Ключ реестра.
            BuiltInRegistries.BLOCK,
            registry -> {
                registry.register(
                    Identifier.fromNamespaceAndPath(MODID, "example_block_1"),
                    new Block(...));
            }
    );
}
```

- Ключи ванильных реестров — в `BuiltInRegistries`.
- Ключи реестров NeoForge — в `NeoForgeRegistries.Keys`.

## Запросы к реестрам

Реестр — обратимая карта «имя ↔ объект»:

```java
// Получить объект по имени:
BuiltInRegistries.BLOCK.getValue(
    Identifier.fromNamespaceAndPath("minecraft", "dirt"));

// Получить имя объекта:
BuiltInRegistries.BLOCK.getKey(Blocks.DIRT); // "minecraft:dirt"
```

- Проверка наличия: `BuiltInRegistries.BLOCK.containsKey(...)`.
  Отличный способ узнать, установлен ли другой мод.
- Перебор всех ключей: `BuiltInRegistries.BLOCK.keySet()`.
- Перебор всех записей: `BuiltInRegistries.BLOCK.entrySet()`.

Важные правила:

- Запросы всегда идут к **ванильному** `Registry`, а не к
  `DeferredRegister` (тот лишь утилита регистрации).
- **Нельзя** запрашивать реестр, пока регистрация ещё идёт. Делайте это
  после её завершения.

## Свой реестр (для других модов)

Свой реестр позволяет другим модам добавлять контент в ваш мод без правок
вашего кода.

Создание ключа и реестра:

```java
public static final ResourceKey<Registry<Spell>> SPELL_REGISTRY_KEY =
    ResourceKey.createRegistryKey(
        Identifier.fromNamespaceAndPath("yourmodid", "spells"));

public static final Registry<Spell> SPELL_REGISTRY =
    new RegistryBuilder<>(SPELL_REGISTRY_KEY)
        .sync(true)     // синхронизация целочисленных id (для сети)
        .defaultKey(Identifier.fromNamespaceAndPath("yourmodid", "empty"))
        .maxId(256)
        .create();
```

Регистрация самого реестра в корневом реестре через `NewRegistryEvent`:

```java
@SubscribeEvent
public static void registerRegistries(NewRegistryEvent event) {
    event.register(SPELL_REGISTRY);
}
```

Дальше контент регистрируется как обычно — через `DeferredRegister` или
`RegisterEvent`.

## Реестры датапаков (datapack registries)

- Особый вид реестра: данные грузятся из JSON датапака **при загрузке
  мира**, а не при старте игры.
- Примеры: большинство реестров генерации мира.
- Позволяют менять содержимое датапаком без перекомпиляции мода.
- Регистрируются через `DataPackRegistryEvent.NewRegistry`.

## Fabric: регистрация

- В Fabric объекты регистрируют через `Registry.register(...)` в
  `ModInitializer#onInitialize`:

```java
public class ExampleMod implements ModInitializer {
    public static final Item EXAMPLE_ITEM = new Item(
        new Item.Settings());

    @Override
    public void onInitialize() {
        Registry.register(Registries.ITEM,
            Identifier.of("yourmodid", "example_item"),
            EXAMPLE_ITEM);
    }
}
```

- Регистрация выполняется **до** готовности реестров, в момент инициализации
  мода.
- Точные сигнатуры зависят от версии — сверяйтесь с официальными docs
  Fabric.

## Порядок регистрации (NeoForge)

1. Конструктор мода создаёт `DeferredRegister` и вызывает `.register(modBus)`.
2. Для каждого реестра публикуется `RegisterEvent`.
3. Регистрируются события реестров (`NewRegistryEvent`,
   `DataPackRegistryEvent.NewRegistry`).
4. Только **после** этого можно безопасно читать реестры.

## Частые ошибки

- **Запрос реестра во время регистрации** — краш или пустой результат.
- **Дубликат registry name** в одном реестре — ошибка регистрации.
- **Пустое имя** — невалидная запись.
- **`DeferredRegister` не подключён к modBus** — объекты не регистрируются.
- **Использование `DeferredRegister` для запросов** — для чтения нужен
  `Registry` (`BuiltInRegistries`), а не регистратор.
- **Обращение к `DeferredHolder#get()` слишком рано** — объект ещё не
  создан, вернётся ошибка/пусто.
- **Регистрация на неверной шине** — `RegisterEvent` идёт на mod-шине.

## Проверка версий

- Пакеты (`BuiltInRegistries` / `Registry` / `ResourceLocation` vs
  `Identifier`), сигнатуры и события меняются между версиями и загрузчиками.
- Версии Minecraft и загрузчиков см. в документе про версии.
- Сверяйтесь с официальной документацией загрузчика под вашу версию.
