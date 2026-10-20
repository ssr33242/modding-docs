# Структура аддона Bedrock Edition

Аддон (Add-On) для Bedrock Edition — это набор из двух паков: **пак поведения**
(behavior pack, BP) и **пак ресурсов** (resource pack, RP). Аддон может
содержать только один из них, но для полноценного контента обычно нужны оба.

> Источники (официальные):
> - Официальные примеры Mojang: `https://github.com/Mojang/bedrock-samples`
> - Официальная документация и схемы:
>   `https://github.com/MicrosoftDocs/minecraft-creator` (папка `content/forms`)
> - Официальный портал: `https://learn.microsoft.com/minecraft/creator`
> - Версия игры берётся из `version.json` в `Mojang/bedrock-samples`.

## Актуальная версия Bedrock

- **Последняя версия:** `1.26.50.4` (от 15.09.2026).
- В манифесте это записывается как `min_engine_version`: `[1, 26, 50]`.
- Версия формата (`format_version`) и версия движка (`min_engine_version`) —
  это **разные** вещи. `format_version` задаёт формат конкретного файла,
  `min_engine_version` — минимальную версию игры.

## Структура паков на диске

Пак поведения:

- `behavior_pack/manifest.json` — обязательный манифест пака.
- `behavior_pack/pack_icon.png` — иконка пака (необязательно).
- `behavior_pack/entities/` — определения сущностей (`*.json`).
- `behavior_pack/blocks/` — определения блоков.
- `behavior_pack/items/` — определения предметов.
- `behavior_pack/recipes/` — рецепты (`recipe_shaped`, `recipe_shapeless`).
- `behavior_pack/loot_tables/` — таблицы добычи.
- `behavior_pack/functions/` — файлы функций (`*.mcfunction`).
- `behavior_pack/dialogue/` — диалоги NPC (сцены меню).
- `behavior_pack/scripts/` — JavaScript-скрипты (`*.js`), не компилируются.
- `behavior_pack/spawn_rules/` — правила появления мобов.
- `behavior_pack/trading/` — торговые таблицы.

Пак ресурсов:

- `resource_pack/manifest.json` — обязательный манифест пака.
- `resource_pack/textures/` — текстуры (`*.png`), обычно в подпапках
  `items/`, `blocks/`, `entity/`.
- `resource_pack/texts/` — файлы локализации:
  - `en_US.lang` — английский,
  - `ru_RU.lang` — русский.
- `resource_pack/sounds/` — звуки (`sound_definitions.json`).
- `resource_pack/models/` — модели сущностей.
- `resource_pack/entity/` — клиентские определения сущностей
  (`*.entity.json`).
- `resource_pack/ui/` — JSON UI (экраны, элементы). Список файлов UI
  объявляется в `_ui_defs.json`.
- `resource_pack/font/` — шрифты.

## Манифест пака поведения

Официальный пример из `Mojang/bedrock-samples`, файл
`behavior_pack/manifest.json`:

```json
{
  "format_version": 2,
  "header": {
    "description": "Example vanilla behavior pack",
    "name": "Vanilla Behavior Pack",
    "uuid": "ee649bcf-256c-4013-9068-6a802b89d756",
    "version": [0, 0, 1],
    "min_engine_version": [1, 26, 50]
  },
  "modules": [
    {
      "description": "Example vanilla behavior pack",
      "type": "data",
      "uuid": "fa6e90c8-c925-460f-8155-c8a60b753caa",
      "version": [0, 0, 1]
    }
  ],
  "dependencies": [
    {
      "uuid": "66c6e9a8-3093-462a-9c36-dbb052165822",
      "version": [0, 0, 1]
    }
  ]
}
```

Разбор полей манифеста:

- `format_version` — версия формата манифеста. Сейчас `2`.
- `header.name` — название пака (видно в игре).
- `header.description` — описание пака.
- `header.uuid` — **уникальный** UUID пака. Для каждого пака свой.
- `header.version` — версия пака в виде `[мажор, минор, патч]`.
- `header.min_engine_version` — минимальная версия игры: `[1, 26, 50]`.
- `modules[].type` — тип модуля: `data` (пак поведения) или `resources`
  (пак ресурсов).
- `modules[].uuid` — UUID модуля (отдельный от UUID пака).
- `dependencies` — зависимости от других паков (например, от
  `@minecraft/server` для скриптов).

## Манифест пака ресурсов

- Отличия от пака поведения — только тип модуля:
  `"type": "resources"`.
- UUID пака и UUID модуля должны быть уникальными.
- Если пак ресурсов должен подключаться к паку поведения, их можно связать
  через `dependencies`: в RP указать UUID BP или наоборот.

