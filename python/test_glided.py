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
    pass
