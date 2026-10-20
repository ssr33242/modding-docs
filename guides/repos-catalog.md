# Репозитории по моддингу Minecraft — большой каталог

Живой каталог: ссылки собраны через GitHub API и Modrinth API (звёзды — на момент
сбора). Разбит по темам: ядра, моды, плагины, аддоны Bedrock, сервера, инструменты,
документация.

## 1. Ядра и загрузчики модов (Java)

- **MinecraftForge/MinecraftForge** — https://github.com/MinecraftForge/MinecraftForge ★7.8k
  Базовое ядро Forge.
- **neoforged/NeoForge** — https://github.com/neoforged/NeoForge
  Современный форк Forge (1.20.2+).
- **FabricMC/fabric** — https://github.com/FabricMC/fabric
  Ядро Fabric (лоадер + API).
- **FabricMC/fabric-loader** — https://github.com/FabricMC/fabric-loader
  Только загрузчик Fabric.
- **FabricMC/fabric-loom** — https://github.com/FabricMC/fabric-loom ★369
  Gradle-плагин сборки Fabric-модов.
- **QuiltMC/quilt-loader** — https://github.com/QuiltMC/quilt-loader ★520
  Загрузчик Quilt.
- **QuiltMC/quilt-standard-libraries (QSL)** — https://github.com/QuiltMC/quilt-standard-libraries
  Стандартная библиотека Quilt.
- **MinecraftForge/FML** — https://github.com/MinecraftForge/FML ★434
  Загрузчик Forge (архив, влит в Forge).
- **CleanroomMC/Cleanroom** — https://github.com/CleanroomMC/Cleanroom ★622
  Модернизированный форк Forge для старых версий (1.12.2).
- **Sinytra/Connector** — https://github.com/Sinytra/Connector ★759
  Запуск Fabric-модов на NeoForge.
- **KiltMC/Kilt** — https://github.com/KiltMC/Kilt ★708
  Запуск Forge/NeoForge-модов на Fabric.
- **Ray-T-r/Minecraft-Forbric-mod-loader** — https://github.com/Ray-T-r/Minecraft-Forbric-mod-loader
  Загрузка Fabric + Forge + NeoForge в одном инстансе.
- **PacifistMC/Forgix** — https://github.com/PacifistMC/Forgix ★189
  Объединение jar разных загрузчиков в один.

## 2. Кросс-платформенная разработка (мультилоадер)

- **architectury/architectury-api** — https://github.com/architectury/architectury-api ★450
  Промежуточный API для одного кода на Fabric и Forge/NeoForge.
- **architectury/architectury-loom** — https://github.com/architectury/architectury-loom
  Loom с поддержкой мультилоадера.
- **FabricMC/fabric-api** — https://github.com/FabricMC/fabric-api
  Основной API Fabric.
- **Sinytra/ForgifiedFabricAPI** — https://github.com/Sinytra/ForgifiedFabricAPI
  Fabric API для NeoForge (для мультилоадер-сборок).

## 3. Инструменты разработки и IDE

- **minecraft-dev/MinecraftDev** — https://github.com/minecraft-dev/MinecraftDev ★1.8k
  Плагин IntelliJ IDEA для моддинга (Fabric, Forge, Mixin, миксин-отладка).
- **SpyglassMC/Spyglass** — https://github.com/SpyglassMC/Spyglass ★478
  Инструменты для датапаков: валидация, автодополнение.
- **MCreator/MCreator** — https://github.com/MCreator/MCreator ★1.2k
  Визуальный редактор модов (Java-моды и Bedrock-аддоны) без кода.
- **misode/misode.github.io** — https://github.com/misode/misode.github.io ★925
  Генераторы датапаков, лут-таблиц, рецептов, моделей.
- **mcbeet/beet** — https://github.com/mcbeet/beet ★305
  Набор инструментов для разработки пакетов данных (датпаков).
- **SuperTails/langcraft** — https://github.com/SuperTails/langcraft ★562
  Компилятор LLVM IR → датапак.
- **MinecraftFunctionPlusPlus/MCFPP** — https://github.com/MinecraftFunctionPlusPlus/MCFPP ★281
  Объектно-ориентированный язык, компилируемый в датапак.
- **Deftu/Gradle-Toolkit** — https://github.com/Deftu/Gradle-Toolkit
  Набор Gradle-инструментов для моддинга.
