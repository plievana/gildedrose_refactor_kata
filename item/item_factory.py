from . import Item
from .aged_brie import AgedBrie
from .backstage_passes import BackstagePasses
from .sulfuras import Sulfuras
from .standard_item import StandardItem
from .fields.name import ItemName
from .fields.sell_in import ItemSellIn
from .fields.quality import ItemQuality

class ItemFactory:
    
    @staticmethod
    def based_on(name: str, sell_in: int, quality: int) -> Item:
        name: ItemName = ItemName(name)
        sell_in: ItemSellIn = ItemSellIn(sell_in)
        quality: ItemQuality = ItemQuality(quality)

        if name.is_aged_brie():
             return AgedBrie(name, sell_in, quality)
        
        if name.is_backstage_passes():
            return BackstagePasses(name, sell_in, quality)
        
        if name.is_sulfuras():
             return Sulfuras(name, sell_in, quality)

        return StandardItem(name, sell_in, quality)
 