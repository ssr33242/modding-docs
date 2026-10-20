# Меню и формы в Bedrock Edition

В Bedrock Edition есть **три** официальных способа сделать меню:

1. **Скриптовые формы** (`@minecraft/server-ui`) — диалоги из кода. Самый
   простой и надёжный способ.
2. **Диалоги NPC** (`/dialogue`, файлы диалогов) — меню прямо в мире, без
   скриптов.
3. **JSON UI** (пак ресурсов) — полная перерисовка интерфейса. Самый сложный
   способ, нужен только для нестандартных экранов.

> Источники (официальные):
> - Типы API: `https://unpkg.com/@minecraft/server-ui@2.2.0/index.d.ts`
>   (и `@minecraft/server`).
> - Схема диалогов NPC:
>   `https://github.com/MicrosoftDocs/minecraft-creator`
>   (`content/forms/dialogue/dialogue_document.form.json`,
>   `content/forms/command/cmd_dialogue.form.json`).
> - JSON UI: `content/forms/ui/ui_screen.form.json`,
>   `content/forms/ui/ui_element.form.json`, `content/forms/ui/ui_defs.form.json`.

## Часть 1. Скриптовые формы (`@minecraft/server-ui`)

Подключение в манифесте пака поведения:

```json
"dependencies": [
  { "module_name": "@minecraft/server", "version": "2.10.0" },
  { "module_name": "@minecraft/server-ui", "version": "2.2.0" }
]
```

Есть три класса форм:

- `ActionFormData` — список кнопок (меню действий).
- `MessageFormData` — диалог с двумя кнопками (Да/Нет).
- `ModalFormData` — анкета с полями ввода, слайдерами, переключателями.

### ActionFormData — меню из кнопок

Методы класса:

- `.title(text)` — заголовок формы.
- `.body(text)` — текст под заголовком.
- `.button(text, iconPath?)` — добавить кнопку (можно с иконкой).
- `.divider()` — разделитель (в новых версиях API).
- `.header(text)` — заголовок-раздел.
- `.label(text)` — статичный текст.
- `.show(player)` — показать форму игроку, возвращает `Promise`.

Пример меню с обработкой выбора:

```javascript
import { world } from "@minecraft/server";
import { ActionFormData } from "@minecraft/server-ui";

function showMainMenu(player) {
  const form = new ActionFormData()
    .title("Главное меню")
    .body("Выберите действие:")
    .button("Исцелиться", "textures/items/apple")
    .button("Телепорт на спавн")
    .button("Выдать предметы");

  form.show(player).then((response) => {
    if (response.canceled) return; // игрок закрыл форму
    switch (response.selection) {
      case 0:
        player.runCommand("effect @s instant_health 1 10 true");
        break;
      case 1:
        player.runCommand("tp @s 0 100 0");
        break;
      case 2:
        player.runCommand("give @s diamond 64");
        break;
    }
  });
}

world.afterEvents.playerSpawn.subscribe((event) => {
  if (event.initialSpawn) showMainMenu(event.player);
});
```

Разбор:

- `response.canceled` — `true`, если игрок закрыл форму.
- `response.selection` — индекс нажатой кнопки (с нуля).
- Кнопки **нумеруются в порядке добавления**.

### MessageFormData — вопрос с двумя кнопками

Методы:

- `.title(text)`, `.body(text)`.
- `.button1(text)` — первая кнопка.
- `.button2(text)` — вторая кнопка.
- `.show(player)` — показать, вернёт `MessageFormResponse`.

Пример подтверждения:

```javascript
import { MessageFormData } from "@minecraft/server-ui";

function confirmTeleport(player) {
  new MessageFormData()
    .title("Подтверждение")
    .body("Телепортироваться на спавн?")
    .button1("Да")
    .button2("Нет")
    .show(player)
    .then((response) => {
      if (response.canceled) return;
      if (response.selection === 0) {
        player.runCommand("tp @s 0 100 0");
      }
    });
}
```

- `response.selection === 0` — нажата `button1`.
- `response.selection === 1` — нажата `button2`.

### ModalFormData — анкета с полями

Методы-конструкторы:

