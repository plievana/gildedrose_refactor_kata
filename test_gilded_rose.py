# -*- coding: utf-8 -*-
from typing import Sequence
import unittest

from item import Item
from item.updatable_item import UpdatableItem
from item import updatable_item_factory
from item.updatable_item_factory import UpdatableItemFactory
from gilded_rose import GildedRose

class GildedRoseTest(unittest.TestCase):
    def list_of(self, item: UpdatableItem) -> Sequence[UpdatableItem]:
        return [item]

    def test_that_sell_in_value_is_decreased(self):
        whatever_item: Item = Item("whatever", 10, 0)
        updatable_item = UpdatableItemFactory.item_to_updatable(whatever_item)

        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(updatable_item))

        self.assertEqual(whatever_item.sell_in, 9)

    def test_that_quality_value_is_decreased(self):
        whatever_item: Item = Item("whatever", 1, 10)
        updatable_item = UpdatableItemFactory.item_to_updatable(whatever_item)

        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(updatable_item))

        self.assertEqual(whatever_item.quality, 9)

    def test_that_quality_decreases_twice_as_much_when_sell_by_is_passed(self):
        whatever_item: Item = Item("whatever", 0, 10)
        updatable_item = UpdatableItemFactory.item_to_updatable(whatever_item)

        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(updatable_item))

        self.assertEqual(whatever_item.quality, 8)

    def test_that_quality_is_never_negative(self):
        whatever_item: Item = Item("whatever", 0, 0)
        updatable_item = UpdatableItemFactory.item_to_updatable(whatever_item)

        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(updatable_item))

        self.assertEqual(whatever_item.quality, 0)

    def test_aged_brie_increases_quality_with_age(self):
        aged_brie: Item  = Item("Aged Brie", 5, 1)
        updatable_aged_brie = UpdatableItemFactory.item_to_updatable(aged_brie)

        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(updatable_aged_brie))

        self.assertEqual(aged_brie.quality, 2)

    def test_quality_never_increases_past_fifty(self):
        aged_brie: Item = Item("Aged Brie", 5, 50)
        updatable_aged_brie = UpdatableItemFactory.item_to_updatable(aged_brie)

        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(updatable_aged_brie))

        self.assertEqual(aged_brie.quality, 50)

    def test_sulfuras_never_changes(self):
        sulfuras: Item = Item("Sulfuras, Hand of Ragnaros", 0, 25)
        updatable_sulfuras = UpdatableItemFactory.item_to_updatable(sulfuras)

        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(updatable_sulfuras))

        self.assertEqual(sulfuras.quality, 25)
        self.assertEqual(sulfuras.sell_in, 0)
    
    def  test_backstage_pass_increases_quality_by_one_if_sell_by_greater_then_ten(self):
        backstage_passes: Item = Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)
        updatable_backstage_passes = UpdatableItemFactory.item_to_updatable(backstage_passes)

        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(updatable_backstage_passes))

        self.assertEqual(backstage_passes.quality, 21)

    def test_backstage_pass_increases_quality_by_two_if_sell_by_smaller_than_ten(self):
        backstage_passes: Item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 20)
        updatable_backstage_passes = UpdatableItemFactory.item_to_updatable(backstage_passes)

        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(updatable_backstage_passes))

        self.assertEqual(backstage_passes.quality, 22)
    
    def test_backstage_pass_increases_quality_by_three_if_sell_by_smaller_than_five(self):
        backstage_passes: Item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)
        updatable_backstage_passes = UpdatableItemFactory.item_to_updatable(backstage_passes)

        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(updatable_backstage_passes))

        self.assertEqual(backstage_passes.quality, 23)
    
    def test_backstage_pass_loses_value_after_sell_by_passes(self):
        backstage_passes: Item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)
        updatable_backstage_passes = UpdatableItemFactory.item_to_updatable(backstage_passes)

        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(updatable_backstage_passes))

        self.assertEqual(backstage_passes.quality, 0)
    
if __name__ == '__main__':
    unittest.main()