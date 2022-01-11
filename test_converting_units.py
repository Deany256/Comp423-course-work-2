import pytest
from converting_units import converting_to_MPH, converting_to_KMPH


@pytest.mark.parametrize("mph,kmph,expected", [([100, 50], [], [160.9, 80.5])])
def test_converting_to_KMPH(mph, kmph, expected):
    assert converting_to_KMPH(mph, kmph) == expected


@pytest.mark.parametrize("kmph,mph,expected", [([100], [], [62.2])])
def test_converting_to_MPH(kmph, mph, expected):
    assert converting_to_MPH(kmph, mph) == expected
