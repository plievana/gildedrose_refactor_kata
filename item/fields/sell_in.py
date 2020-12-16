

class ItemSellIn:
    __slots__ = ('value',)

    def __init__(self, v: int):
        self.value = v
    
    def decrease(self) -> 'ItemSellIn':
        return ItemSellIn(self.value - 1)
    
    def is_less_than(self, days: int) -> bool:
        return self.value < days
    
    def __eq__(self, o):
        if not isinstance(o, ItemSellIn):
            return False
        
        return self.value == o.value
    