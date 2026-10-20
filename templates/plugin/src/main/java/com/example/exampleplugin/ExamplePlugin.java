package com.example.exampleplugin;

import net.kyori.adventure.text.Component;
import net.kyori.adventure.text.format.NamedTextColor;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerJoinEvent;
import org.bukkit.plugin.java.JavaPlugin;
import org.jetbrains.annotations.NotNull;

public final class ExamplePlugin extends JavaPlugin implements Listener {

    @Override
    public void onEnable() {
        // Создать config.yml из ресурсов, если его нет
        saveDefaultConfig();

        // Зарегистрировать команду (должна быть объявлена в plugin.yml!)
        if (getCommand("example") != null) {
            getCommand("example").setExecutor(this);
        }

        // Зарегистрировать слушателя событий
        getServer().getPluginManager().registerEvents(this, this);

        getLogger().info("ExamplePlugin включён. Версия: " + getPluginMeta().getVersion());
    }

    @Override
    public void onDisable() {
        getLogger().info("ExamplePlugin выключен.");
    }

    @Override
    public boolean onCommand(@NotNull CommandSender sender,
                             @NotNull Command command,
                             @NotNull String label,
                             String @NotNull [] args) {
        if (!command.getName().equalsIgnoreCase("example")) {
            return false;
        }

        String greeting = getConfig().getString("greeting", "Привет из плагина!");

        if (args.length == 0) {
            sender.sendMessage(Component.text(greeting, NamedTextColor.GREEN));
            return true;
        }

        switch (args[0].toLowerCase()) {
            case "info" -> sender.sendMessage(Component.text(
                    "ExamplePlugin v" + getPluginMeta().getVersion(), NamedTextColor.AQUA));
            case "player" -> {
                if (sender instanceof Player player) {
                    player.sendMessage(Component.text("Ты игрок: " + player.getName(),
                            NamedTextColor.YELLOW));
                } else {
                    sender.sendMessage(Component.text("Команда только для игроков.",
                            NamedTextColor.RED));
                }
            }
            default -> sender.sendMessage(Component.text("Неизвестный аргумент: " + args[0],
                    NamedTextColor.RED));
        }
        return true;
    }

    @EventHandler
    public void onPlayerJoin(PlayerJoinEvent event) {
        Player player = event.getPlayer();
        String welcome = getConfig().getString("welcome", "Добро пожаловать, %player%!");
        player.sendMessage(Component.text(
                welcome.replace("%player%", player.getName()), NamedTextColor.GOLD));
    }
}
