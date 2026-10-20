# Команды Bedrock Edition (через `/`)

Команды в Bedrock Edition вводятся в чате с ведущим слешем: `/give`, `/tp`,
`/setblock` и так далее. У каждой команды есть **уровень разрешений**
(permission level) и признак «требует читов» (requires cheats).

> Источники (официальные):
> - Схемы команд Mojang/Microsoft:
>   `https://github.com/MicrosoftDocs/minecraft-creator`
>   (папка `content/forms/command/*.form.json`)
> - Официальные описания популярных команд:
>   `https://learn.microsoft.com/minecraft/creator/documents/commandspopularcommands`
> - Вводная по командам и селекторам:
>   `https://learn.microsoft.com/minecraft/creator/documents/commandsintroduction`

## Что такое уровень разрешений

- `0` — доступно всем игрокам.
- `1` — обычный игрок с включёнными читами.
- `2` — оператор (op) или включённые читы в одиночном мире.
- `3` — оператор на выделенном сервере (частичный админ).
- `4` — полный оператор/администратор выделенного сервера.

Чем выше уровень, тем опаснее команда. На выделенном сервере права
настраиваются в `permissions.json`.

## Что значит «требует читов»

- `requiresCheats = true` — команда работает только если в мире включены
  читы (в одиночной игре) или игрок имеет нужные права (на сервере).
- `requiresCheats = false` — команда доступна и без читов.

## Команды уровня 0 (доступны всем)

- `help` — список доступных команд, постранично.
- `list` — список игроков на сервере.
- `me` — сообщение о себе в чат.
- `packstack` — печатает стек паков клиента или сервера.
- `tell` — личное сообщение игроку (то же, что `/msg`, `/w`).

## Команды уровня 1 (игрок с читами)

Это самый большой список — базовые игровые команды:

- `aimassist` — включить/выключить помощь прицеливания (контроллер).
- `camera` — переключить перспективу камеры игрока.
- `camerashake` — тряска камеры игрока (интенсивность, длительность).
- `clear` — очистить инвентарь игрока.
- `clearspawnpoint` — убрать точку возрождения игрока.
- `clone` — копировать блоки из одной области в другую.
- `controlscheme` — задать/сбросить схему управления камерой.
- `damage` — нанести урон сущностям.
- `daylock` — зафиксировать/разблокировать смену дня и ночи.
- `dialogue` — открыть диалог NPC игроку (см. раздел ниже).
- `difficulty` — задать сложность (Peaceful/Easy/Normal/Hard).
- `effect` — добавить или снять эффекты состояния.
- `enchant` — зачаровать предмет в руке.
- `event` — вызвать событие у сущности.
- `execute` — выполнить команду от имени сущностей (важная команда!).
- `fill` — заполнить область блоком.
- `fog` — добавить или убрать туман.
- `function` — выполнить файл функции (`*.mcfunction`).
- `gamemode` — сменить режим игры.
- `gamerule` — прочитать или изменить правило мира.
- `gametest` — управление gametest-тестами (нужен бета-API).
- `give` — выдать предмет игроку.
- `hud` — управление элементами интерфейса (HUD).
- `inputpermission` — вкл/выкл ввод игрока (например, запретить движение).
- `kick` — выгнать игрока с сервера.
- `kill` — убить сущности (игроков, мобов).
- `locate` — найти ближайший биом или структуру.
- `loot` — выдать добычу из таблицы лута в инвентарь или в мир.
- `mobevent` — управлять событиями мобов.
- `music` — управлять проигрыванием музыкальных треков.
- `particle` — создать источник частиц.
- `place` — разместить структуру/фичу/правило фичи.
- `playanimation` — проиграть одноразовую анимацию сущности.
- `playsound` — проиграть звук.
- `project` — инструменты редактора проекта (только режим Editor).
- `recipe` — разблокировать встроенные рецепты игроку.
- `replaceitem` — заменить предметы в инвентарях.
- `ride` — посадить сущности друг на друга или снять.
- `say` — сообщение в чат от имени мира/сервера.
- `schedule` — запланировать действие по времени или загрузке области.
- `scoreboard` — табло счёта (объективы, команды, игроки).
- `scriptevent` — отправить событие в скрипты (см. раздел ниже).
- `setblock` — заменить блок.
- `setworldspawn` — задать точку появления мира.
- `spawnpoint` — задать точку возрождения игрока.
- `spreadplayers` — раскидать сущности по случайным местам.
- `stopsound` — остановить звук.
- `structure` — сохранить или загрузить структуру.
- `summon` — призвать сущность.
- `tag` — управлять тегами сущностей.
- `teleport` — телепортировать сущности (то же, что `/tp`).
- `tellraw` — отправить JSON-сообщение игрокам (интерактивный текст).
- `testfor` — посчитать сущности по условию.
- `testforblock` — проверить блок в позиции.
- `testforblocks` — сравнить две области блоков.
- `tickingarea` — управлять ticking-area (постоянно загруженные области).
- `time` — прочитать или изменить игровое время.
- `title` — заголовок на экране обычным текстом.
- `titleraw` — заголовок на экране JSON-сообщением.
- `toggledownfall` — переключить погоду.
- `weather` — задать погоду.
- `xp` — добавить или отнять опыт игрока.