- **jpenilla/run-task** — https://github.com/jpenilla/run-task ★365
  Gradle-задачи для запуска сервера/прокси.

## 4. Маппинги и деобфускация

- **FabricMC/yarn** — https://github.com/FabricMC/yarn ★1.2k
  Свободные маппинги имён Minecraft.
- **Legacy-Fabric/yarn** — https://github.com/Legacy-Fabric/yarn ★54
  Yarn для старых версий и снапшотов.
- **MinecraftForge/MCPConfig** — https://github.com/MinecraftForge/MCPConfig
  Конфиги MCP (маппинги Forge).
- **phase/MinecraftMappings** — https://github.com/phase/MinecraftMappings ★61
  Транзитивные маппинги 1.7.10–1.15.2 (Spigot ↔ MCP ↔ Yarn ↔ Mojang).

## 5. Примеры и шаблоны модов

- **FabricMC/fabric-example-mod** — https://github.com/FabricMC/fabric-example-mod
  Официальный пример мода Fabric.
- **neoforged/MDK** — https://github.com/neoforged/MDK
  Официальный Mod Development Kit для NeoForge.
- **MinecraftForge/MDKExamples** — https://github.com/MinecraftForge/MDKExamples
  Официальные примеры Forge MDK (Mod Development Kit).
- **QuiltMC/quilt-template-mod** — https://github.com/QuiltMC/quilt-template-mod
  Шаблон мода Quilt.
- **TelepathicGrunt/StructureTutorialMod** — https://github.com/TelepathicGrunt/StructureTutorialMod ★329
  Пример регистрации структуры (NeoForge, Forge, Fabric).
- **myoun/fabric-example-mod-kotlin-with-kotlin-dsl** — https://github.com/myoun/fabric-example-mod-kotlin-with-kotlin-dsl ★43
  Пример мода Fabric на Kotlin + Kotlin DSL.

## 6. Крупные открытые моды (учиться по коду)

- **Creators-of-Create/Create** — https://github.com/Creators-of-Create/Create ★4.6k
  Пример крупного инженерного мода (NeoForge/Forge).
- **AppliedEnergistics/Applied-Energistics-2** — https://github.com/AppliedEnergistics/Applied-Energistics-2 ★1.8k
  Крупный мод про хранение и автоматизацию.
- **CaffeineMC/lithium** — https://github.com/CaffeineMC/lithium ★2.2k
  Оптимизация игровой логики (Fabric/NeoForge).
- **CaffeineMC/phosphor-fabric** — https://github.com/CaffeineMC/phosphor-fabric ★1.1k
  Оптимизация освещения.
- **CaffeineMC/sodium** — https://github.com/CaffeineMC/sodium
  Оптимизация рендера (Fabric/NeoForge).
- **EngineHub/WorldEdit** — https://github.com/EngineHub/WorldEdit ★3.5k
  Редактор мира (мод + плагин).
- **MightyPirates/OpenComputers** — https://github.com/MightyPirates/OpenComputers ★1.7k
  Компьютеры в Minecraft.
- **henkelmax/simple-voice-chat** — https://github.com/henkelmax/simple-voice-chat ★734
  Голосовой чат (мультилоадер).

## 7. Плагины для серверов (Bukkit/Spigot/Paper)

- **PaperMC/Paper** — https://github.com/PaperMC/Paper
  Основное современное серверное ядро.
- **PaperMC/Velocity** — https://github.com/PaperMC/Velocity
  Высокопроизводительный прокси.
- **SpigotMC/Spigot** — https://hub.spigotmc.org/stash/projects/SPIGOT
  Spigot (исходники через Stash).
- **LuckPerms/LuckPerms** — https://github.com/LuckPerms/LuckPerms ★2.3k
  Система прав (examples: обращения к API хоста).
- **EssentialsX/Essentials** — https://github.com/EssentialsX/Essentials ★2.3k
  Набор базовых серверных команд.
- **DiscordSRV/DiscordSRV** — https://github.com/DiscordSRV/DiscordSRV ★1.2k
  Мост Minecraft ↔ Discord.
- **ViaVersion/ViaVersion** — https://github.com/ViaVersion/ViaVersion ★1.6k
  Совместимость версий клиентов.
- **SkriptLang/Skript** — https://github.com/SkriptLang/Skript ★1.4k
  Скриптинг серверной логики без компиляции.
- **Slimefun/Slimefun4** — https://github.com/Slimefun/Slimefun4 ★1.1k
  «Модпак» в виде плагина.