- `.title(text)` — заголовок.
- `.textField(label, placeholder, options?)` — поле ввода текста.
- `.dropdown(label, items, options?)` — выпадающий список.
- `.slider(label, min, max, options?)` — ползунок.
- `.toggle(label, options?)` — переключатель (вкл/выкл).
- `.submitButton(text)` — текст кнопки отправки.
- `.divider()`, `.header(text)`, `.label(text)` — оформление.
- `.show(player)` — показать, вернёт `ModalFormResponse`.

Пример анкеты:

```javascript
import { ModalFormData } from "@minecraft/server-ui";

function showSettings(player) {
  new ModalFormData()
    .title("Настройки игрока")
    .textField("Ваше имя", "введите имя")
    .dropdown("Команда", ["Красные", "Синие", "Зелёные"])
    .slider("Скорость", 0, 10, { defaultValue: 5 })
    .toggle("Показывать подсказки", { defaultValue: true })
    .submitButton("Сохранить")
    .show(player)
    .then((response) => {
      if (response.canceled) return;
      const [name, team, speed, hints] = response.formValues;
      player.sendMessage(`Имя: ${name}, команда: ${team}, скорость: ${speed}`);
    });
}
```

Разбор `response.formValues`:

- Это массив значений **в порядке добавления элементов**.
- `textField` → `string`.
- `dropdown` → `number` (индекс выбранного пункта).
- `slider` → `number`.
- `toggle` → `boolean`.
- Если игрок закрыл форму, значение может быть `undefined`.

### Обработка ошибок и «игрок занят»

- `show()` может отклониться (`FormRejectReason`):
  `PlayerQuit` (игрок вышел), `ServerShutdown` (сервер остановился),
  `MalformedResponse` (битый ответ клиента).
- `cancelationReason` (`FormCancelationReason`): `UserBusy` (игрок занят —
  открыт чат или другой экран), `UserClosed` (закрыл сам).
- Если форма «не показывается», проверьте `UserBusy`: во время открытого
  чата формы автоматически отменяются.
- В новых версиях API есть `DataDrivenScreenClosedReason` (`ClientClosed`,
  `ServerClosed`, `UserBusy`).

Правило: **всегда** проверяйте `response.canceled` перед чтением данных.

### Вызов формы от имени игрока

- Форму показывает сервер конкретному игроку: `form.show(player)`.
- Нельзя показать форму всем сразу — нужно вызвать для каждого игрока
  в цикле.

## Часть 2. Диалоги NPC (`/dialogue` и файлы диалогов)

Это меню, которое открывается у NPC **без скриптов**. Состоит из файла
диалога и команды `/dialogue`.

### Файл диалога

Официальная структура (из схемы `dialogue_document`):

- `format_version` — версия формата, использовать `1.20.80` и выше.
- `minecraft:npc_dialogue` — корневой объект.
- `minecraft:npc_dialogue.scenes` — массив сцен.
- У каждой сцены: `scene_tag`, необязательный `text`, `npc_name`,
  `buttons`, `commands`.

Файл кладётся в папку `behavior_pack/dialogue/`, например
`dialogue/my_scene.json`:

```json
{
  "format_version": "1.20.80",
  "minecraft:npc_dialogue": {
    "scenes": [
      {
        "scene_tag": "my_scene",
        "npc_name": "Страж",
        "text": "Привет! Что тебе нужно?",
        "buttons": [
          {
            "name": "Исцели меня",
            "commands": [
              "/effect @initiator instant_health 1 10 true"
            ]
          },
          {
            "name": "Дай хлеб",
            "commands": [
              "/give @initiator bread 5"
            ]
          }
        ]
      }
    ]
  }
}
```

Разбор:

- `scene_tag` — имя сцены, по нему её открывает `/dialogue`.
- `npc_name` — имя NPC в заголовке меню.
- `text` — основной текст диалога.
- `buttons[].name` — подпись кнопки.
- `buttons[].commands` — команды, которые выполняются при нажатии.
- `@initiator` — **специальный селектор**: тот игрок, который нажал кнопку.

### Открытие диалога командой

- `/dialogue open <npc> <player> [sceneName]` — открыть сцену игроку.
- `/dialogue change <npc> <sceneName> [players]` — сменить сцену у NPC.

Пример:

```
/dialogue open @e[type=npc,c=1] @p my_scene
```

- `@e[type=npc,c=1]` — ближайший NPC.
- `@p` — ближайший игрок.
- `my_scene` — имя сцены из файла.

