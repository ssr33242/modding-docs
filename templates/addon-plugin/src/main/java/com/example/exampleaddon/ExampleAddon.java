package com.example.exampleaddon;

import net.kyori.adventure.text.Component;
import net.kyori.adventure.text.format.NamedTextColor;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.plugin.Plugin;
import org.bukkit.plugin.java.JavaPlugin;
import org.jetbrains.annotations.NotNull;

/**
 * Пример аддона-плагина: расширяет другой плагин (хост).
 *
 * Ключевое:
 *   - хост объявлен в plugin.yml через depend/softdepend;
 *   - обращаемся к хосту только если он реально загружен;
 *   - используем публичный API хоста, не лезем во внутренности.
 */
public final class ExampleAddon extends JavaPlugin {

    private Plugin host;

    @Override
    public void onEnable() {
        // Проверяем наличие хоста (для softdepend — обязательно)
        host = getServer().getPluginManager().getPlugin("LuckPerms");
        if (host == null) {
            getLogger().warning("Хост-плагин LuckPerms не найден — аддон работает в урезанном режиме.");
        } else {
            getLogger().info("Аддон подключён к хосту: " + host.getName()
                    + " v" + host.getPluginMeta().getVersion());
        }

        if (getCommand("exampleaddon") != null) {
            getCommand("exampleaddon").setExecutor(this);
        }
    }

    @Override
    public boolean onCommand(@NotNull CommandSender sender,
                             @NotNull Command command,
                             @NotNull String label,
                             String @NotNull [] args) {
        if (!command.getName().equalsIgnoreCase("exampleaddon")) {
            return false;
        }

        if (host == null) {
            sender.sendMessage(Component.text("Хост-плагин недоступен.", NamedTextColor.RED));
            return true;
        }

        sender.sendMessage(Component.text("Аддон работает вместе с " + host.getName(),
                NamedTextColor.GREEN));
        // Здесь был бы вызов публичного API хоста:
        //   LuckPerms api = LuckPermsProvider.get();
        //   ... api.getUserManager().loadUser(uuid) ...
        return true;
    }
}
