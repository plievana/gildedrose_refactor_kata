# -*- coding: utf-8 -*-
from typing import Sequence
from item.updatable_item import UpdatableItem


class GildedRose(object):

    def update_quality(self, items: Sequence[UpdatableItem]) -> None:
        for item in items:
            item.update()
