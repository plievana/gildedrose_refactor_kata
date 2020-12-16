from . import Item
from .fields.name import ItemName
from .fields.sell_in import ItemSellIn
from .fields.quality import ItemQuality

class Sulfuras(Item):
    def __init__(self, name: ItemName, sell_in: ItemSellIn, quality: ItemQuality):
        super(Sulfuras, self).__init__(name, sell_in, quality)
    

    def update(self):
        pass
