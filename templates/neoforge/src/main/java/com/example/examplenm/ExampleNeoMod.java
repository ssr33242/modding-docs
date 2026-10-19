package com.example.examplenm;

import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.Item;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.fml.common.Mod;
import net.neoforged.neoforge.registries.DeferredHolder;
import net.neoforged.neoforge.registries.DeferredItem;
import net.neoforged.neoforge.registries.DeferredRegister;

@Mod(ExampleNeoMod.MOD_ID)
public class ExampleNeoMod {
    public static final String MOD_ID = "examplenm";

    public static final DeferredRegister.Items ITEMS =
            DeferredRegister.createItems(MOD_ID);

    public static final DeferredItem<Item> RUBY =
            ITEMS.registerSimpleItem("ruby", new Item.Properties());

    public ExampleNeoMod(IEventBus modEventBus) {
        ITEMS.register(modEventBus);
    }
}
