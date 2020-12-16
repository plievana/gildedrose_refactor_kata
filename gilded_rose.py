# -*- coding: utf-8 -*-
from typing import Sequence
from item import Item

class GildedRose(object):

    def update_quality(self, items: Sequence[Item]) -> None:
        for item in items:
            item.update()
