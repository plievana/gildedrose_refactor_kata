from .updatable_item import UpdatableItem
from . import Item

DOUBLE_QUALITY_DECREASE_SELL_IN_THRESHOLD: int = 0

class StandardItem(UpdatableItem):
    def __init__(self, item: Item):
        super(StandardItem, self).__init__(item)
    
    def update(self) -> None:
        self.decrease_sell_in()
        self.decrease_quality()

        if self.sell_in_f() < DOUBLE_QUALITY_DECREASE_SELL_IN_THRESHOLD:
            self.decrease_quality()
        