- **EngineHub/WorldGuard** — https://github.com/EngineHub/WorldGuard ★941
  Защита территории.
- **IntellectualSites/FastAsyncWorldEdit** — https://github.com/IntellectualSites/FastAsyncWorldEdit ★807
  Ускоренный WorldEdit.
- **GrimAnticheat/Grim** — https://github.com/GrimAnticheat/Grim ★1.8k
  Асинхронный античит.
- **EndstoneMC/endstone** — https://github.com/EndstoneMC/endstone ★757
  Сервер Bedrock с plugin API в стиле Paper.
- **xenondevs/Nova** — https://github.com/xenondevs/Nova ★500
  Серверный фреймворк для кастомного контента.

## 8. Bedrock Edition — аддоны, скрипты, серверы

- **Mojang/bedrock-samples** — https://github.com/Mojang/bedrock-samples
  Официальные ресурсы и примеры из игры.
- **microsoft/minecraft-scripting-samples** — https://github.com/microsoft/minecraft-scripting-samples ★242
  Официальные примеры Script API и GameTest.
- **JaylyDev/ScriptAPI** — https://github.com/JaylyDev/ScriptAPI ★180
  Сообщество скриптов для Bedrock.
- **Bedrock-OSS/bedrock-wiki** — https://github.com/Bedrock-OSS/bedrock-wiki
  Основная вики по аддонам Bedrock.
- **Bedrock-OSS/regolith** — https://github.com/Bedrock-OSS/regolith
  Система сборки аддонов.
- **bridge-core/editor** — https://github.com/bridge-core/editor
  Редактор аддонов с IntelliSense.
- **JannisX11/blockbench** — https://github.com/JannisX11/blockbench
  Модели, текстуры, анимации (и Java, и Bedrock).
- **Amethyst** — больше не поддерживается (репозиторий удалён). Для работы с JSON
  Bedrock используй `bridge-core/editor`, `mcbeet/beet` и `Bedrock-OSS/regolith`.
- **ZtechNetwork/MCBVanillaResourcePack** — https://github.com/ZtechNetwork/MCBVanillaResourcePack ★414
  Ванильные ресурс-паки Bedrock (эталон).
- **SIsilicon/WorldEdit-BE** — https://github.com/SIsilicon/WorldEdit-BE ★429
  WorldEdit как аддон Bedrock.
- **LiteLDev/LeviLamina** — https://github.com/LiteLDev/LeviLamina ★1.7k
  Загрузчик модов для Bedrock (бывший LiteLoaderBDS).

## 9. Серверные ядра Bedrock

- **pmmp/PocketMine-MP** — https://github.com/pmmp/PocketMine-MP ★3.6k
  Сервер Bedrock на PHP.
- **CloudburstMC/Nukkit** — https://github.com/CloudburstMC/Nukkit ★1.4k
  Bedrock-сервер на Java.
- **PowerNukkitX/PowerNukkitX** — https://github.com/PowerNukkitX/PowerNukkitX ★684
  Расширенный форк Nukkit.
- **df-mc/dragonfly** — https://github.com/df-mc/dragonfly ★853
  Bedrock-сервер на Go.
- **Nukkit/Nukkit** — https://github.com/Nukkit/Nukkit ★836
  Оригинальный Nukkit (старый).

## 10. Мосты Java ↔ Bedrock

- **GeyserMC/Geyser** — https://github.com/GeyserMC/Geyser ★5.9k
  Bedrock-игроки заходят на Java-сервер.
- **GeyserMC/Floodgate** — https://github.com/GeyserMC/Floodgate ★696
  Вход Bedrock-игроков без Java-аккаунта.
- **GeyserMC/Hydraulic** — https://github.com/GeyserMC/Hydraulic ★317
  Bedrock-игроки на модовых Java-серверах.
- **GeyserMC/GeyserConnect** — https://github.com/GeyserMC/GeyserConnect ★243
  Подключение Bedrock без своего сервера.
- **GeyserMC/MCProtocolLib** — https://github.com/GeyserMC/MCProtocolLib ★909
  Библиотека протокола Java.
- **DragonetMC/DragonProxy** — https://github.com/DragonetMC/DragonProxy ★981
  Прокси Bedrock → Java.

## 11. Библиотеки протокола (для продвинутых)

- **retrooper/packetevents** — https://github.com/retrooper/packetevents ★921
  Библиотека пакетов Java.
