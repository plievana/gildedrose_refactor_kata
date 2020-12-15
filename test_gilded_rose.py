# -*- coding: utf-8 -*-
import unittest

from item import Item
from gilded_rose import GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_that_sell_in_value_is_decreased(self):
        whatever_item: Item = Item("whatever", 10, 0)

        gilded_rose: GildedRose = GildedRose([whatever_item])
        gilded_rose.update_quality()

        self.assertEquals(whatever_item.sell_in, 9)

    def test_that_quality_value_is_decreased(self):
        whatever_item: Item = Item("whatever", 1, 10)

        gilded_rose: GildedRose = GildedRose([whatever_item])
        gilded_rose.update_quality()

        self.assertEquals(whatever_item.quality, 9)

    def test_that_quality_decreases_twice_as_much_when_sell_by_is_passed(self):
        whatever_item: Item = Item("whatever", 0, 10)

        gilded_rose: GildedRose = GildedRose([whatever_item])
        gilded_rose.update_quality()

        self.assertEquals(whatever_item.quality, 8)

    def test_that_quality_is_never_negative(self):
        whatever_item: Item = Item("whatever", 0, 0)

        gilded_rose: GildedRose = GildedRose([whatever_item])
        gilded_rose.update_quality()

        self.assertEquals(whatever_item.quality, 0)

    def test_aged_brie_increases_quality_with_age(self):
        aged_brie: Item  = Item("Aged Brie", 5, 1)

        gilded_rose: GildedRose = GildedRose([aged_brie])
        gilded_rose.update_quality()

        self.assertEquals(aged_brie.quality, 2)

    def test_quality_never_increases_past_fifty(self):
        aged_brie: Item = Item("Aged Brie", 5, 50) 

        gilded_rose: GildedRose = GildedRose([aged_brie])
        gilded_rose.update_quality()

        self.assertEquals(aged_brie.quality, 50)

    def test_sulfuras_never_changes(self):
        sulfuras: Item = Item("Sulfuras, Hand of Ragnaros", 0, 25)

        gilded_rose: GildedRose = GildedRose([sulfuras])
        gilded_rose.update_quality()

        self.assertEquals(sulfuras.quality, 25)
        self.assertEquals(sulfuras.sell_in, 0)
    
    def  test_backstage_pass_increases_quality_by_one_if_sell_by_greater_then_ten(self):
        backstage_passes: Item = Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)

        gilded_rose: GildedRose = GildedRose([backstage_passes])
        gilded_rose.update_quality()

        self.assertEquals(backstage_passes.quality, 21)

    def test_backstage_pass_increases_quality_by_two_if_sell_by_smaller_than_ten(self):
        backstage_passes: Item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 20)

        gilded_rose: GildedRose = GildedRose([backstage_passes])
        gilded_rose.update_quality()

        self.assertEquals(backstage_passes.quality, 22)
    
    def test_backstage_pass_increases_quality_by_three_if_sell_by_smaller_than_five(self):
        backstage_passes: Item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)

        gilded_rose: GildedRose = GildedRose([backstage_passes])
        gilded_rose.update_quality()

        self.assertEquals(backstage_passes.quality, 23)
    
    def test_backstage_pass_loses_value_after_sell_by_passes(self):
        backstage_passes: Item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)

        gilded_rose: GildedRose = GildedRose([backstage_passes])
        gilded_rose.update_quality()

        self.assertEquals(backstage_passes.quality, 0)
    
if __name__ == '__main__':
    unittest.main()