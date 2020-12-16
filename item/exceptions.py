class ItemQualityOutOfRangeException(Exception):
    def __init__(self, v):
        msg = f'Tried to set an ItemQuality of {v} which is outside the valid range.'
        super(ItemQualityOutOfRangeException, self).__init__(msg)