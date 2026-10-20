# События в Java Edition (Forge / NeoForge)

События — один из главных механизмов моддинга. Игра «публикует» события,
когда что-то происходит (игрок кликнул, сущность прыгнула, блок отрисован,
игра загрузилась). Мод подписывается на нужные события и выполняет код.

> Источники (официальные):
> - NeoForge: `https://github.com/neoforged/Documentation/blob/main/docs/concepts/events.md`
> - MinecraftForge: `https://github.com/MinecraftForge/Documentation`
> - Fabric: `https://docs.fabricmc.net/`

## Шины событий (event bus)

- `NeoForge.EVENT_BUS` — **главная (game) шина**. Большинство игровых
  событий публикуется здесь.
- **Mod-шина** — своя шина у каждого мода, передаётся в конструктор мода.
  Здесь публикуются события жизненного цикла и регистрации.
- События главной шины выполняются на одном потоке и **последовательно**.
- События mod-шины часто выполняются **параллельно** (быстрее при запуске).

## Как подписаться на событие

Обработчик — метод с одним параметром-событием и возвратом `void`. Есть
три способа подписки.

### Способ 1: `IEventBus#addListener`

```java
@Mod("yourmodid")
public class YourMod {
    public YourMod(IEventBus modBus) {
        NeoForge.EVENT_BUS.addListener(YourMod::onLivingJump);
    }

    private static void onLivingJump(LivingEvent.LivingJumpEvent event) {
        LivingEntity entity = event.getEntity();
        if (!entity.level().isClientSide()) {
            entity.heal(1);
        }
    }
}
```

### Способ 2: `@SubscribeEvent`

```java
public class EventHandler {
    @SubscribeEvent
    public void onLivingJump(LivingEvent.LivingJumpEvent event) {
        LivingEntity entity = event.getEntity();
        if (!entity.level().isClientSide()) {
            entity.heal(1);
        }
    }
}

@Mod("yourmodid")
public class YourMod {
    public YourMod(IEventBus modBus) {
        NeoForge.EVENT_BUS.register(new EventHandler());
    }
}
```

Можно и статически: обработчики `static`, а вместо объекта передаётся класс:
`NeoForge.EVENT_BUS.register(EventHandler.class)`.

### Способ 3: `@EventBusSubscriber`

Аннотация на класс — NeoForge сам найдёт и зарегистрирует обработчики,
конструктор мода трогать не нужно:

```java
@EventBusSubscriber(modid = "yourmodid")
public class EventHandler {
    @SubscribeEvent
    public static void onLivingJump(LivingEvent.LivingJumpEvent event) {
        LivingEntity entity = event.getEntity();
        if (!entity.level().isClientSide()) {
            entity.heal(1);
        }
    }
}
```

Рекомендуется указывать `modid` — легче отлаживать конфликты модов.

## Иерархия событий

- Часть событий наследуется от `Event`, часть — от подклассов с контекстом:
  - `BlockEvent` — контекст блока.
  - `EntityEvent` — контекст сущности.
  - `LivingEvent` — контекст живой сущности.
  - `PlayerEvent` — контекст игрока.
- Эти «контекстные» суперклассы **абстрактные** — подписываться на них
  **нельзя**, игра упадёт. Подписывайтесь на конкретные подтипы.

## Отменяемые события

- Некоторые события реализуют `ICancellableEvent`.
- Отмена: `event.setCanceled(true)`.
- Проверка: `event.isCanceled()`.
- После отмены остальные обработчики **не выполняются**, и включается
  «отменяющее» поведение (например, отмена смены цели сущности).
- Обработчик может явно получать отменённые события: параметр
  `receiveCanceled = true` в `addListener` или `@SubscribeEvent`.

## TriState и Result

- Некоторые события имеют три состояния через `TriState`:
  - `TriState.TRUE` — принудительно выполнить действие.
  - `TriState.FALSE` — отменить действие.
  - `TriState.DEFAULT` — стандартное поведение игры.
- Другие события используют enum `Result` прямо на классе (например,
  `MobDespawnEvent.Result.DENY`).
- Управление — через `set*`-метод события:

