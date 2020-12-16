from . import Item
from .updatable_item import UpdatableItem

DOUBLE_QUALITY_DECREMENT_SELL_IN_THRESHOLD: int = 0

class AgedBrie(UpdatableItem):
    def __init__(self, item: Item):
        super(AgedBrie, self).__init__(item)
    

    def update(self):
        self.decrease_sell_in()
        self.increase_quality()

        if self.sell_in_f() < DOUBLE_QUALITY_DECREMENT_SELL_IN_THRESHOLD:
            self.increase_quality()
