AGED_BRIE: str = "Aged Brie"
BACKSTAGE_PASSES: str = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS: str = "Sulfuras, Hand of Ragnaros"

class ItemName:
    __slots__ = ('value',)
    def __init__(self, value: str):
        self.value = value

    def is_aged_brie(self) -> bool:
        return AGED_BRIE == self.value
    

    def is_backstage_passes(self) -> bool:
        return BACKSTAGE_PASSES == self.value
    
    def is_sulfuras(self) -> bool:
        return SULFURAS == self.value

    def __eq__(self, o):
        if not isinstance(o, ItemName):
            return False
        return o.value == self.value
