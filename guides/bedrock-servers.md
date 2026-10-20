# Bedrock — серверные платформы (Geyser, Floodgate, Nukkit, PocketMine)

Если нужно, чтобы **Bedrock-игроки** (телефон, консоль, Windows Bedrock) играли
вместе с **Java-игроками** — аддоны не помогут. Нужны серверные платформы.

## Geyser + Floodgate — мост Bedrock ↔ Java

**Geyser** — прокси, который переводит Bedrock-протокол в Java-протокол. Java-сервер
работает как обычно, Bedrock-игроки подключаются к нему через Geyser.

**Floodgate** — дополнение к Geyser, которое позволяет Bedrock-игрокам заходить
**без Java-аккаунта** (без лицензии).

### Установка на Paper/Spigot-сервер

1. Скачать `Geyser-Spigot.jar` и `floodgate-spigot.jar` (с geysermc.org / Modrinth).
2. Положить оба в `plugins/`.
3. Запустить сервер — создадутся папки `plugins/Geyser-Spigot/` и `plugins/floodgate/`.
4. В `plugins/Geyser-Spigot/config.yml` указать параметры Bedrock-порта
   (`bedrock.port`, по умолчанию 19132).
5. Перезапустить сервер.
6. Bedrock-игроки подключаются к IP сервера на UDP-порт 19132.

### Важно (сетевые порты)

- **Java** — TCP (по умолчанию 25565).
- **Bedrock** — **UDP** (по умолчанию 19132).
- Нужно открыть **оба** порта (TCP и UDP), отключить проксирование Bedrock-порта
  (SRV-записи для Bedrock не работают так, как для Java).
- Сменить порт Bedrock можно в конфиге Geyser.

### Живые версии (проверено по Modrinth)

- Geyser — `2.12.0` (сборка `b1267`), поддерживает MC до `26.3`, для 1.20.5–1.21.1 —
  платформы `paper`, `spigot`, `fabric`, `neoforge`, `velocity`, `bungeecord`.
- Floodgate — платформы `fabric`, `neoforge`, `spigot`/`paper`.
- Актуализировать: `https://api.modrinth.com/v2/project/geyser/version`

### Проверка, что Geyser работает

- В логе сервера: «Started Geyser on 0.0.0.0:19132».
- Bedrock-игрок видит сервер в списке (или подключается по IP:порт).
- Java-игрок и Bedrock-игрок видят друг друга в мире.
- Если Bedrock-игрок не заходит — проверить UDP-порт и брандмауэр.

## Nukkit / Cloudburst Nukkit

- Сервер, написанный целиком под Bedrock-протокол. Не требует Geyser.
- Плагины — своя система (Nukkit-плагины), несовместимы с Bukkit/Spigot.
- CloudburstMC/Nukkit — https://github.com/CloudburstMC/Nukkit
- PowerNukkitX — https://github.com/PowerNukkitX/PowerNukkitX (расширенный форк).

Когда выбирать: если сервер **только для Bedrock-игроков** и нужны свои плагины.

## PocketMine-MP

- Сервер для Bedrock на PHP: https://github.com/pmmp/PocketMine-MP
- Своя система плагинов (PHP), отдельные репозитории в Poggit.
- Когда выбирать: небольшие Bedrock-серверы, где важна простота плагинов.

## Dragonfly

- Сервер Bedrock на Go: https://github.com/df-mc/dragonfly
- Высокая производительность, своя система плагинов на Go.

## Что выбрать

- **Java-сервер + хочу пустить Bedrock-игроков** → Geyser + Floodgate.
- **Только Bedrock, плагины на Java-подобном API** → Nukkit / PowerNukkitX.
- **Только Bedrock, плагины на PHP** → PocketMine-MP.
- **Только Bedrock, максимальная производительность** → Dragonfly.

## Инструменты совместимости

- **ViaVersion** — https://modrinth.com/plugin/viaversion
  Позволяет игрокам разных Java-версий заходить на сервер одной версии.
- **ViaBackwards / ViaRewind** — для старых клиентов (1.8 и т.п.).
- **ViaBedrock** — https://github.com/ViaVersion/ViaBedrock
  Прокси-перевод версий Bedrock.

## Частые ошибки при настройке моста

- **Bedrock-игрок не видит сервер** — закрыт UDP-порт 19132, или провайдер блокирует
  UDP. Проверить брандмауэр и NAT.
- **Java-игроки не видят Bedrock-игроков** — Geyser и сервер на разных машинах без
  правильной настройки `remote`/`auth-type`.
- **Floodgate-игрок не может зайти** — не настроен `auth-type` (должен быть `floodgate`)
  и не добавлен ключ Floodgate.
- **Плагины Bukkit не работают на Nukkit** — это разные API; для Bedrock-ядер нужны
  свои плагины.
- **Скины/аватары Bedrock отображаются неверно** — ограничение Geyser (частичная
  совместимость), а не ошибка установки.
