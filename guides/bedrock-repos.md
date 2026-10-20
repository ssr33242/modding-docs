# Bedrock Edition — репозитории и площадки

Где искать, публиковать и брать примеры аддонов, пакетов и скриптов для Bedrock Edition.

## Официальные источники Mojang/Microsoft

- **Minecraft Creator Documentation** — https://learn.microsoft.com/minecraft/creator/
  Главная официальная документация по аддонам: `manifest.json`, сущности, блоки,
  рецепты, Script API.
- **Официальные примеры (Sample Packs)** —
  https://github.com/Mojang/bedrock-samples
  Ресурсы и поведение из самой игры + примеры. Лучший источник «как правильно».
- **Script API reference** —
  https://learn.microsoft.com/minecraft/creator/scriptapi/
  Полный справочник по `@minecraft/server` и другим модулям.
- **minecraft.net/addons** — витрина официальных аддонов.

## Крупные площадки для загрузки и публикации

- **MCPEDL** — https://mcpedl.com
  Самая большая площадка аддонов, карт, пакетов. Публикация бесплатная.
- **CurseForge (Bedrock)** — https://www.curseforge.com/minecraft-bedrock
  Официальная поддержка Bedrock: аддоны, пакеты, миры. Есть API и программа авторов.
- **Modrinth** — https://modrinth.com
  Поддерживает ресурс-паки и датапаки; часть Bedrock-паков тоже там.
- **Planet Minecraft** — https://www.planetminecraft.com
  Раздел Bedrock: скины, пакеты, карты.

## Репозитории и инструменты (GitHub)

- **Mojang/bedrock-samples** — https://github.com/Mojang/bedrock-samples
  Официальные примеры (см. выше).
- **Bedrock-OSS** — https://github.com/Bedrock-OSS
  Сообщество и ключевые инструменты:
  - `bedrock-wiki` — https://github.com/Bedrock-OSS/bedrock-wiki (основная вики)
  - `regolith` — система сборки аддонов
- **bridge.** — https://github.com/bridge-core/editor
  Редактор аддонов с IntelliSense и сборкой.
- **Blockbench** — https://github.com/JannisX11/blockbench
  Модели, текстуры, анимации; экспорт в формат Bedrock.
- **Amethyst** — https://github.com/Amethystic/amethyst
  Продвинутый инструмент для работы с JSON Bedrock.
- **mcbe-essentials** — https://github.com/Ersatz77/mcbe-essentials
  Примеры скриптов Script API.
- **Bedrock Script API примеры** — https://github.com/JaylyDev/ScriptAPI
  Большая коллекция примеров и утилит для `@minecraft/server`.

## Вики и справочники (неофициальные, но полезные)

- **Bedrock Wiki** — https://wiki.bedrock.dev
  Основной русско/англоязычный справочник: блоки, предметы, сущности, скрипты,
  рецепты, лут-таблицы.
- **Microsoft Learn (Creator)** — официальный и самый достоверный.
- **Minecraft Wiki (Bedrock)** — https://minecraft.wiki/w/Bedrock_Edition

## Серверные платформы для Bedrock

- **Geyser** — https://geysermc.org / https://github.com/GeyserMC/Geyser
  Прокси-мост: позволяет Bedrock-игрокам заходить на Java-сервер (и наоборот).
- **Floodgate** — https://github.com/GeyserMC/Floodgate
  Позволяет Bedrock-игрокам заходить **без** Java-аккаунта. Работает вместе с Geyser.
- **Nukkit / Cloudburst Nukkit** — https://github.com/CloudburstMC/Nukkit
  Серверное ядро, написанное под Bedrock-протокол (плагины Nukkit).
- **PocketMine-MP** — https://github.com/pmmp/PocketMine-MP
  Сервер для Bedrock на PHP; своя система плагинов.
- **PowerNukkitX** — https://github.com/PowerNukkitX/PowerNukkitX
  Расширенный форк Nukkit с поддержкой новых версий.
- **Dragonfly** — https://github.com/df-mc/dragonfly
  Сервер Bedrock на Go.
- **ViaBedrock** — https://github.com/ViaVersion/ViaBedrock
  Прокси-перевод версий Bedrock.

## Инструменты для работы с пакетами

- Генераторы UUID: любой UUID-генератор или `python -c "import uuid; print(uuid.uuid4())"`.
- Упаковка: любой архиватор (zip → переименовать в `.mcpack`/`.mcaddon`).
- Проверка JSON: любой JSON-валидатор; игра придирчива к синтаксису.
- Отладка скриптов: содержимое-логи в игре («Настройки» → «Создатель» → «Логи контента»).

## Как искать нужный аддон

- Смотри **обновления и совместимость** с версией игры (`min_engine_version`).
- Проверяй, есть ли у аддона **исходники** (GitHub) — так проще учиться.
- Официальные примеры Mojang — эталон структуры; начинать лучше с них.
- Для серверных нужд (не для клиента) — Geyser/Floodgate/Nukkit, а не аддоны.
