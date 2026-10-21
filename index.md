# Minecraft Modding Reference

Рабочий справочник по созданию контента для Minecraft: моды, плагины, аддоны.
Матрица совместимости, проверенные шаблоны и пошаговые инструкции.

!!! info "Состояние на 21 октября 2026"
    Minecraft Java — релиз **26.3**, снапшот **26.4-snapshot-5**.

    | Загрузчик | 26.x | Версия под 26.3 |
    |---|---|---|
    | Fabric | ✅ | API `0.163.0+26.3`, Loader `0.19.5`, Loom `1.18-SNAPSHOT` |
    | NeoForge | ✅ | `26.3.0.95`, ModDevGradle `2.0.148` |
    | Forge | ✅ | `26.3-66.0.13`, ForgeGradle `6.0.54` (только Gradle 8.x) |
    | Paper | ✅ | `26.3` |
    | Quilt | ❌ | нет маппингов под 26.x |

    С 26.1 Minecraft **не обфусцируется**, Yarn не выпускается → Fabric-моды
    под 26.x собираются на **официальных маппингах Mojang**.

## С чего начать

1. **Определи платформу**: Java (мод/плагин) или Bedrock (аддон).
2. Открой [карту знаний](knowledge/knowledge-map.md) — выбери ядро и тип.
3. Возьми шаблон из `templates/<тип>/` (репозиторий на GitHub).
4. Подставь свои `MOD_ID`/`group`, версии и пакет.
5. Собери: `gradle build` / `mvn package` / zip.
6. Готовый файл — в `build/libs/`, `target/` или `.mcaddon`.

## Разделы

| Раздел | Что внутри |
|---|---|
| [Версии и загрузчики](docs/java/versions.md) | Актуальные версии Minecraft, загрузчиков и библиотек |
| [Обзор загрузчиков](docs/java/loaders.md) | Fabric / NeoForge / Forge / Quilt / Architectury / Paper |
| [Toolchain](docs/java/toolchain.md) | Gradle, JDK, плагины сборки и типовые грабли |
| [Маппинги](docs/java/mappings.md) | Mojang mappings vs Yarn vs Parchment |
| [Миграция на 26.x](docs/java/migration-26x.md) | Перенос мода с 1.21.x на 26.x |
| [Что не собирается](docs/java/unsupported.md) | Реальные проблемы и обходные пути |
| [Матрица совместимости](COMPATIBILITY.md) | Версия ↔ ядро ↔ Gradle ↔ JDK ↔ маппинги |
| [Гайды](guides/from-zero-to-jar.md) | От пустой папки до готового файла |
| [Bedrock](docs/bedrock/addon-structure.md) | Аддоны, скрипты, меню, JSON UI |

## Как обновляются версии

Версии в репозитории **не протухают**: скрипт
[`scripts/refresh_versions.py`](https://github.com/ssr33242/modding-docs/blob/main/scripts/refresh_versions.py)
тянет живые данные с официальных API (Mojang, Fabric meta, Modrinth, NeoForge,
Forge, Quilt, PaperMC) и обновляет [`versions.json`](versions.json).
GitHub Actions запускает его ежедневно.

```bash
python scripts/refresh_versions.py          # обновить
python scripts/refresh_versions.py --check  # только посмотреть
```

## Принципы

- Всё, что помечено «проверено сборкой», **реально собрано**, и в jar есть
  `.class`-файлы.
- Версии берутся из **первоисточников**, а не по памяти.
- `BUILD SUCCESSFUL` **не значит**, что мод рабочий — всегда проверяй jar.

## Зеркала официальной документации

| Документация | Зеркало |
|---|---|
| Fabric | [ssr33242/fabric-docs](https://github.com/ssr33242/fabric-docs) |
| NeoForge | [ssr33242/neoforge-docs](https://github.com/ssr33242/neoforge-docs) |
| Forge | [ssr33242/forge-docs](https://github.com/ssr33242/forge-docs) |

Синхронизируются с оригиналом автоматически, ежедневно.

Лицензия: MIT.
