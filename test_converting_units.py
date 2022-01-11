import pytest
from converting_units import (
    convert_into_MPH,
    convert_into_KMPH,
    get_smallest_value,
    get_largest_value,
    get_mode_of_dictionary,
)


@pytest.mark.parametrize("mph,expected", [(100, 160.9), (20, 32.2)])
def test_convert_to_KMPH(mph, expected):
    assert convert_into_KMPH(mph) == expected


@pytest.mark.parametrize("kmph,expected", [(100, 62.2), (20, 12.4)])
def test_convert_to_MPH(kmph, expected):
    assert convert_into_MPH(kmph) == expected


@pytest.mark.parametrize(
    "values,expected",
    [({1: 4.0, 2: 2.5}, 2), ({24: 7.0, 12: 15.2}, 24)],
)
def test_get_smallest_value(values, expected):
    assert get_smallest_value(values) == expected


@pytest.mark.parametrize(
    "values,expected",
    [({1: 4.0, 2: 2.5}, 1), ({24: 7.0, 12: 15.2}, 12)],
)
def test_get_largest_value(values, expected):
    assert get_largest_value(values) == expected


@pytest.mark.parametrize(
    "possible_values,expected",
    [({0: 0, 1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90}, 45.0)],
)
def test_get_mode_of_dictionary(possible_values, expected):
    assert get_mode_of_dictionary(possible_values) == expected
