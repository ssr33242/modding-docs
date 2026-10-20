# Команды в Java Edition (Brigadier)

Команды в Java Edition запускаются из чата через слеш (`/`), из консоли
сервера, из командных блоков и из функций. Мод может регистрировать свои
команды.

> Источники (официальные):
> - NeoForge: команды —
>   `https://github.com/neoforged/Documentation/blob/main/docs/misc/commands.md`
> - MinecraftForge: команды —
>   `https://github.com/MinecraftForge/Documentation`
> - Mojang Brigadier (библиотека разбора команд):
>   `https://github.com/Mojang/brigadier`
> - Fabric: команды — `https://docs.fabricmc.net/`

## Что такое Brigadier

- Команды в Minecraft строятся на библиотеке **Brigadier** от Mojang.
- Команда — это **дерево узлов** (tree of nodes) с корнем-диспетчером
  (`CommandDispatcher`).
- **Литерал** (`literal`) — фиксированное слово, например `mymod` или
  `reload` в `/mymod reload`.
- **Аргумент** (`argument`) — именованный входной параметр с типом, например
  число или селектор сущности.
- Узлы соединяются через `.then(...)`, а выполняются через `.executes(...)`.
- Узел может иметь логику выполнения, дочерние узлы или и то, и другое.

## Как устроен аргумент

- Аргумент **объявляется** при построении дерева: имя + `ArgumentType`.
- Его значение **читается** в логике выполнения из `CommandContext` по тому
  же имени.
- Имя — это контракт между объявлением и чтением.

## Регистрация команды (NeoForge)

Дерево команд передаётся в `CommandDispatcher#register` во время события
`RegisterCommandsEvent`:

```java
@SubscribeEvent
public static void registerCommands(RegisterCommandsEvent event) {
    event.getDispatcher().register(
        Commands.literal("mymod")
            .then(Commands.literal("reload")
                .executes(context -> {
                    // Логика команды
                    return Command.SINGLE_SUCCESS;
                })
                .then(Commands.literal("force")
                    .executes(context -> {
                        // Логика команды
                        return Command.SINGLE_SUCCESS;
                    })
                )
            )
    );
}
```

Разбор:

- `Commands.literal("mymod")` — начинает литерал.
- `.then(...)` — присоединяет дочерний узел.
- `.executes(...)` — задаёт `Command`-колбэк.
- Возвращаемый `int` — число результатов (сколько игроков затронуто).
- Пример выше регистрирует `/mymod reload` и `/mymod reload force`.

## Регистрация команды (MinecraftForge)

В Forge используется то же событие, но с шиной событий Forge:

```java
@SubscribeEvent
public static void onRegisterCommands(RegisterCommandsEvent event) {
    event.getDispatcher().register(
        Commands.literal("mymod")
            .then(Commands.literal("hello")
                .executes(ctx -> {
                    ctx.getSource().sendSuccess(
                        () -> Component.literal("Привет!"), false);
                    return 1;
                })
            )
    );
}
```

- `RegisterCommandsEvent` — общий класс, есть и в Forge, и в NeoForge.
- Регистрируйте обработчик на **game**-шине (`NeoForge.EVENT_BUS` /
  `MinecraftForge.EVENT_BUS`).

## Клиентские команды

- Если зарегистрировать команду в `RegisterClientCommandsEvent`, она будет
  работать **только на клиенте**.
- На сервере такая команда недоступна.
- Серверные команды регистрируются в `RegisterCommandsEvent`.

## Права доступа (`requires`)

Права задаются методом `#requires` — предикат по `CommandSourceStack`:

```java
Commands.literal("op-me")
    .requires(Commands.hasPermission(Commands.LEVEL_OWNERS))
    .executes(context -> {
        // логика
        return Command.SINGLE_SUCCESS;
    })
```

Уровни прав в классе `Commands`:

- `LEVEL_ALL` — все.
- `LEVEL_MODERATORS` — модераторы.
- `LEVEL_GAMEMASTERS` — гейм-мастера.
- `LEVEL_ADMINS` — администраторы.
- `LEVEL_OWNERS` — владельцы.

Предикат вычисляется на сервере, поэтому может проверять уровень прав
и другое состояние.

## Аргументы команды

Стандартные типы аргументов (из Brigadier и Minecraft):

- `IntegerArgumentType.integer(min, max)` — целое число.
- `DoubleArgumentType.doubleArg(min, max)` — число с плавающей точкой.
- `BoolArgumentType.bool()` — булево.
- `StringArgumentType.word()` / `.string()` / `.greedyString()` — строки.
- `EntityArgument.player(ctx)` / `.players(ctx)` — игрок/игроки.
- `EntityArgument.entity(ctx)` / `.entities(ctx)` — сущность/сущности.
- `BlockPosArgument.blockPos()` — позиция блока.
- `Vec3Argument.vec3()` — координаты (с относительными `~`).
- `ScoreHolderArgument.scoreHolder()` — держатель счёта.
- `ResourceLocationArgument.id()` — идентификатор ресурса.

Пример с аргументом:

```java
Commands.literal("mymod")
    .then(Commands.literal("heal")
        .then(Commands.argument("target", EntityArgument.players())
            .executes(context -> {
                Collection<ServerPlayer> players =
                    EntityArgument.getPlayers(context, "target");
                for (ServerPlayer p : players) {
                    p.heal(20.0f);
                }
                return players.size();
            })
        )
    );
```

Использование: `/mymod heal @a`.

## Чтение аргументов

- Значения достаются из `CommandContext` по имени, использованному при
  объявлении:

```java
int amount = IntegerArgumentType.getInteger(context, "amount");
String name = StringArgumentType.getString(context, "name");
```

- `context.getSource()` даёт `CommandSourceStack` (кто/где выполняет).

## Отправка ответа игроку

- `context.getSource().sendSuccess(supplier, broadcastToOps)` — обычный
  ответ команды.
- `sendFailure(...)` — сообщение об ошибке (красным).
- В новых версиях текст — это `Component` (`Component.literal("...")`),
  а не `String`/`TextComponent`.

## Рекомендации по регистрации

- Регистрируйте команды в `RegisterCommandsEvent`, не в конструкторе мода.
- Для аргументов, требующих доступа к реестрам, используйте
  `RegisterCommandsEvent#getBuildContext` (`CommandBuildContext`) — он
  передаётся в типы аргументов, которым он нужен.
- Предикаты `requires` не должны иметь побочных эффектов.

## Частые ошибки

- **Регистрация команды вне `RegisterCommandsEvent`** — команда не
  появится.
- **Обработчик не на game-шине** — событие не сработает.
- **Возврат результата `0` или отрицательного числа** — команда считается
  неуспешной.
- **Опечатка в имени аргумента** при чтении из контекста — `IllegalArgumentException`.
- **Строковые литералы вместо `Component`** в новых версиях — не
  скомпилируется.
- **Проверка прав только на клиенте** — обязательно проверяйте на сервере
  через `requires`.
- **`getBuildContext` не передан** аргументу, который его требует — ошибка
  при построении дерева.

## Проверка версий

- Классы и методы Brigadier/Minecraft меняются между версиями.
- Актуальные версии загрузчиков и Minecraft — см. документ про версии.
- Сверяйтесь с официальной документацией загрузчика под вашу версию.
