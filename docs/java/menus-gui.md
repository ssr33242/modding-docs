# Меню и GUI в Java Edition (Forge / NeoForge)

GUI в Minecraft: Java Edition строится на двух частях:

- **Screen** (экран) — то, что видит и с чем взаимодействует игрок.
- **Menu** (`AbstractContainerMenu`) — логика слотов и синхронизации между
  клиентом и сервером (для инвентарей и подобного).

> Источники (официальные):
> - NeoForge: экраны —
>   `https://github.com/neoforged/Documentation/blob/main/docs/rendering/screens.md`
> - NeoForge: меню —
>   `https://github.com/neoforged/Documentation/blob/main/docs/inventories/menus.md`
> - MinecraftForge: `https://github.com/MinecraftForge/Documentation`

## Render в две фазы

Отрисовка GUI проходит в две фазы:

- **Фаза сбора (submission phase)** — собирает все элементы (кнопки, текст,
  предметы) в `GuiRenderState`.
- **Фаза отрисовки (render phase)** — сортирует и рисует элементы.

Типы элементов ванилы:

- `GuiElementRenderState` — общий элемент.
- `GuiItemRenderState` — предмет.
- `GuiTextRenderState` — текст.
- `PictureInPictureRenderState` — «картинка в картинке».

## Относительные координаты

- X растёт слева направо, Y — сверху вниз.
- Координаты **не фиксированы**: зависят от размера экрана и масштаба GUI.
- Всегда пересчитывайте координаты под текущий размер экрана.
- Плохо пересчитанные координаты — элементы уезжают или выглядят криво.
- Проверка: меняйте «Масштаб GUI» в настройках — элементы должны
  оставаться на месте.

## `GuiGraphicsExtractor`

- Основной объект фазы сбора.
- Первый параметр почти всех методов отрисовки.
- Даёт доступ к текущей позе (`Matrix3x2fStack`) для смещений и поворотов:

```java
graphics.pose().pushMatrix();
graphics.pose().translate(10, 10);   // смещение
// ... рисование ...
graphics.pose().popMatrix();
```

## Основные методы отрисовки

- Цветные прямоугольники (fill) — фон, полосы, подсветка.
- Строки (текст) — надписи, значения.
- Текстуры (blit) — фон контейнера, иконки.
- Предметы (item render) — отрисовка стака предметов.
- Подсказки (tooltips) — всплывающие описания.
- Picture-in-Picture — вложенная отрисовка (например, превью).

## `Screen` — базовый экран

- Базовый класс всех экранов.
- Конструктор принимает `Component` (заголовок), `Minecraft` и `Font`:

```java
public MyScreen(Component title) {
    super(Minecraft.getInstance(), Minecraft.getInstance().font, title);
}
```

### Инициализация (`init`)

- Вызывается после создания экрана.
- Здесь добавляют виджеты и **предвычисляют** относительные координаты.
- При изменении размера окна `init` вызывается снова.

Три способа добавить виджет:

- `addWidget` — интерактивный и озвучиваемый, но **не рисуется**.
- `addRenderableOnly` — только рисуется, не интерактивный.
- `addRenderableWidget` — интерактивный, озвучиваемый и рисуется
  (**основной способ**).

```java
@Override
protected void init() {
    super.init();
    this.addRenderableWidget(new EditBox(/* ... */));
}
```

### Тик экрана

- `tick()` — клиентская логика каждый тик (анимации, обновление данных).

### Обработка ввода

- Через `GuiEventListener`: `mouseClicked`, `keyPressed`, `charTyped`.
- `ContainerEventHandler` — обработка событий для контейнеров/виджетов.
- `NarratableEntry` — поддержка озвучивания (accessibility).

### Отрисовка и закрытие

- `render(...)` — отрисовка экрана.
- `onClose()` — вызывается при закрытии экрана.
- Если экран открыт поверх мира, мир может ставиться на паузу (настраивается).

## `AbstractContainerScreen` — экран с инвентарём

- Наследуйте, если экран **связан с меню** (слоты, инвентарь).
- Экран + обработчик ввода меню, содержит логику слотов и синхронизации.
- Обычно нужно переопределить всего пару методов.

Конструктор принимает:

- сам контейнер-меню (generic `T`),
- инвентарь игрока (для имени),
- заголовок экрана,
- ширину и высоту фоновой текстуры.

