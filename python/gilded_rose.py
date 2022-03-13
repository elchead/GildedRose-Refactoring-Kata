# -*- coding: utf-8 -*-
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


def _base_update(item: Item, quality_inc: int):
    item.sell_in -= 1
    item.quality += quality_inc
    item.quality = max(min(item.quality, 50), 0)


class Sulfuras:
    def __init__(self, item: Item):
        self.item = item

    def update_quality(self):
        return


class AgedBrie:
    def __init__(self, item: Item):
        self.item = item

    def update_quality(self):
        quality_inc = 1
        if self.item.sell_in <= 0:
            quality_inc = 2
        _base_update(self.item, quality_inc)


class BackstagePasses:
    def __init__(self, item: Item):
        self.item = item

    def update_quality(self):
        quality_inc = 1
        if self.item.sell_in <= 10:
            quality_inc = 2
        if self.item.sell_in <= 5:
            quality_inc = 3
        if self.item.sell_in <= 0:
            quality_inc = -self.item.quality
        _base_update(self.item, quality_inc)


class OtherItems:
    def __init__(self, item: Item):
        self.item = item

    def update_quality(self):
        quality_inc = -1
        if self.item.sell_in <= 0:
            quality_inc = -2
        _base_update(self.item, quality_inc)


def create_smart_item(item: Item):
    if item.name == "Sulfuras, Hand of Ragnaros":
        return Sulfuras(item)
    elif item.name == "Aged Brie":
        return AgedBrie(item)
    elif item.name == "Backstage passes to a TAFKAL80ETC concert":
        return BackstagePasses(item)
    else:
        return OtherItems(item)


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            create_smart_item(item).update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
