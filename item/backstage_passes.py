from . import Item
from .updatable_item import UpdatableItem

DOUBLE_QUALITY_INCREASE_SELL_IN_THRESHOLD: int = 10
TRIPLE_QUALITY_INCREASE_SELL_IN_THRESHOLD: int = 5
QUALITY_RESET_SELL_IN_THRESHOLD: int = 0

class BackstagePasses(UpdatableItem):

    def __init__(self, item: Item):
        super(BackstagePasses, self).__init__(item)
    
    
    def update(self):
        self.decrease_sell_in()
        self.increase_quality()

        if self.sell_in_f() < DOUBLE_QUALITY_INCREASE_SELL_IN_THRESHOLD:
            self.increase_quality()
        
        if self.sell_in_f() < TRIPLE_QUALITY_INCREASE_SELL_IN_THRESHOLD:
            self.increase_quality()
        
        if self.sell_in_f() < QUALITY_RESET_SELL_IN_THRESHOLD:
            self.reset_quality()
