package com.example.examplemod;

import net.minecraft.item.Item;
import net.minecraft.item.ItemGroups;
import net.minecraft.item.BlockItem;
import net.minecraft.block.Block;
import net.minecraft.block.AbstractBlock;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.util.Identifier;
import org.quiltmc.loader.api.ModContainer;
import org.quiltmc.loader.api.ModInitializer;
import org.quiltmc.qsl.item.group.api.QuiltItemGroup;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ExampleMod implements ModInitializer {
    public static final String MOD_ID = "examplemod";
    public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);

    public static final Block RUBY_BLOCK = new Block(
            AbstractBlock.Settings.create().strength(4.0F));
    public static final Item RUBY = new Item(new Item.Settings());

    @Override
    public void onInitialize(ModContainer mod) {
        Registry.register(Registries.BLOCK, id("ruby_block"), RUBY_BLOCK);
        Registry.register(Registries.ITEM, id("ruby_block"),
                new BlockItem(RUBY_BLOCK, new Item.Settings()));
        Registry.register(Registries.ITEM, id("ruby"), RUBY);

        LOGGER.info("ExampleMod инициализирован на Quilt");
    }

    public static Identifier id(String path) {
        return new Identifier(MOD_ID, path);
    }
}
