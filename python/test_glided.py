import pytest
from gilded_rose import *


def create_and_update(items):
    sut = GildedRose(items)
    sut.update_quality()


@pytest.mark.parametrize("quality", [0, 1, 2, 3, 50])
def test_never_negative(quality):
    items = [Item("item", 0, quality)]

    create_and_update(items)
    assert items[0].quality >= 0


def test_lower_quality():
    quality = 1
    quality_2 = 2
    items = [Item("item", 10, quality), Item("item", 10, quality_2)]

    create_and_update(items)
    assert items[0].quality == quality - 1
    assert items[1].quality == quality_2 - 1


def test_lower_sellin():
    sellin = 1
    sellin_2 = -1
    items = [Item("item", sellin, 1), Item("item", sellin_2, 10)]

    create_and_update(items)
    assert items[0].sell_in == sellin - 1
    assert items[1].sell_in == sellin_2 - 1


def get_new_quality_with_name(name, old_quality, sellin):
    items = [Item(name, sellin, old_quality)]
    create_and_update(items)
    return items[0].quality


def get_new_quality(old_quality, sellin):
    return get_new_quality_with_name("item", old_quality, sellin)


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
