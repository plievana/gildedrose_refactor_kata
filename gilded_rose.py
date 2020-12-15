# -*- coding: utf-8 -*-
from typing import Sequence
from item import Item


AGED_BRIE: str = "Aged Brie"
BACKSTAGE_PASSES: str = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS: str = "Sulfuras, Hand of Ragnaros"

AGED_BRIE_DOUBLE_QUALITY_DECREMENT_SELL_IN_THRESHOLD: int = 0

BACKSTAGE_PASSES_DOUBLE_QUALITY_INCREASE_SELL_IN_THRESHOLD: int = 10
BACKSTAGE_PASSES_TRIPLE_QUALITY_INCREASE_SELL_IN_THRESHOLD: int = 5
BACKSTAGE_PASSES_QUALITY_RESET_SELL_IN_THRESHOLD: int = 0

DEFAULT_ITEM_DOUBLE_QUALITY_DECREASE_SELL_IN_THRESHOLD: int = 0

MAX_QUALITY: int = 50
MIN_QUALITY: int = 0


class GildedRose(object):

    def __init__(self, items: Sequence[Item]):
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            if item.name == AGED_BRIE:
                self.decrease_sell_in(item)
                self.update_aged_brie_quality(item)
            elif item.name == BACKSTAGE_PASSES:
                self.decrease_sell_in(item)
                self.update_backstage_passes_quality(item)
            elif item.name == SULFURAS:
                pass
            else:
                self.decrease_sell_in(item)
                self.update_default_item_quality(item)
                
    def decrease_sell_in(self, item: Item) -> None:
        item.sell_in -= 1

    def update_aged_brie_quality(self, item: Item) -> None:
        self.increase_quality(item)

        if item.sell_in < AGED_BRIE_DOUBLE_QUALITY_DECREMENT_SELL_IN_THRESHOLD:
            self.increase_quality(item)

    def update_backstage_passes_quality(self, item: Item) -> None:
        self.increase_quality(item)

        if item.sell_in < BACKSTAGE_PASSES_DOUBLE_QUALITY_INCREASE_SELL_IN_THRESHOLD:
            self.increase_quality(item)
        
        if item.sell_in < BACKSTAGE_PASSES_TRIPLE_QUALITY_INCREASE_SELL_IN_THRESHOLD:
            self.increase_quality(item)

        if item.sell_in < BACKSTAGE_PASSES_QUALITY_RESET_SELL_IN_THRESHOLD:
            self.reset_quality(item)
        
    def update_default_item_quality(self, item: Item):
        self.decrease_quality(item)

        if item.sell_in < DEFAULT_ITEM_DOUBLE_QUALITY_DECREASE_SELL_IN_THRESHOLD:
            self.decrease_quality(item)
        
    def reset_quality(self, item:Item) -> None:
        item.quality = 0

    def increase_quality(self, item: Item) -> None:
        if item.quality < MAX_QUALITY:
            item.quality += 1

    def decrease_quality(self, item: Item) -> None:
        if item.quality > MIN_QUALITY:
            item.quality -= 1