```java
@SubscribeEvent
public static void renderNameTag(RenderNameTagEvent.CanRender event) {
    event.setCanRender(TriState.FALSE);
}

@SubscribeEvent
public static void mobDespawn(MobDespawnEvent event) {
    event.setResult(MobDespawnEvent.Result.DENY);
}
```

## Приоритет обработчиков

- Enum `EventPriority`: `HIGHEST`, `HIGH`, `NORMAL` (по умолчанию), `LOW`,
  `LOWEST`.
- Обработчики выполняются от `HIGHEST` к `LOWEST`.
- При равном приоритете — в порядке регистрации.
- Приоритет задаётся параметром `priority` в `addListener` /
  `@SubscribeEvent`.
- Приоритеты **игнорируются** для событий, которые публикуются параллельно.

## Сторона (side)

- Часть событий существует только на клиенте (например, события рендера).
- Клиентские обработчики регистрируйте в клиентском классе.
- С `@EventBusSubscriber` укажите сторону:
  `@EventBusSubscriber(value = Dist.CLIENT, modid = "yourmodid")`.
- С `addListener` проверяйте сторону через `FMLEnvironment#getDist`.

## Шина мода и жизненный цикл

События mod-шины отличаются тем, что реализуют `IModBusEvent`. Порядок
запуска:

1. Вызывается конструктор мода — здесь регистрируйте обработчики.
2. Срабатывают все `@EventBusSubscriber`.
3. `FMLConstructModEvent`.
4. События реестров: `NewRegistryEvent`, `DataPackRegistryEvent.NewRegistry`,
   и для каждого реестра `RegisterEvent`.
5. `FMLCommonSetupEvent` — общая настройка.
6. Настройка по стороне: `FMLClientSetupEvent` (клиент) или
   `FMLDedicatedServerSetupEvent` (сервер).
7. Обработка `InterModComms`.
8. `FMLLoadCompleteEvent`.

- Многие события жизненного цикла выполняются параллельно. Чтобы выполнить
  код в главном потоке, используйте `#enqueueWork(Runnable)`.

## `InterModComms` — сообщения между модами

- Система обмена данными между модами для совместимости.
- `InterModEnqueueEvent` — отправка: `InterModComms#sendTo(...)`.
- `InterModProcessEvent` — приём: `InterModComms#getMessages(...)`.
- Сообщения представлены объектами `IMCMessage` (отправитель, получатель,
  ключ, поставщик данных).
- Все методы класса потокобезопасны.

## Прочие события mod-шины

Примеры (часть исторически осталась на mod-шине):

- `RegisterColorHandlersEvent.BlockTintSources`, `.ItemTintSources`,
  `.ColorResolvers`.
- `ModelEvent.BakingCompleted`.
- `TextureAtlasStitchedEvent`.

Часть из них планируют перенести на game-шину в будущих версиях.

## Примеры типичных событий

- `LivingEvent.LivingJumpEvent` — живая сущность прыгнула.
- `PlayerEvent.PlayerLoggedInEvent` — игрок вошёл.
- `PlayerEvent.PlayerLoggedOutEvent` — игрок вышел.
- `BlockEvent.BreakEvent` — блок сломан.
- `BlockEvent.BlockToolModificationEvent` — инструмент изменил блок.
- `EntityJoinLevelEvent` — сущность появилась в мире.
- `ServerTickEvent` / `ClientTickEvent` — тик сервера/клиента.
- `RegisterCommandsEvent` — регистрация команд.
- `MobDespawnEvent` — моб исчезает.

## Частые ошибки

- **Подписка на абстрактное событие** (`BlockEvent`, `EntityEvent`,
  `LivingEvent`, `PlayerEvent`) — краш игры.
- **Изменение мира в клиентском событии на сервере или наоборот** —
  проверяйте `isClientSide()`.
- **Регистрация в конструкторе не на той шине** (game вместо mod или
  наоборот) — событие не сработает.
- **Тяжёлая логика в тиковом событии** — просадка производительности.
- **Забыт `receiveCanceled`** — обработчик не увидит отменённые события.
- **Проверка стороны через `@EventBusSubscriber` без `value`** —
  клиентские события могут не зарегистрироваться.

## Проверка версий

- Имена событий, их пакеты и способы регистрации меняются между версиями.
- Версии загрузчиков см. в документе про версии.
- Ориентируйтесь на официальную документацию загрузчика для вашей версии.
