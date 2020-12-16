from item.exceptions import ItemQualityOutOfRangeException

MAX_VALUE: int = 50
MIN_VALUE: int = 0


class ItemQuality:
    __slots__ = ('value',)
    
    def __init__(self, value: int):
        if value < MIN_VALUE or value > MAX_VALUE:
            raise ItemQualityOutOfRangeException(value)

        self.value = value
    
    def increase(self) -> 'ItemQuality':
        if self.value == MAX_VALUE:
            return self
        
        return ItemQuality(self.value + 1)


    def decrease(self) -> 'ItemQuality':
        if self.value == MIN_VALUE:
            return self
        
        return ItemQuality(self.value - 1)

    def reset(self) -> 'ItemQuality':
        return ItemQuality(MIN_VALUE)

    def __eq__(self, o):
        if not isinstance(o, ItemQuality):
            return False
        return o.value == self.value
