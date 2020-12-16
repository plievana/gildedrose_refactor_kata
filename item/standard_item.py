from . import Item
from .fields.name import ItemName
from .fields.sell_in import ItemSellIn
from .fields.quality import ItemQuality

DOUBLE_QUALITY_DECREASE_SELL_IN_THRESHOLD: int = 0

class StandardItem(Item):
    def __init__(self, name: ItemName, sell_in: ItemSellIn, quality: ItemQuality):
        super(StandardItem, self).__init__(name, sell_in, quality)
    
    def update(self) -> None:
        self.decrease_sell_in()
        self.decrease_quality()

        if self.has_to_be_sold_in_less_than(DOUBLE_QUALITY_DECREASE_SELL_IN_THRESHOLD):
            self.decrease_quality()
        