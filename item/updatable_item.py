from abc import abstractmethod

from . import Item

MAX_QUALITY: int = 50
MIN_QUALITY: int = 0


class UpdatableItem(Item):
    __slots__ = ('item',)

    def __init__(self, item: Item):
        super(UpdatableItem, self).__init__(item.name, item.sell_in, item.quality)
        self.item = item
    

    @abstractmethod
    def update(self) -> None:
        pass

    def sell_in_f(self) -> int:
        return self.item.sell_in

    def decrease_sell_in(self) -> None:
        self.item.sell_in -= 1
    
    def increase_quality(self) -> None:
        if self.item.quality < MAX_QUALITY:
            self.item.quality += 1
        
    def decrease_quality(self) -> None:
        if self.item.quality > MIN_QUALITY:
            self.item.quality -= 1
        

    def reset_quality(self) -> None:
        self.item.quality = 0