### Особенности селектора `@initiator`

- `@initiator` доступен **только** внутри команд кнопок диалога.
- Он указывает на игрока, который нажал кнопку.
- В обычных командах `@initiator` не существует.

## Часть 3. JSON UI (экраны через пак ресурсов)

JSON UI позволяет описать интерфейс целиком — экраны, кнопки, панели — в
файлах пака ресурсов. Это не «меню игрока», а настоящий интерфейс.

### Файл `_ui_defs.json`

Обязательный файл-реестр: перечисляет, какие UI-файлы загружать.

```json
{
  "ui_defs": [
    "ui/my_screen.json",
    "ui/my_common_elements.json"
  ]
}
```

- Путь указывается относительно корня пака ресурсов.
- Обычно файлы лежат в папке `ui/`.
- Без этого файла игра не узнает о ваших UI-файлах.

### Файл экрана

Структура файла экрана (`ui_screen`):

- `namespace` — пространство имён экрана (необязательно).
- Остальные ключи — определения элементов.
- Имя элемента может включать наследование через `@`:
  `my_button@common.button`.
- Переменные начинаются с `$` и могут переопределяться.

Пример `ui/my_screen.json`:

```json
{
  "namespace": "my_ui",

  "my_panel": {
    "type": "panel",
    "size": ["100%", "100%"],
    "controls": [
      {
        "title@my_ui.my_title": {}
      },
      {
        "btn@common.button": {
          "$pressed_button_name": "button.my_button",
          "controls": [
            {
              "label": {
                "type": "label",
                "text": "Нажми меня"
              }
            }
          ]
        }
      }
    ]
  },

  "my_title": {
    "type": "label",
    "text": "Мой экран",
    "color": [1, 1, 1]
  }
}
```

### Типы элементов UI

Официальный список типов (`ui_element`):

- `panel` — обычная панель (контейнер).
- `stack_panel` — панель-стопка (элементы идут подряд).
- `image` — изображение.
- `label` — текст.
- `button` — кнопка.
- `toggle` — переключатель.
- `slider` — ползунок.
- `slider_box` — ползунок с полем ввода.
- `edit_box` — поле ввода текста.
- `grid` — сетка.
- `scroll_view` — прокручиваемая область.
- `scrollbar_box` — полоса прокрутки.
- `dropdown` — выпадающий список.
- `input_panel` — панель ввода.
- `screen` — экран.
- `custom` — пользовательский (с собственным `renderer`).
- `factory` — фабрика (генератор элементов).
- `selection_wheel` — колесо выбора.

### Основные свойства элементов

- `type` — тип элемента.
- `size` — размер `[ширина, высота]`.
- `offset` — смещение от якоря.
- `anchor_from` / `anchor_to` — привязка элемента.
- `layer` — слой отрисовки.
- `controls` — вложенные элементы (список).
- `renderer` — рендерер для `custom`-типов.
- `$переменная` — переменные элемента.

### Когда использовать JSON UI

- Если нужно **изменить внешний вид** существующих экранов (инвентарь, чат).
- Если нужен полностью нестандартный интерфейс (карта, HUD, кастомное
  меню с графикой).
- Для простых меню (кнопки, вопросы, анкеты) JSON UI **избыточен** —
  используйте `@minecraft/server-ui`.

## Что выбрать

- Простое меню с кнопками → `ActionFormData`.
- Да/Нет подтверждение → `MessageFormData`.
- Анкета с вводом → `ModalFormData`.
- Меню у NPC без кода → диалоги NPC (`/dialogue`).
- Полная переделка интерфейса → JSON UI.

## Частые ошибки

- **Форма не показывается** — игрок занят (открыт чат). Проверяйте
  `response.cancelationReason === FormCancelationReason.UserBusy`.
- **Читают `formValues` без проверки `canceled`** — получите ошибку или
  `undefined`.
- **Индексы кнопок считают с 1** — на самом деле с 0.
- **Диалог не открывается** — забыт `format_version: "1.20.80"` или файл не
  в папке `dialogue/`.
- **`@initiator` не работает вне диалога** — это специальный селектор только
  для кнопок диалога.
- **`_ui_defs.json` забыт** — JSON UI-файлы игнорируются.
- **Наследование `@` без базового элемента** — экран не загрузится,
  проверьте имя базового элемента по официальным UI-файлам.
