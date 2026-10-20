# Скриптинг Bedrock Edition (`@minecraft/server`)

Скрипты в Bedrock — это обычный JavaScript, который выполняется движком
игры. Они дают доступ к сущностям, блокам, инвентарям, событиям и
интерфейсу. Скрипты лежат в паке поведения и подключаются через манифест.

> Источники (официальные):
> - Типы API: `@minecraft/server`, `@minecraft/server-ui` на npm
>   (`https://registry.npmjs.org/@minecraft/server`,
>   `https://unpkg.com/@minecraft/server@2.10.0/index.d.ts`).
> - Официальные примеры: `https://github.com/Mojang/bedrock-samples`.
> - Документация: `https://learn.microsoft.com/minecraft/creator`.

## Подключение скриптов

В манифесте пака поведения нужно добавить модуль `script` и зависимости:

```json
{
  "format_version": 2,
  "header": {
    "name": "My Scripts",
    "description": "Скриптовый аддон",
    "uuid": "11111111-2222-3333-4444-555555555555",
    "version": [1, 0, 0],
    "min_engine_version": [1, 26, 50]
  },
  "modules": [
    {
      "type": "data",
      "uuid": "66666666-7777-8888-9999-000000000000",
      "version": [1, 0, 0]
    },
    {
      "type": "script",
      "language": "javascript",
      "entry": "scripts/main.js",
      "uuid": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      "version": [1, 0, 0]
    }
  ],
  "dependencies": [
    { "module_name": "@minecraft/server", "version": "2.10.0" }
  ]
}
```

Разбор:

- `type: "script"` — включает выполнение JS.
- `language: "javascript"` — обязательное поле.
- `entry` — путь к точке входа относительно корня пака поведения.
- `dependencies[].module_name` — имя модуля движка.
- `dependencies[].version` — версия модуля (без `beta`, если не нужен бета-API).

## Актуальные версии модулей

- `@minecraft/server` — стабильная `2.10.0`, бета `2.13.0-beta`.
- `@minecraft/server-ui` — стабильная `2.2.0`, бета `2.5.0-beta`.
- `@minecraft/server-admin` — только бета, `1.0.0-beta` (только сервер).
- `@minecraft/server-net` — только бета, `1.0.0-beta` (только сервер).
- `@minecraft/server-gametest` — только бета, `1.0.0-beta` (только сервер).

## Импорт API

```javascript
import { world, system, MinecraftDimensionTypes } from "@minecraft/server";
import { ActionFormData } from "@minecraft/server-ui";
```

- `world` — объект мира: игроки, измерения, сущности, счёт, события.
- `system` — системные события и планировщик задач.
- `MinecraftDimensionTypes` — константы измерений (`overworld`, `nether`,
  `the_end`).

## Основные объекты

- `world.getPlayers()` — список игроков.
- `world.getDimension("overworld")` — измерение.
- `world.sendMessage(text)` — сообщение в чат всем.
- `world.setDynamicProperty(key, value)` — сохранить данные мира.
- `world.getDynamicProperty(key)` — прочитать данные мира.
- `world.scoreboard` — табло счёта.
- `system.run(callback)` — выполнить в следующем тике.
- `system.runInterval(callback, ticks)` — повторять каждые N тиков.
- `system.runTimeout(callback, ticks)` — выполнить один раз через N тиков.
- `system.clearRun(handle)` — отменить задачу.

## Три контекста выполнения (важно!)

В Bedrock есть три режима выполнения кода, и **не всё можно делать в любом
из них**:

- **Early execution** — на самом старте мира, до полной загрузки.
  Здесь можно регистрировать команды и события.
- **Before events** (`world.beforeEvents`, `system.beforeEvents`) —
  события «до» изменения. В них **нельзя** изменять мир напрямую
  (менять блоки/сущности) — только читать и решать, отменять ли событие.
- **After events** (`world.afterEvents`) — события «после» изменения.
  Здесь можно менять мир.

Правило: если нужно изменить мир в ответ на `before`-событие, отложите
изменение через `system.run(...)`.

```javascript
world.beforeEvents.entityHurt.subscribe((event) => {
  event.cancel = true; // можно отменить урон
  system.run(() => {
    // изменение мира — только в system.run
    event.hurtEntity.sendMessage("Урон отменён");
  });
});
```

## События мира (`world.afterEvents`)

Основные события после изменения (официальные имена):

- `playerJoin` — игрок вошёл.
- `playerLeave` — игрок вышел.
- `playerSpawn` — игрок появился.
- `entitySpawn` — сущность появилась.
- `entityDie` — сущность погибла.
- `entityHurt` — сущность получила урон.
- `entityHeal` — сущность исцелена.
- `entityHitEntity` — сущность ударила сущность.
- `entityHitBlock` — сущность ударила блок.
- `playerBreakBlock` — игрок сломал блок.
- `playerPlaceBlock` — игрок поставил блок.
- `playerInteractWithBlock` — игрок взаимодействовал с блоком.
- `playerInteractWithEntity` — игрок взаимодействовал с сущностью.
- `itemUse` — предмет использован.
- `itemUseOn` — предмет применён к блоку.
- `explosion` — взрыв.
- `weatherChange` — смена погоды.
- `dataDrivenEntityTrigger` — сработал событие сущности из данных.
- `effectAdd` — добавлен эффект.
- `worldLoad` — мир загружен.