```java
public MyContainerScreen(MyMenu menu, Inventory playerInv, Component title) {
    super(menu, playerInv, title);
}
```

Поля позиционирования подписей:

- `titleLabelX`, `titleLabelY` — координаты заголовка экрана.
- `inventoryLabelX`, `inventoryLabelY` — координаты названия инвентаря.

Важные поля:

- `leftPos`, `topPos` — предвычисленный левый верхний угол фона
  (считаются в `init`).
- Размер текстуры по умолчанию — `176 x 166`. Это **область** текстуры, а
  не размер PNG (PNG обычно `256 x 256`).

## `Menu` (backend)

- Меню — «вид» на данные, а не сами данные. Не связывайте данные напрямую с
  меню.
- Меню создаются и удаляются динамически, поэтому реестровым объектом
  является не меню, а его **тип** — `MenuType`.
- `MenuType` должен быть зарегистрирован.

Создание `MenuType` через `MenuSupplier`:

```java
public static final Supplier<MenuType<MyMenu>> MY_MENU =
    REGISTER.register("my_menu",
        () -> new MenuType<>(MyMenu::new, FeatureFlags.DEFAULT_FLAGS));

public MyMenu(int containerId, Inventory playerInv) {
    super(MY_MENU.get(), containerId);
}
```

- `MenuSupplier` — функция от `(containerId, playerInv)`, возвращает меню.
- `containerId` уникален **для конкретного игрока** — один и тот же id у
  разных игроков означает разные меню.

`IContainerFactory` — если клиенту нужны доп. данные (например, позиция в
мире). Даёт доступ к `RegistryFriendlyByteBuf`:

```java
public static final Supplier<MenuType<MyMenuExtra>> MY_MENU_EXTRA =
    REGISTER.register("my_menu_extra",
        () -> IMenuTypeExtension.create(MyMenu::new));

public MyMenuExtra(int containerId, Inventory playerInv, FriendlyByteBuf extraData) {
    super(MY_MENU_EXTRA.get(), containerId);
    // читаем доп. данные из буфера
}
```

### `AbstractContainerMenu`

- Базовый класс всех меню.
- Принимает `MenuType` и `containerId`.
- `#stillValid` — проверка, что игрок ещё может пользоваться меню
  (например, не отошёл от блока). Через `ContainerLevelAccess`.
- **Синхронизация данных** — отдельный механизм (слоты + `ContainerData`),
  нельзя свободно менять данные сервера из клиента.

## Открытие меню

- Меню открывается на **сервере** командой/кодом.
- Клиент получает `MenuType` и создаёт соответствующий экран.
- Распространённые реализации — `SimpleMenuProvider` или свой провайдер.

## Регистрация экрана для меню

Экран регистрируется в `RegisterMenuScreensEvent` (mod-шина, только клиент):

```java
@SubscribeEvent
public static void registerScreens(RegisterMenuScreensEvent event) {
    event.register(MY_MENU.get(), MyContainerScreen::new);
}
```

## Fabric: экраны

- Экраны наследуют `Screen`, обработка ввода аналогична.
- Расширение `HandledScreens` регистрирует экран для типа меню (аналог
  `RegisterMenuScreensEvent`).
- Точные сигнатуры см. в официальных docs Fabric.

## Частые ошибки

- **Фиксированные координаты** вместо относительных — элементы уезжают при
  смене масштаба GUI.
- **Забыт `super.init()`** — виджеты/состояние некорректны.
- **Предметы/данные рисуются из клиентского состояния** без синхронизации —
  рассинхрон сервер/клиент.
- **`MenuType` не зарегистрирован** — меню не откроется.
- **Регистрация экрана на сервере** — `RegisterMenuScreensEvent` только
  клиентский.
- **Изменение данных меню напрямую** с клиента — не синхронизируется, нужен
  серверный путь.
- **Использование устаревшего API отрисовки** — в новых версиях введён
  `GuiRenderState`/`GuiGraphicsExtractor`, старые вызовы могут отличаться.

## Проверка версий

- Пакеты и классы отрисовки, сигнатуры экранов и меню меняются между
  версиями.
- Версии Minecraft и загрузчиков см. в документе про версии.
- Сверяйтесь с официальной документацией загрузчика под вашу версию.