- **PrismarineJS/bedrock-protocol** — https://github.com/PrismarineJS/bedrock-protocol ★486
  Протокол Bedrock (JS).
- **Sandertv/gophertunnel** — https://github.com/Sandertv/gophertunnel ★576
  Протокол Bedrock (Go).
- **CloudburstMC/Protocol** — https://github.com/CloudburstMC/Protocol ★419
  Протокол Bedrock (Java).
- **barneygale/quarry** — https://github.com/barneygale/quarry ★548
  Протокол Minecraft на Python.

## 12. Датапаки и паки ресурсов

- **misode/misode.github.io** — https://github.com/misode/misode.github.io ★925
  Генераторы датапаков и ресурсов.
- **ComunidadAylas/PackSquash** — https://github.com/ComunidadAylas/PackSquash ★864
  Оптимизатор паков.
- **OpenNBS/NoteBlockStudio** — https://github.com/OpenNBS/NoteBlockStudio ★1k
  Создание музыки для Minecraft.
- **mcbeet/beet** — https://github.com/mcbeet/beet ★305
  Комплект разработки пакетов.

## 13. Официальная документация (исходники)

- **FabricMC/fabric-docs** — https://github.com/FabricMC/fabric-docs ★232
  Официальная документация Fabric.
- **neoforged/Documentation** — https://github.com/neoforged/Documentation
  Документация NeoForge.
- **MinecraftForge/Documentation** — https://github.com/MinecraftForge/Documentation ★513
  Документация Forge.
- **QuiltMC/quiltmc.org** — https://github.com/QuiltMC/quiltmc.org
  Сайт и вики Quilt.
- **PaperMC/docs** — https://github.com/PaperMC/docs
  Документация Paper.
- **Bedrock-OSS/bedrock-wiki** — https://github.com/Bedrock-OSS/bedrock-wiki
  Вики по Bedrock.

## 14. Полезные списки и подборки

- **TheUsefulLists/UsefulMods** — https://github.com/TheUsefulLists/UsefulMods ★2.4k
  Список полезных модов.
- **LambdAurora/optifine_alternatives** — https://github.com/LambdAurora/optifine_alternatives ★459
  Альтернативы OptiFine.
- **comp500/quilt-serverside-mods** — https://github.com/comp500/quilt-serverside-mods ★571
  Серверные моды для Quilt.
- **Bytekron/Awesome-Minecraft** — https://github.com/Bytekron/Awesome-Minecraft ★68
  Большая подборка ссылок: ядра, прокси, плагины, загрузчики.
- **mouse0w0/MinecraftDeveloperGuide** — https://github.com/mouse0w0/MinecraftDeveloperGuide ★3.4k
  Гид для разработчиков (кит.).

## 15. Modrinth — крупные проекты

- **fabric-api** — https://modrinth.com/mod/fabric-api (284 млн загрузок) — базовый API Fabric.
- **sodium** — https://modrinth.com/mod/sodium (249 млн) — оптимизация рендера.
- **architectury-api** — https://modrinth.com/mod/architectury-api (107 млн) — мультилоадер API.
- **geyser** — https://modrinth.com/plugin/geyser (1.5 млн) — мост Bedrock ↔ Java.
- **lithium** — https://modrinth.com/mod/lithium — оптимизация логики.
- **iris** — https://modrinth.com/mod/iris — шейдеры для Sodium.

## Как этим пользоваться

1. **Изучение API** — открывать крупные моды (Create, AE2, Lithium) и смотреть, как
   они регистрируют контент.
2. **Шаблон проекта** — брать официальные MDK/example-mod, а не сборки из интернета.
3. **Своя библиотека** — смотреть архитектуру architectury-api для мультилоадера.
4. **Плагин** — ориентир: LuckPerms (API хоста, `softdepend`), EssentialsX (команды).
5. **Bedrock-аддон** — начинать с `Mojang/bedrock-samples` и `minecraft-scripting-samples`.

## Где искать дальше

- GitHub Topics: `minecraft-mod`, `minecraft-plugin`, `fabric-mod`, `bedrock-addon`
- Modrinth: https://modrinth.com
- CurseForge: https://www.curseforge.com/minecraft
- Hangar (PaperMC): https://hangar.papermc.io
- SpigotMC: https://www.spigotmc.org/resources/
- MCPEDL (Bedrock): https://mcpedl.com
