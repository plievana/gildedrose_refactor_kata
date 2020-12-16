# -*- coding: utf-8 -*-
from typing import Sequence
import unittest

from item import Item
from item.item_factory import ItemFactory
from item.fields.sell_in import ItemSellIn
from item.fields.quality import ItemQuality
from item.exceptions import ItemQualityOutOfRangeException
from gilded_rose import GildedRose

class GildedRoseTest(unittest.TestCase):
    def list_of(self, item: Item) -> Sequence[Item]:
        return [item]

    def test_that_sell_in_value_is_decreased(self):
        whatever_item: Item = ItemFactory.based_on("whatever", 10, 0)
        
        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(whatever_item))

        expected_sell_in: ItemSellIn = ItemSellIn(9)
        self.assertEqual(whatever_item.sell_in(), expected_sell_in)

    def test_that_quality_value_is_decreased(self):
        whatever_item: Item = ItemFactory.based_on("whatever", 1, 10)
        
        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(whatever_item))

        expected_quality: ItemQuality = ItemQuality(9)
        self.assertEqual(whatever_item.quality(), expected_quality)

    def test_that_quality_decreases_twice_as_much_when_sell_by_is_passed(self):
        whatever_item: Item = ItemFactory.based_on("whatever", 0, 10)
        
        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(whatever_item))

        expected_quality: ItemQuality = ItemQuality(8)
        self.assertEqual(whatever_item.quality(), expected_quality)

    def test_that_quality_is_never_negative(self):
        whatever_item: Item = ItemFactory.based_on("whatever", 0, 0)
        
        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(whatever_item))

        expected_quality: ItemQuality = ItemQuality(0)
        self.assertEqual(whatever_item.quality(), expected_quality)

    def test_aged_brie_increases_quality_with_age(self):
        aged_brie: Item  = ItemFactory.based_on("Aged Brie", 5, 1)
        
        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(aged_brie))

        expected_quality: ItemQuality = ItemQuality(2)
        self.assertEqual(aged_brie.quality(), expected_quality)

    def test_quality_never_increases_past_fifty(self):
        aged_brie: Item = ItemFactory.based_on("Aged Brie", 5, 50)
        
        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(aged_brie))

        expected_quality: ItemQuality = ItemQuality(50)
        self.assertEqual(aged_brie.quality(), expected_quality)

    def test_sulfuras_never_changes(self):
        sulfuras: Item = ItemFactory.based_on("Sulfuras, Hand of Ragnaros", 0, 25)
    
        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(sulfuras))

        expected_quality: ItemQuality = ItemQuality(25)
        expected_sell_in: ItemSellIn = ItemSellIn(0)
        self.assertEqual(sulfuras.quality(), expected_quality)
        self.assertEqual(sulfuras.sell_in(), expected_sell_in)
    
    def test_backstage_pass_increases_quality_by_one_if_sell_by_greater_then_ten(self):
        backstage_passes: Item = ItemFactory.based_on("Backstage passes to a TAFKAL80ETC concert", 11, 20)
        
        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(backstage_passes))

        expected_quality: ItemQuality = ItemQuality(21)
        self.assertEqual(backstage_passes.quality(), expected_quality)

    def test_backstage_pass_increases_quality_by_two_if_sell_by_smaller_than_ten(self):
        backstage_passes: Item = ItemFactory.based_on("Backstage passes to a TAFKAL80ETC concert", 6, 20)
        
        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(backstage_passes))

        expected_quality: ItemQuality = ItemQuality(22)
        self.assertEqual(backstage_passes.quality(), expected_quality)
    
    def test_backstage_pass_increases_quality_by_three_if_sell_by_smaller_than_five(self):
        backstage_passes: Item = ItemFactory.based_on("Backstage passes to a TAFKAL80ETC concert", 5, 20)
        
        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(backstage_passes))

        expected_quality: ItemQuality = ItemQuality(23)
        self.assertEqual(backstage_passes.quality(), expected_quality)
    
    def test_backstage_pass_loses_value_after_sell_by_passes(self):
        backstage_passes: Item = ItemFactory.based_on("Backstage passes to a TAFKAL80ETC concert", 0, 20)
        
        gilded_rose: GildedRose = GildedRose()
        gilded_rose.update_quality(self.list_of(backstage_passes))

        expected_quality: ItemQuality = ItemQuality(0)
        self.assertEqual(backstage_passes.quality(), expected_quality)
    
    def test_quality_does_not_allow_values_below_zero(self):
        with self.assertRaises(ItemQualityOutOfRangeException):
            ItemQuality(-1)

    def test_quality_does_not_allow_values_over_fifty(self):
        with self.assertRaises(ItemQualityOutOfRangeException):
            ItemQuality(51)
            
if __name__ == '__main__':
    unittest.main()