## Как получить UUID

- UUID — это 128-битный идентификатор вида
  `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`.
- Можно сгенерировать любым генератором UUID (официального требования к
  конкретному генератору нет).
- **Каждый пак и каждый модуль должен иметь собственный UUID.**
  Дубликат UUID у двух паков приведёт к конфликту.

## Зависимость от скриптового API

Чтобы использовать `@minecraft/server`, в манифесте BP нужно объявить модуль
`script` и зависимость на нужный модуль движка:

```json
{
  "format_version": 2,
  "header": {
    "name": "My Scripted Add-On",
    "description": "Add-on with scripts",
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
    {
      "module_name": "@minecraft/server",
      "version": "2.10.0"
    }
  ]
}
```

Разбор:

- `modules[].type = "script"` — включает выполнение JS.
- `modules[].entry` — путь к точке входа относительно корня BP.
- `modules[].language = "javascript"` — обязательное поле для script-модуля.
- `dependencies[].module_name` — имя модуля (`@minecraft/server`,
  `@minecraft/server-ui` и т.д.).
- `dependencies[].version` — версия модуля **без** префикса `beta`, если
  нужен стабильный API.

## Стабильный API и бета-API

- **Стабильный** API доступен всегда, версия вида `2.10.0`.
- **Бета** API включается экспериментальным флагом в мире («Beta APIs»),
  версия вида `2.13.0-beta`.
- Если объявить в манифесте `"version": "2.13.0-beta"`, то аддон **потребует**
  включения бета-API в мире, иначе скрипты не загрузятся.
- Актуальные версии модулей (проверять на npm):

  - `@minecraft/server` — стабильная `2.10.0`, бета `2.13.0-beta`.
  - `@minecraft/server-ui` — стабильная `2.2.0`, бета `2.5.0-beta`.
  - `@minecraft/server-admin` — только бета, `1.0.0-beta`.
  - `@minecraft/server-net` — только бета, `1.0.0-beta`.
  - `@minecraft/server-gametest` — только бета, `1.0.0-beta`.

> `server-admin`, `server-net` и `server-gametest` работают **только** на
> выделенном сервере (dedicated server), не в одиночной игре.

## Версии модулей движка в манифесте

- Версия модуля в `dependencies` — это **версия скриптового API**, а не
  версия Minecraft.
- Часть версии после последней точки может быть beta/rc. Для стабильного
  релиза указывают точную версию (например, `2.10.0`).
- Официальный способ обновить — посмотреть последнюю версию на npm:
  `https://registry.npmjs.org/@minecraft/server` и взять поле
  `dist-tags.latest`.

## Как собрать `.mcaddon`

- `.mcaddon` — это ZIP-архив, в котором лежат папки BP и/или RP.
- Внутри архива должны быть **папки паков** (например, `my_behavior_pack/`
  и `my_resource_pack/`), а внутри каждой — `manifest.json`.
- Порядок загрузки и подключения задаёт пользователь в настройках мира.
- Переименовать `*.zip` в `*.mcaddon` недостаточно: важно, чтобы структура
  внутри была правильной (манифесты на верхнем уровне папок паков).

## Типичные ошибки

- **Дубликат UUID** у двух паков — игра считает их одним и ломает загрузку.
- **Забыт `pack_icon.png`** — не критично, но пак будет без иконки.
- **`min_engine_version` выше версии игры** — пак не загрузится.
- **Нет `dependencies` на `@minecraft/server`** — скрипты не выполнятся.
- **`entry` указывает на несуществующий файл** — скрипт молча не запустится,
  ищите ошибку в консоли мира (включите «Content Log»).
- **`format_version` в файлах контента выше, чем поддерживает игра** —
  файл игнорируется.

## Где смотреть ошибки

- Включите в настройках игры вывод журнала содержимого (Content Log).
- На выделенном сервере журнал пишется в файл консоли сервера.
- Ошибки скриптов видны в чате/логе как сообщения с префиксом
  `[Scripting]`.

## Полезные официальные примеры

В репозитории `Mojang/bedrock-samples` целиком лежит ванильный пак поведения
и пак ресурсов — это лучший источник реальных рабочих примеров:

- `behavior_pack/entities/`, `blocks/`, `items/`, `recipes/`,
  `loot_tables/`, `spawn_rules/`, `trading/`.
- `resource_pack/` — текстуры, модели, звуки, локализация.

Разбирать реальные примеры из этого репозитория полезнее, чем писать контент
с нуля: структура и значения полей там заведомо корректные для текущей
версии.
