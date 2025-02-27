# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemStrategy:
    def update(self, item):
        raise NotImplementedError("Subclass must implement abstract method")

class NormalItemStrategy(ItemStrategy):
    def update(self, item):
        item.sell_in -= 1
        if item.quality > 0:
            item.quality -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1

class AgedBrieStrategy(ItemStrategy):
    def update(self, item):
        item.sell_in -= 1
        if item.quality < 50:
            item.quality += 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1

class SulfurasStrategy(ItemStrategy):
    def update(self, item):
        item.sell_in -= 1
        item.quality = item.quality 

class BackstagePassStrategy(ItemStrategy):
    def update(self, item):
        if item.sell_in > 10:
            item.quality += 1
        elif 5 < item.sell_in <= 10:
            item.quality += 2
        elif 0 < item.sell_in <= 5:
            item.quality += 3
        else:
            item.quality = 0
        if item.quality > 50:
            item.quality = 50
        item.sell_in -= 1

def get_item_strategy(item):
    if item.name == "Aged Brie":
        return AgedBrieStrategy()
    elif item.name == "Backstage passes to a TAFKAL80ETC concert":
        return BackstagePassStrategy()
    elif item.name.strip().lower() in ["sulfuras", "sulfuras, hand of ragnaros"]:
        return SulfurasStrategy()
    else:
        return NormalItemStrategy()

class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            strategy = get_item_strategy(item)
            strategy.update(item)
