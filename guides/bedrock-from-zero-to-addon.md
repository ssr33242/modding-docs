# Bedrock Edition — аддоны от нуля до `.mcaddon`

Bedrock Edition (мобильные устройства, консоли, Windows 10/11 Bedrock) не поддерживает
Java-моды. Вместо них — **аддоны**: наборы данных и скриптов, которые игра подхватывает
без правки кода.

## Что такое аддон

Аддон — это один или два пакета:

- **Resource Pack** (`resource_packs`) — графика и звук: текстуры, модели, анимации,
  звуки, шрифты, UI, языковые файлы.
- **Behavior Pack** (`behavior_packs`) — логика: новые предметы, блоки, сущности,
  рецепты, лут-таблицы, спавн-правила, события.
- **Script API** (`@minecraft/server`) — JavaScript для сложного поведения.

Упаковка:

- `.mcpack` — один пакет (только ресурсы или только поведение).
- `.mcaddon` — zip с обоими пакетами (и ресурсным, и поведенческим).
- `.mctemplate` — шаблон мира со встроенными пакетами.

## Структура аддона

```
my_addon/
├── behavior_packs/
│   └── my_bp/
│       ├── manifest.json
│       ├── pack_icon.png
│       ├── entities/
│       ├── items/
│       ├── blocks/
│       ├── recipes/
│       ├── loot_tables/
│       ├── spawn_rules/
│       └── scripts/          (если используется Script API)
└── resource_packs/
    └── my_rp/
        ├── manifest.json
        ├── pack_icon.png
        ├── textures/
        ├── models/
        ├── sounds/
        ├── texts/
        └── font/
```

## `manifest.json` — обязательный файл

Ключевые поля:

- `format_version` — версия формата манифеста (например `2`).
- `header.name` — название пакета.
- `header.description` — описание.
- `header.uuid` — **уникальный** UUID пакета (обязательно).
- `header.version` — версия пакета, массив `[1, 0, 0]`.
- `header.min_engine_version` — минимальная версия игры, массив `[1, 21, 0]`.
- `modules` — список модулей:
  - `type: "data"` — поведенческий пакет;
  - `type: "resources"` — ресурсный пакет;
  - `type: "script"` — скриптовый модуль (с `language: "javascript"` и точкой входа).
  - `uuid` — **другой** UUID, уникальный для модуля.
- `dependencies` — зависимости между пакетами и от версий `@minecraft/server`.

**Важно:** UUID должны быть уникальными и разными для header и modules. Генерировать
любым UUID-генератором (в Python: `python -c "import uuid; print(uuid.uuid4())"`).

## Минимальные примеры контента

- **Предмет** — `items/my_item.json` с компонентами (`minecraft:icon`, `minecraft:max_stack_size`).
- **Блок** — `blocks/my_block.json` + текстуры и `terrain_texture.json` в ресурс-паке.
- **Сущность** — `entities/my_entity.json` (поведение) + модель и текстуры (ресурсы).
- **Рецепт** — `recipes/my_recipe.json` (формат `minecraft:recipe_shaped` или `_shapeless`).
- **Лут-таблица** — `loot_tables/entities/my_entity.json`.

## Script API (JavaScript)

- Подключается как модуль `type: "script"` в `manifest.json`.
- Зависимость от `@minecraft/server` объявляется в `dependencies` с нужной версией
  (например `"1.11.0"` или `"1.17.0"` — зависит от версии игры).
- Точка входа — JS-файл, например `scripts/main.js`:
  ```js
  import { world, system } from "@minecraft/server";
  world.afterEvents.playerSpawn.subscribe((ev) => {
      ev.player.sendMessage("Добро пожаловать!");
  });
  ```
- Доступные модули: `@minecraft/server`, `@minecraft/server-ui`, `@minecraft/server-admin`,
  `@minecraft/server-gametest`.

## Сборка и установка аддона

1. Собрать папки `behavior_packs/my_bp` и `resource_packs/my_rp`.
2. Упаковать **содержимое** (не саму папку) в zip.
3. Переименовать zip в `.mcaddon` (оба пакета) или `.mcpack` (один).
4. Открыть файл — игра сама импортирует пакеты.
5. Применить в мире: «Настройки мира» → «Наборы ресурсов» / «Наборы поведения».
6. Включить экспериментальные функции, если аддон их использует (Script API, новые
   блоки/предметы иногда требуют).

## Как тестировать

- **Windows**: положить распакованные пакеты в
  `%LOCALAPPDATA%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\development_behavior_packs\`
  и `...development_resource_packs\`, затем включить их в мире. Так правки видны без
  переустановки.
- Смотреть лог: «Настройки» → «Создатель» → «Логи контента».
- Для скриптов — включить «Beta APIs» в экспериментальных настройках мира.

## Частые ошибки

- **Пакет не виден в игре** — неверный `manifest.json` (битый JSON, нет `uuid`,
  нет `modules`).
- **Ошибка «duplicate uuid»** — тот же UUID у header и module или у двух пакетов.
- **Текстуры не применяются** — перепутаны местами resource/behavior pack или
  отсутствует `terrain_texture.json`/`item_texture.json`.
- **Скрипт не запускается** — не включены Beta APIs, неверная версия `@minecraft/server`
  в `dependencies`, или модуль `type: "script"` не объявлен.
- **`.mcaddon` не импортируется** — в zip попала лишняя вложенная папка; упаковывать
  надо содержимое пакета, а не папку верхнего уровня.
- **Мир не грузится** — аддон использует `min_engine_version` выше версии игры.

## Репозитории и площадки аддонов

См. `guides/bedrock-repos.md` — там список площадок (MCPEDL, CurseForge, GitHub),
инструментов (Bridge., Blockbench, Amethyst) и официальные примеры от Mojang.
