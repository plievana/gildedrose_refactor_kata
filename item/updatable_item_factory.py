from typing import Sequence
from . import Item
from .updatable_item import UpdatableItem
from .aged_brie import AgedBrie
from .backstage_passes import BackstagePasses
from .sulfuras import Sulfuras
from .standard_item import StandardItem

AGED_BRIE: str = "Aged Brie"
BACKSTAGE_PASSES: str = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS: str = "Sulfuras, Hand of Ragnaros"

class UpdatableItemFactory:    

    @staticmethod
    def item_to_updatable(item: Item) -> UpdatableItem:
        if item.name == AGED_BRIE:
            return AgedBrie(item)
        if item.name == BACKSTAGE_PASSES:
            return BackstagePasses(item)
        if item.name == SULFURAS:
            return Sulfuras(item)
        
        return StandardItem(item)
        
    @staticmethod
    def list_to_updatable(items: Sequence[Item]) -> Sequence[UpdatableItem]:
        return map(lambda item: UpdatableItemFactory.item_to_updatable(item), items)
