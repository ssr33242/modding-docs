# Плагины для серверов Minecraft — пошагово от пустой папки до `.jar`

Плагины — это серверные расширения для **Bukkit**-семейства (Bukkit, Spigot, Paper,
Purpur, Folia). Работают только на сервере, клиенту ничего ставить не нужно — этим
они отличаются от модов.

## Когда плагин, а когда мод

- **Плагин** — серверная логика: команды, права, экономика, защита территории,
  мини-игры, чат, телепорты. Ставится в `plugins/`.
- **Мод** — меняет игру на клиенте (блоки, предметы, сущности, рендер). Ставится в `mods/`.
- Если задача — «новый блок/моб/измерение», это мод. Если «админ-команда, регионы,
  разрешения» — это плагин.

## Семейство иерархии (важно понимать совместимость)

- **Bukkit** — базовый API, устарел, но совместим по интерфейсам.
- **Spigot** — улучшенный Bukkit (производительность, патчи).
- **Paper** — современный форк Spigot: быстрее, больше API. Наиболее рекомендуемый.
- **Purpur** — форк Paper с дополнительными настройками.
- **Folia** — форк Paper с многопоточной обработкой регионов (свой API, не все
  плагины совместимы).

Плагин, собранный под **Bukkit/Spigot API**, обычно запускается и на Paper.
Плагин под **Paper API** (новые методы) — только на Paper и его форках.

## Живые версии (проверено по API PaperMC и Modrinth)

- **PaperMC API** переехал: старый `api.papermc.io/v2` отвечает `410 Gone`.
  Новый — `https://fill.papermc.io/v3/projects/paper`.
- **Paper 1.21.1** — последняя сборка `133` (`paper-1.21.1-133.jar`)
- **Paper 1.20.6** — группа `1.20`
- **Paper 26.3** — группа `26.3` (актуальная ветка)
- Актуализировать: `https://fill.papermc.io/v3/projects/paper`

## Соответствие «версия сервера ↔ Java ↔ API»

- **Minecraft 1.21.x** → Java **21** → Paper/Spigot API `1.21.x-R0.1-SNAPSHOT`
- **Minecraft 1.20.5–1.20.6** → Java **21** → API `1.20.6-R0.1-SNAPSHOT`
- **Minecraft 1.19.4–1.20.4** → Java **17** → API соответствующей версии
- **Minecraft 1.17–1.18.2** → Java **17**
- **Minecraft 1.16.5** → Java **8/11/16**
- **Minecraft 1.12.2** → Java **8**

## Структура проекта (Maven или Gradle)

1. **`plugin.yml`** — обязательный манифест в `src/main/resources/`:
   - `name` — имя плагина;
   - `version` — версия (можно `${project.version}` через фильтрацию ресурсов);
   - `main` — полное имя главного класса;
   - `api-version` — версия API, например `1.21` (обязательно для новых ядер);
   - `author`, `description`, `website`;
   - `commands:` — объявление команд;
   - `permissions:` — объявление прав.
2. **`pom.xml`** (Maven) или **`build.gradle`** (Gradle) — сборка.
3. **Главный класс** — наследует `JavaPlugin`.
4. **Дополнительно** — `config.yml` в ресурсах для настроек.

## Репозиторий зависимостей

- Paper API: `https://repo.papermc.io/repository/maven-public/`
- Spigot API: `https://hub.spigotmc.org/nexus/content/repositories/snapshots/`
- Maven-координата Paper: `io.papermc.paper:paper-api:<версия>`
- Maven-координата Spigot: `org.spigotmc:spigot-api:<версия>`

## Главный класс — что обязательно

- Наследование от `org.bukkit.plugin.java.JavaPlugin`.
- `onEnable()` — регистрация команд (`getCommand("...").setExecutor(...)`) и слушателей
  (`getServer().getPluginManager().registerEvents(...)`).
- `onDisable()` — сохранение данных, остановка задач.
- `getConfig()` — доступ к `config.yml`, `saveDefaultConfig()` — создать его из ресурсов.

## Сборка

**Maven:**
- `mvn clean package`
- Результат — `target/<name>-<version>.jar`.

**Gradle:**
- `gradlew build`
- Результат — `build/libs/<name>-<version>.jar`.

Итоговый `.jar` кладётся в папку `plugins/` сервера и подхватывается при
перезапуске (`/reload` для плагинов использовать не рекомендуется — могут утечь
классы; лучше полный рестарт).

## Частые ошибки

- **`plugin.yml` не найден / `main` не указан** — файл должен лежать в корне
  ресурсов, а `main` точно совпадать с пакетом и классом.
- **Плагин не грузится: «Unsupported API version»** — не тот `api-version` или
  старая сборка Java. Для 1.21 нужен `api-version: 1.21` и Java 21.
- **`ClassNotFoundException` при загрузке** — зависимость не в `jar` (нужен
  `shade`/`shadow`-плагин) или `main` указан неверно.
- **Плагин работает на Paper, но не на Spigot** — используются Paper-специфичные
  API (`Adventure`, компоненты, `PaperLib`).
- **Команда не работает** — не объявлена в `plugin.yml` **и** не зарегистрирована
  в `onEnable()`; нужны оба шага.
- **Конфликт с другим плагином** — используй события с приоритетом и проверяй
  `event.isCancelled()` перед изменением.
- **Сборка тянет `paper-api` как обычную зависимость** — правильно
  `compileOnly`/`provided`, иначе конфликт с сервером.

## Проверка результата

Внутри `.jar` должны быть:

- `plugin.yml` в корне;
- скомпилированные `.class`;
- класс, указанный в `main`;
- `config.yml`, если есть.

Проверить: `jar tf plugin.jar | findstr plugin.yml`.