## Команды уровня 2 (оператор / читы)

- `deop` — снять статус оператора.
- `op` — выдать статус оператора.
- `place` (в отдельных сборках) — размещение структур.
- `reload` — перезагрузить все функции и скрипты из паков поведения.
- `script` — отладочные опции скриптов.
- `wsserver` — подключиться к websocket-серверу.

## Команды уровня 3

- `setmaxplayers` — задать максимум игроков в сессии.

## Команды уровня 4 (админ выделенного сервера)

- `allowlist` — управление списком разрешённых игроков.
- `changesetting` — изменить настройку работающего сервера.
- `permission` — перезагрузить и применить права.
- `reloadconfig` — перезагрузить конфиги (переменные, секреты, права).
- `reloadpacketlimitconfig` — перезагрузить лимиты пакетов из файла.
- `save` — управлять сохранением данных на диск.
- `sendshowstoreoffer` — открыть страницу магазина (Marketplace).
- `stop` — остановить сервер.
- `transfer` — перевести игрока на другой сервер.

## Команда `execute` — выполнить от имени сущности

`/execute` — одна из важнейших команд, позволяет применять другие команды
через контекст сущности или позиции.

- `/execute as <селектор> run <команда>` — выполнить от имени сущностей.
- `/execute at <селектор> run <команда>` — выполнить в позиции сущностей.
- `/execute positioned <x y z> run <команда>` — выполнить в позиции.
- `/execute if <условие> run <команда>` — выполнить, если условие истинно.
- `/execute unless <условие> run <команда>` — выполнить, если ложно.

Пример: нанести урон всем зомби в радиусе 10 блоков:

```
/execute as @e[type=zombie,r=10] run damage @s 5
```

## Селекторы целей

- `@p` — ближайший игрок.
- `@r` — случайный игрок.
- `@a` — все игроки.
- `@e` — все сущности.
- `@s` — сущность, от имени которой выполняется команда.
- `@e[type=zombie]` — все зомби.
- `@e[type=zombie,r=10]` — зомби в радиусе 10 блоков.
- `@a[name=Steve]` — конкретный игрок.
- `@e[tag=myTag]` — сущности с тегом.

## Команда `scriptevent` — мост между командами и скриптами

`/scriptevent` отправляет событие в скрипты (`@minecraft/server`). Это
официальный способ связать команды и JavaScript-код.

- Синтаксис: `/scriptevent <messageId> <message>`
- `messageId` — идентификатор события (задаёте сами).
- `message` — данные события (до 2048 символов).
- Доступна с версии `1.20.30`.
- Уровень разрешений `1`, требует читов.

Пример команды:

```
/scriptevent my_namespace:heal_player Steve
```

Пример обработчика в скрипте BP (`scripts/main.js`):

```javascript
import { system, world } from "@minecraft/server";

system.afterEvents.scriptEventReceive.subscribe((event) => {
  if (event.id === "my_namespace:heal_player") {
    const playerName = event.message;
    const player = world.getPlayers({ name: playerName })[0];
    if (player) {
      player.runCommand("effect @s instant_health 1 10 true");
    }
  }
});
```

Разбор:

- `scriptEventReceive` — официальное событие приёма `scriptevent`.
- `event.id` — идентификатор сообщения (`messageId`).
- `event.message` — данные после идентификатора.
- Обработчик должен быть подписан до срабатывания события.

## Команда `dialogue` — открыть меню NPC

Команда `/dialogue` открывает диалоговое меню NPC игроку.

- Перегрузка 1: `/dialogue open <npc> <player> [sceneName]`
  - `npc` — селектор сущности типа NPC.
  - `player` — имя или селектор игрока.
  - `sceneName` — необязательное имя сцены из пака поведения.
- Перегрузка 2: `/dialogue change <npc> <sceneName> [players]`
  - меняет сцену у NPC.
- Доступна с версии `1.20.80` (диалоговые документы).

Пример:

