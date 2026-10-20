# Проверка аддона Bedrock перед сборкой

Аддон легко «собрать» и так же легко получить паки, которые игра молча
игнорирует. Перед упаковкой в `.mcaddon` прогоняйте аддон через проверки —
это дешевле, чем искать причину в игре.

> Источники (официальные):
> - Схемы и примеры Mojang: `https://github.com/Mojang/bedrock-samples`
> - Схемы форм/команд/UI: `https://github.com/MicrosoftDocs/minecraft-creator`
> - Типы Script API: `https://unpkg.com/@minecraft/server@<версия>/index.d.ts`

## Чек-лист манифеста

- `format_version` — **целое число** `2`, не строка.
- `header.name`, `header.description`, `header.uuid`, `header.version`,
  `header.min_engine_version` — все на месте.
- `header.version` и `header.min_engine_version` — **массивы чисел**
  (`[1, 0, 0]`, `[1, 26, 50]`), а не строки.
- `header.uuid` и UUID каждого модуля — **разные** и в формате
  `8-4-4-4-12` только из символов `0-9a-f` (буквы `g`–`z` недопустимы!).
- `modules[].type` — `data` (BP), `resources` (RP) или `script`.
- Script-модуль обязан иметь `language: "javascript"` и `entry`
  (например `scripts/main.js`), и файл по этому пути должен существовать.
- Зависимость на API — `{ "module_name": "@minecraft/server",
  "version": "2.10.0" }`. Без `beta` — стабильный API; с `beta` — нужен
  флаг «Beta APIs» в мире.

## Чек-лист предмета

- Корень — `minecraft:item`, внутри `description` и `components`.
- `description.identifier` — вида `namespace:name`.
- `description.menu_category.category` — категория в креативе.
- Перевод — `minecraft:display_name.value` (ключ вида
  `item.mystic.amulet.name`), а не поле `translation`.
- Иконка — `minecraft:icon.textures.default` = имя записи из
  `textures/item_texture.json`.
- `format_version` — `1.21.10` и выше (актуальные — `1.26.x`).

## Чек-лист ресурсов

- `textures/item_texture.json` → все указанные текстуры существуют как
  `.png` в `resource_pack/textures/`.
- Для каждого ключа `display_name` есть строка в `texts/*.lang`
  (`ru_RU.lang`, `en_US.lang`).
- Есть `pack_icon.png` в каждом паке (не обязательно, но желательно).

## Чек-лист скриптов

- Импорты только из объявленных в манифесте модулей.
- События: `event.itemStack` (а не `getItem()`), `event.source` уже типа
  `Player`.
- Здоровье — `getComponent("minecraft:health")` (`EntityHealthComponent`),
  чтение `currentValue`/`effectiveMax`, запись `setCurrentValue(...)`.
- Свои команды — только в `system.beforeEvents.startup`, через
  `init.customCommandRegistry.registerCommand(...)`.

## Чек-лист упаковки `.mcaddon`

- `.mcaddon` — это ZIP; внутри папки паков (например `my_bp/`, `my_rp/`),
  а в каждой — `manifest.json` в корне.
- Если в архиве лежат `behavior_packs/` и `resource_packs/` — тоже верно.
- Порядок и включение паков задаёт пользователь в настройках мира.

## Правило проверки UUID

Регулярное выражение для допустимого UUID:

```
^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
```

Если «UUID» содержит символы вне `0-9a-f` — игра пак не примет.

## Частые ошибки

- `format_version: "2.0.0"` (строка) вместо `2` (число).
- UUID с буквами `g`–`z` — не hex.
- Script-модуль без `entry`/`language` — скрипты не грузятся.
- `dependencies` ссылается на несуществующий UUID вместо
  `@minecraft/server`.
- Предмет без корня `minecraft:item`.
- Текстура указана, но `.png` нет — в игре фиолетово-чёрный квадрат.
- Одинаковые UUID у BP и RP — паки конфликтуют.
- Ключ локализации не найден в `.lang` — в игре показывается сырой ключ.

## Порядок работы

1. Проверить манифесты (формат, версии, UUID, модули).
2. Проверить контент (предметы/блоки: корень и обязательные поля).
3. Проверить ресурсы (текстуры, локализация).
4. Проверить скрипты (импорты, события, API).
5. Собрать ZIP и убедиться в правильной структуре.
6. Загрузить в игру и включить журнал содержимого (Content Log).
