# Инструменты моддинга — что чем делать

Разделение по задачам: собрать мод, смоделировать, нарисовать, написать скрипт,
отладить. Всё проверено — ссылки живые.

## Сборка и среда разработки

- **Gradle** — https://gradle.org — основная система сборки для Java-модов.
- **Fabric Loom** — https://github.com/FabricMC/fabric-loom — Gradle-плагин для Fabric.
- **Architectury Loom** — https://github.com/architectury/architectury-loom — Loom с
  поддержкой мультилоадера (Fabric + Forge/NeoForge).
- **ModDevGradle** — https://github.com/neoforged/ModDevGradle — официальный плагин
  сборки NeoForge (современная альтернатива пользовательскому Gradle-плагину).
- **ForgeGradle** — часть Forge MDK — Gradle-плагин для Forge.
- **run-task (jpenilla)** — https://github.com/jpenilla/run-task — Gradle-задачи для
  запуска сервера/прокси из сборки.
- **Gradle-Toolkit (Deftu)** — https://github.com/Deftu/Gradle-Toolkit — вспомогательные
  Gradle-задачи для моддинга.

## IDE и редакторы кода

- **IntelliJ IDEA** — https://www.jetbrains.com/idea/ — основная среда для моддинга.
- **MinecraftDev (плагин IDEA)** — https://github.com/minecraft-dev/MinecraftDev —
  подсветка и деобфускация Mixin, поддержка Fabric/Forge.
- **VS Code** — https://code.visualstudio.com/ — для датапаков, скриптов, JSON.
- **MCIDE** — https://github.com/MC-IDE/MCIDE — отдельная IDE под моддинг на базе
  платформы IntelliJ.

## Визуальные редакторы модов (без кода)

- **MCreator** — https://github.com/MCreator/MCreator — генератор Java-модов и
  Bedrock-аддонов через визуальный интерфейс.

## Модели, текстуры, анимации

- **Blockbench** — https://github.com/JannisX11/blockbench — модели, текстуры,
  анимации; экспорт и в Java, и в Bedrock. Основной инструмент.
- **Aseprite / Krita / GIMP** — рисование текстур.
- **Paint.NET** — https://www.getpaint.net/ — простой редактор для Windows.

## Датапаки и ресурс-паки

- **misode.github.io** — https://github.com/misode/misode.github.io — генераторы
  рецептов, лут-таблиц, моделей, тегов, датапаков.
- **Spyglass** — https://github.com/SpyglassMC/Spyglass — валидация и автодополнение
  для датапаков в редакторе.
- **beet** — https://github.com/mcbeet/beet — комплект разработки пакетов.
- **PackSquash** — https://github.com/ComunidadAylas/PackSquash — сжатие паков.
- **langcraft** — https://github.com/SuperTails/langcraft — компилятор LLVM IR → датапак.
- **MCFPP** — https://github.com/MinecraftFunctionPlusPlus/MCFPP — ООП-язык в датапак.

## Инструменты Bedrock Edition

- **Mojang/bedrock-samples** — https://github.com/Mojang/bedrock-samples — эталон
  структуры пакетов и ванильные данные.
- **minecraft-scripting-samples** — https://github.com/microsoft/minecraft-scripting-samples —
  официальные примеры Script API.
- **bridge.** — https://github.com/bridge-core/editor — редактор аддонов Bedrock с
  подсветкой и сборкой.
- **regolith** — https://github.com/Bedrock-OSS/regolith — система сборки аддонов из
  исходников.
- **JaylyDev/ScriptAPI** — https://github.com/JaylyDev/ScriptAPI — коллекция скриптов.

## Маппинги и деобфускация

- **Yarn** — https://github.com/FabricMC/yarn — маппинги Fabric.
- **MCPConfig** — https://github.com/MinecraftForge/MCPConfig — маппинги Forge.
- **MinecraftMappings** — https://github.com/phase/MinecraftMappings — транзитивные
  маппинги между системами.

## Отладка и профилирование

- **spark** — https://github.com/lucko/spark — профилировщик сервера и клиента
  (мод и плагин).
- **Scarpet / /debug** — встроенная отладка датапаков и функций.
- **Логи контента** — в Bedrock: «Настройки» → «Создатель» → «Логи контента».

## Полезные онлайн-ресурсы

- **Minecraft Wiki** — https://minecraft.wiki — протоколы, форматы, поведение игры.
- **Modrinth** — https://modrinth.com — хостинг модов и паков.
- **CurseForge** — https://www.curseforge.com/minecraft — хостинг модов.
- **Hangar** — https://hangar.papermc.io — хостинг плагинов Paper.
- **SpigotMC** — https://www.spigotmc.org/resources/ — плагины Bukkit/Spigot.
- **MCPEDL** — https://mcpedl.com — аддоны Bedrock.