События «до» (`world.beforeEvents`): `entityHurt`, `entityHeal`,
`playerBreakBlock`, `itemUse`, `explosion`, `effectAdd`, `entityRemove`,
`entityTamed`.

## События системы (`system.afterEvents`)

- `scriptEventReceive` — принято сообщение `/scriptevent` (см. ниже).
- `startup` — система запущена.
- `shutdown` — система останавливается.

События «до» (`system.beforeEvents`): `startup` — используется для
регистрации команд (`customCommandRegistry`).

## Проверка версии и совместимость

- `@minecraft/server` до версии `2.x` имел другой API. Код под `1.x`
  может не работать под `2.10.0`.
- Стабильный API не требует экспериментальных флагов.
- Бета-API требует включения «Beta APIs» в мире.

## Хранение данных

- `world.setDynamicProperty("key", value)` — данные уровня мира.
- `entity.setDynamicProperty(...)` — данные сущности.
- `player.setDynamicProperty(...)` — данные игрока.
- Значения: строка, число, булево. Для объектов используйте JSON:

```javascript
world.setDynamicProperty("my_config", JSON.stringify({ hp: 20 }));
const cfg = JSON.parse(world.getDynamicProperty("my_config") ?? "{}");
```

## Таймеры

```javascript
const handle = system.runInterval(() => {
  for (const p of world.getPlayers()) {
    p.onScreenDisplay.setActionBar("Тик!");
  }
}, 20); // раз в секунду (20 тиков = 1 секунда)

// отменить:
system.clearRun(handle);
```

## `scriptevent` — приём команд от `/scriptevent`

```javascript
import { system, world } from "@minecraft/server";

system.afterEvents.scriptEventReceive.subscribe((event) => {
  if (event.id === "my_ns:spawn_zombie") {
    const { x, y, z } = event.sourceEntity?.location ?? { x: 0, y: 0, z: 0 };
    event.sourceEntity?.dimension.spawnEntity("minecraft:zombie", { x, y, z });
  }
});
```

- `event.id` — идентификатор сообщения.
- `event.message` — данные сообщения.
- `event.sourceEntity` — сущность-источник (если есть).

## Своя команда через скрипты

Регистрация команды делается **только** в `system.beforeEvents.startup`:

```javascript
import { system, CommandPermissionLevel, CustomCommandParamType,
         CustomCommandStatus } from "@minecraft/server";

system.beforeEvents.startup.subscribe((init) => {
  init.customCommandRegistry.registerCommand(
    {
      name: "my_ns:heal",
      description: "Исцелить игрока",
      permissionLevel: CommandPermissionLevel.GameDirectors,
      optionalParameters: [
        { name: "target", type: CustomCommandParamType.PlayerSelector }
      ]
    },
    (origin, target) => {
      const list = target?.length ? target : [origin.sourceEntity];
      for (const p of list) p.runCommand("effect @s instant_health 1 10 true");
      return { status: CustomCommandStatus.Success };
    }
  );
});
```

- `name` — имя команды (лучше с пространством имён).
- `permissionLevel` — `Any` | `GameDirectors` | `Admin` | `Host` | `Owner`.
- `optionalParameters` / `mandatoryParameters` — параметры.
- `CustomCommandParamType` — типы: `Boolean`, `Integer`, `Float`, `String`,
  `PlayerSelector`, `EntitySelector`, `BlockType`, `ItemType`, `Location`,
  `Enum`.
- `callback(origin, ...args)` — обработчик, первый аргумент `origin` с
  `sourceEntity`.
- Возвращает `{ status: CustomCommandStatus.Success }` (или `Fail`).

## Отладка

- Ошибки скриптов печатаются в чат и в журнал содержимого (Content Log).
- Включите Content Log в настройках, чтобы видеть вывод.
- `console.warn("...")` пишет в лог.
- Команда `/script` даёт отладочные опции (например, перезапуск скрипта).
- `/reload` перезагружает функции и скрипты из паков поведения.

## Частые ошибки

- **Регистрация команды в `afterEvents`** — нельзя, только в
  `beforeEvents.startup`.
- **Изменение мира в `before`-событии** — нельзя, откладывайте через
  `system.run(...)`.
- **Не объявлен `dependencies`** — `import` не сработает, скрипт не
  запустится.
- **Версия модуля с `beta`** — потребуется флаг «Beta APIs» в мире.
- **`entry` указывает не на тот файл** — скрипт молча не выполнится.
- **Ожидание синхронного результата формы** — `form.show()` возвращает
  `Promise`, работайте через `.then(...)` или `await`.
- **Данные между перезапусками не сохраняются** — используйте
  `setDynamicProperty`.
