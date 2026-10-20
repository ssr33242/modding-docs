// Mystic Pack — скрипт поведения.
// Совместим с @minecraft/server 1.13.0 (стабильный API для 1.21+).
import { world, system } from "@minecraft/server";

// 1) При входе игрока — приветствие в чат.
world.afterEvents.playerSpawn.subscribe((event) => {
  if (!event.initialSpawn) return;
  event.player.sendMessage("§dMystic Pack загружен! §7Проверьте предмет, блок и существо.");
});

// 2) Раз в 5 секунд подлечиваем существ-хранителей поблизости.
system.runInterval(() => {
  const dimensions = ["overworld", "nether", "the_end"];
  for (const dimName of dimensions) {
    let dim;
    try {
      dim = world.getDimension(dimName);
    } catch (e) {
      continue;
    }
    let pets = [];
    try {
      pets = dim.getEntities({ families: ["mystic_pet"] });
    } catch (e) {
      continue;
    }
    for (const pet of pets) {
      try {
        const health = pet.getComponent("minecraft:health");
        if (health && health.currentValue < health.effectiveMax) {
          health.setCurrentValue(Math.min(health.currentValue + 1, health.effectiveMax));
        }
      } catch (e) {
        // компонент недоступен — пропускаем
      }
    }
  }
}, 100);

// 3) При использовании амулета — небольшой эффект и сообщение.
world.afterEvents.itemUse.subscribe((event) => {
  if (!event.itemStack || event.itemStack.typeId !== "mystic:amulet") return;
  const player = event.source;
  try {
    player.addEffect("regeneration", 100, { amplifier: 0 });
    player.sendMessage("§dАмулет пульсирует магией!");
  } catch (e) {
    player.sendMessage("§dАмулет используется.");
  }
});
