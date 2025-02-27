# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_item()
        self.assertEqual(["Sulfuras"], all_items)

    # logical error tests
    def test_normal_item_quality_decreases(self):
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].quality, "Normal item quality should decrease by 1")

    def test_backstage_passes_quality_increase(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 9, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality, "Backstage passes quality should increase by 2 when 10 days or less")

    def test_quality_never_above_50(self):
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality, "Quality should never be above 50")

    def test_quality_never_negative(self):
        items = [Item("Normal Item", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality, "Item quality should never be negative")

    # syntax error tests
    def test_unimplemented_feature(self):
        items = [Item("Normal Item", 5, 10)]
        gilded_rose = GildedRose(items)
        with self.assertRaises(AttributeError, msg="Calling an unimplemented feature should raise AttributeError"):
            gilded_rose.unimplemented_feature()

    def test_accessing_unimplemented_property(self):
        items = [Item("Aged Brie", 10, 20)]
        with self.assertRaises(AttributeError, msg="Accessing an unimplemented property should raise AttributeError"):
            _ = items[0].unimplemented_property

    def test_item_initialization_invalid_type(self):
        with self.assertRaises(TypeError, msg="Initializing Item with invalid argument types should raise TypeError"):
            Item(name=123, sell_in="ten", quality=None)

    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        with self.assertRaises(AttributeError, msg="Calling a non-existent method should raise AttributeError"):
            _ = gilded_rose.get_item()

if __name__ == '__main__':
    unittest.main()
