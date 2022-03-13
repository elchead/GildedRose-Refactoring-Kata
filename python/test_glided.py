import pytest
from gilded_rose import *


def get_new_quality_with_name(name, old_quality, sellin):
    items = [Item(name, sellin, old_quality)]
    create_and_update(items)
    return items[0].quality


def get_new_sellin_with_name(name, quality, sellin):
    items = [Item(name, sellin, quality)]
    create_and_update(items)
    return items[0].sell_in


def get_new_quality(old_quality, sellin):
    return get_new_quality_with_name("item", old_quality, sellin)


def create_and_update(items):
    sut = GildedRose(items)
    sut.update_quality()


@pytest.mark.parametrize("quality", [0, 1, 2, 3, 50])
def test_never_negative(quality):
    assert get_new_quality(quality, 2) >= 0


def test_lower_quality():
    quality = 1
    quality_2 = 2
    assert get_new_quality(quality, 10) == quality - 1
    assert get_new_quality(quality_2, 10) == quality_2 - 1


def test_lower_sellin_with_multiple_items():
    sellin = 1
    sellin_2 = -1
    items = [Item("item", sellin, 1), Item("item", sellin_2, 10)]
    create_and_update(items)
    assert items[0].sell_in == sellin - 1
    assert items[1].sell_in == sellin_2 - 1


class TestDegradeTwiceAsFast:
    def test_happy_path(self):
        quality = 10
        assert get_new_quality(quality, 0) == quality - 2

    def test_negative_sellin(self):
        quality = 10
        assert get_new_quality(quality, -2) == quality - 2

    def test_quality_never_negative(self):
        quality = 1
        assert get_new_quality(quality, 0) == 0

    def test_brie_increases(self):
        quality = 10
        assert get_new_quality_with_name("Aged Brie", quality, -1) == quality + 2


def test_brie_increases_value():
    quality = 10
    assert get_new_quality_with_name("Aged Brie", quality, 2) == quality + 1


def test_brie_never_beyond_50():
    quality = 50
    assert get_new_quality_with_name("Aged Brie", quality, 2) == quality


def test_sulfuras_never_decreases_quality():
    quality = 80
    assert get_new_quality_with_name("Sulfuras, Hand of Ragnaros", quality, 2) == quality


def test_sulfuras_never_decreases_sellin():
    sellin = 10
    assert get_new_sellin_with_name("Sulfuras, Hand of Ragnaros", 80, sellin) == sellin


class TestBackstage:
    name = "Backstage passes to a TAFKAL80ETC concert"
    quality = 10

    def test_always_increases_quality(self):
        assert get_new_quality_with_name(self.name, self.quality, 15) == self.quality + 1

    @pytest.mark.parametrize("sellin", [6, 8, 10])
    def test_increase_by_2_when_10_days(self, sellin):
        assert get_new_quality_with_name(self.name, self.quality, sellin) == self.quality + 2

    @pytest.mark.parametrize("sellin", [1, 3, 5])
    def test_increase_by_3_when_leq5_days(self, sellin):
        assert get_new_quality_with_name(self.name, self.quality, sellin) == self.quality + 3

    def test_after_concert(self):
        assert get_new_quality_with_name(self.name, self.quality, 0) == 0