```
/dialogue open @e[type=npc,c=1] @p my_scene
```

Сцена задаётся в файле диалога (см. документ про меню и формы).

## Файлы функций (`*.mcfunction`)

- Функция — это файл с расширением `.mcfunction` в папке
  `behavior_pack/functions/`.
- Внутри — по одной команде на строку, **без** ведущего слеша.
- Запуск: `/function <namespace>/<file>` (или `/function file` внутри папки).

Пример `behavior_pack/functions/demo/heal.mcfunction`:

```
effect @s instant_health 1 10 true
say Вы исцелены!
```

Запуск:

```
/function demo/heal
```

- В `functions` можно объявлять теги: файл `functions/tick.json` запускает
  функцию каждый тик.
- `functions/load.json` — при загрузке мира.

## Своя команда через скрипты (custom command)

Bedrock позволяет зарегистрировать **собственную** команду через
`@minecraft/server` — это `customCommandRegistry`. Такая команда появится в
списке автодополнения при вводе `/`.

Официальная точка входа — `system.beforeEvents.startup`:

```javascript
import { system, CommandPermissionLevel, CustomCommandParamType,
         CustomCommandStatus } from "@minecraft/server";

system.beforeEvents.startup.subscribe((initEvent) => {
  initEvent.customCommandRegistry.registerCommand(
    {
      name: "my_namespace:heal",
      description: "Исцелить игрока",
      permissionLevel: CommandPermissionLevel.GameDirectors,
      optionalParameters: [
        { name: "target", type: CustomCommandParamType.PlayerSelector }
      ]
    },
    (origin, target) => {
      const players = target && target.length
        ? target
        : [origin.sourceEntity];
      for (const p of players) {
        p.runCommand("effect @s instant_health 1 10 true");
      }
      return { status: CustomCommandStatus.Success };
    }
  );
});
```

Разбор ключевых частей:

- `system.beforeEvents.startup` — событие, в котором **можно** регистрировать
  команды. В `afterEvents` регистрировать нельзя.
- `customCommandRegistry.registerCommand(definition, callback)` — добавляет
  команду.
- `name` — имя команды. Рекомендуется с пространством имён
  (`namespace:name`); без него команда попадёт в общий список.
- `description` — описание в подсказке.
- `permissionLevel` — уровень прав команды (см. перечисление ниже).
- `optionalParameters` / `mandatoryParameters` — параметры команды.
- `callback(origin, ...args)` — обработчик. Первый аргумент — `origin` с
  полем `sourceEntity`.
- Возвращать нужно объект со `status` (`CustomCommandStatus.Success` или
  `Fail`).

Уровни прав команды (`CommandPermissionLevel`):

- `Any` — все игроки.
- `GameDirectors` — операторы/режиссёры игры.
- `Admin` — администраторы.
- `Host` — хост мира.
- `Owner` — владелец.

Типы параметров (`CustomCommandParamType`):

- `Boolean`, `Integer`, `Float`, `String`.
- `PlayerSelector` — селектор игроков.
- `EntitySelector` — селектор сущностей.
- `BlockType`, `ItemType`, `Location`.
- `Enum` — перечисление (список допустимых значений).

Пример с обязательным и необязательным параметрами:

```javascript
initEvent.customCommandRegistry.registerCommand(
  {
    name: "my_namespace:give_gold",
    description: "Выдать золото",
    permissionLevel: CommandPermissionLevel.GameDirectors,
    mandatoryParameters: [
      { name: "target", type: CustomCommandParamType.PlayerSelector }
    ],
    optionalParameters: [
      { name: "count", type: CustomCommandParamType.Integer }
    ]
  },
  (origin, target, count) => {
    const n = count ?? 1;
    for (const p of target) {
      p.runCommand(`give @s gold_ingot ${n}`);
    }
    return { status: CustomCommandStatus.Success };
  }
);
```

Использование в чате:

```
/my_namespace:give_gold @p 5
```

## Правила работы с командами

- **Проверяйте уровень разрешений**: команда уровня 4 не сработает в
  одиночном мире с обычными правами.
- **`requiresCheats`** определяет, нужны ли читы в мире — без них команды
  уровня 1 не сработают.
- Свои команды регистрируйте **только** в `system.beforeEvents.startup`.
- Для связи команд и скриптов используйте `scriptevent` или custom command —
  это официальные механизмы, а не «взлом чата».
- Имена команд и сообщений `scriptevent` делайте с пространством имён, чтобы
  не конфликтовать с другими паками.
- Не полагайтесь на память: список команд и их схемы меняются от версии к
  версии — сверяйтесь с `content/forms/command` в официальном репозитории.
