from . import Item
from .fields.name import ItemName
from .fields.sell_in import ItemSellIn
from .fields.quality import ItemQuality


DOUBLE_QUALITY_DECREMENT_SELL_IN_THRESHOLD: int = 0

class AgedBrie(Item):
    def __init__(self, name: ItemName, sell_in: ItemSellIn, quality: ItemQuality):
        super(AgedBrie, self).__init__(name, sell_in, quality)
    

    def update(self):
        self.decrease_sell_in()
        self.increase_quality()

        if self.has_to_be_sold_in_less_than(DOUBLE_QUALITY_DECREMENT_SELL_IN_THRESHOLD):
            self.increase_quality()
