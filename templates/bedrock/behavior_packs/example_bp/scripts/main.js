// scripts/main.js — точка входа Script API для аддона Bedrock.
// Требуется включённая настройка "Beta APIs" в мире.

import { world, system } from "@minecraft/server";

world.afterEvents.playerSpawn.subscribe((event) => {
    if (event.initialSpawn) {
        event.player.sendMessage("§aДобро пожаловать на сервер! §7Аддон Example активен.");
    }
});

// Приветствие при получении рубина: пример работы с предметами.
world.afterEvents.itemUse.subscribe((event) => {
    if (event.itemStack?.typeId === "example:ruby") {
        event.source.sendMessage("§cТы держишь рубин — редкий минерал!");
        event.source.runCommand("playsound random.orb @s");
    }
});

// Пример периодической задачи: раз в 30 секунд сообщаем время игрокам.
system.runInterval(() => {
    const time = world.getTimeOfDay();
    for (const player of world.getAllPlayers()) {
        player.onScreenDisplay.setActionBar(`§eВремя в мире: §f${time}`);
    }
}, 600);

world.afterEvents.entityHurt.subscribe((event) => {
    const hurt = event.hurtEntity;
    if (hurt?.typeId === "example:guardian_pet") {
        world.sendMessage("§cТвой питомец-хранитель ранен!");
    }
});
