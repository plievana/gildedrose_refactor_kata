from abc import abstractmethod
from .fields.name import ItemName
from .fields.sell_in import ItemSellIn
from .fields.quality import ItemQuality


class Item:
    __slots__ = ('_name', '_sell_in', '_quality')
    
    def __init__(self, name: ItemName, sell_in: ItemSellIn, quality: ItemQuality):
        self._name = name
        self._sell_in = sell_in
        self._quality = quality
    

    @abstractmethod
    def update(self)->None:
        pass

    def sell_in(self)->ItemSellIn:
        return self._sell_in
    

    def quality(self)->ItemQuality:
        return self._quality
    
    def decrease_sell_in(self)->None:
        self._sell_in = self._sell_in.decrease()
    
    def has_to_be_sold_in_less_than(self, days: int)->bool:
        return self._sell_in.is_less_than(days)
    
    def increase_quality(self)->None:
        self._quality = self._quality.increase()
    
    def decrease_quality(self)->None:
        self._quality = self._quality.decrease()
    
    def reset_quality(self)->None:
        self._quality = self._quality.reset()
    
    def __repr__(self):
        return f'{self._name}, {self._sell_in}, {self._quality}'
