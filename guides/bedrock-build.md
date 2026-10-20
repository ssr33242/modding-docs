# Сборка аддона Bedrock

Аддон — это два пакета (behavior + resource), упакованные в `.mcaddon`.

## Порядок сборки вручную

1. Собрать папки `behavior_packs/example_bp/` и `resource_packs/example_rp/`.
2. Проверить `manifest.json`: уникальные UUID, присутствуют `modules`.
3. Упаковать **содержимое** пакетов (не самих папок) в zip.
4. Переименовать `example.zip` → `ExampleAddon.mcaddon`.
5. Открыть файл — Minecraft импортирует пакеты.
6. В мире включить оба набора: «Наборы ресурсов» и «Наборы поведения».
7. Включить «Beta APIs», если используются скрипты.

## Автоматическая сборка (Python)

```python
import zipfile
from pathlib import Path

ROOT = Path("my_addon")

def pack(src_dir: Path, out: Path) -> None:
    """Упаковать папку-пакет (.mcpack): содержимое внутрь zip."""
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in src_dir.rglob("*"):
            if p.is_file():
                z.write(p, p.relative_to(src_dir))

# Один пакет
pack(ROOT / "behavior_packs" / "example_bp", Path("example_bp.mcpack"))
pack(ROOT / "resource_packs" / "example_rp", Path("example_rp.mcpack"))

# Полный аддон (.mcaddon) — оба пакета в одном zip
with zipfile.ZipFile("ExampleAddon.mcaddon", "w", zipfile.ZIP_DEFLATED) as z:
    for base in ("behavior_packs", "resource_packs"):
        for p in (ROOT / base).rglob("*"):
            if p.is_file():
                z.write(p, p.relative_to(ROOT))
```

## Генерация UUID для manifest.json

```python
import uuid
print(uuid.uuid4())   # один вызов — один уникальный UUID
```

Нужно минимум 3 UUID: header BP, module BP, header RP, module RP (при скрипте — ещё один).

## Куда ставить для теста (Windows Bedrock)

- `%LOCALAPPDATA%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang`
  - `development_behavior_packs\example_bp\`
  - `development_resource_packs\example_rp\`
- Правки подхватываются без переустановки — удобно для отладки.

## Проверка результата

1. Открыть мир с аддоном.
2. Проверить: `/give @s example:ruby`, `/setblock ~ ~ ~ example:ruby_block`,
   `/summon example:guardian_pet`.
3. Рецепт — крафт 3×3 из рубинов даёт рубиновый блок.
4. Скрипт — при входе игрока приходит приветствие в чат.
5. Если что-то не работает — «Настройки» → «Создатель» → «Логи контента».
