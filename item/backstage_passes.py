from . import Item
from .fields.name import ItemName
from .fields.sell_in import ItemSellIn
from .fields.quality import ItemQuality

DOUBLE_QUALITY_INCREASE_SELL_IN_THRESHOLD: int = 10
TRIPLE_QUALITY_INCREASE_SELL_IN_THRESHOLD: int = 5
QUALITY_RESET_SELL_IN_THRESHOLD: int = 0

class BackstagePasses(Item):

    def __init__(self, name: ItemName, sell_in: ItemSellIn, quality: ItemQuality):
        super(BackstagePasses, self).__init__(name, sell_in, quality)
    
    
    def update(self):
        self.decrease_sell_in()
        self.increase_quality()

        if self.has_to_be_sold_in_less_than(DOUBLE_QUALITY_INCREASE_SELL_IN_THRESHOLD):
            self.increase_quality()
        
        if self.has_to_be_sold_in_less_than(TRIPLE_QUALITY_INCREASE_SELL_IN_THRESHOLD):
            self.increase_quality()
        
        if self.has_to_be_sold_in_less_than(QUALITY_RESET_SELL_IN_THRESHOLD):
            self.reset_quality()
