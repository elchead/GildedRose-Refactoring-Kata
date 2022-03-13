import pytest
from gilded_rose import *


def test_zero_never_negative():
    items = [Item("neg", 0, 0)]

    sut = GildedRose(items)
    sut.update_quality()
    assert sut.items[0].quality == 0
