from typing import Dict, List


def convert_into_KMPH(data: float) -> float:
    """Manipulates the data so it can be displayed as MPH

    Args:
        data (float): None-empty variable

    Returns:
        float: Value that can be represented as MPH to one decimal place
    """
    formula = data * 1.609
    return round(formula, 1)


def convert_into_MPH(data: float) -> float:
    """Manipulates the data so it can be displayed as KM/H

    Args:
        data (float): None-empty variable

    Returns:
        float: Value that can be represented as KM/H to one decimal place
    """
    formula = data / 1.609
    return round(formula, 1)


def get_smallest_value(values: Dict[int, float]) -> int:
    """Gets the smallest float value within a dictionary

    Args:
        values (Dict[int, float]): Dictionary full of values

    Returns:
        int: Returns the Key of the lowest value within the Dictionary
    """
    return min(values, key=values.get)


def get_largest_value(values: Dict[int, float]) -> int:
    """Gets the largest float value within a dictionary

    Args:
        values (Dict[int, float]): Dictionary full of values

    Returns:
        int: Returns the Key of the largest value within the Dictionary
    """
    return max(values, key=values.get)


def get_mode_of_dictionary(possible_values: Dict[int, float]) -> float:
    """Calculates the average of all values in the dictionary

    Args:
        values (Dict[int,float]): None-empty Dictionary

    Returns:
        float: A float average of the dictionary's values to one decimal place
    """
    all_values = list(possible_values.values())
    average = round(sum(all_values) / len(all_values), 1)
    return average
