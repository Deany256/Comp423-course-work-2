from typing import List


def converting_to_KMPH(mph: List[float], kmph: List[float]) -> float:

    """Multiply a list of values by a set value

    Args:
        mph (List[float]): Non-empty list of numbers
        kmph (List[float]): an empty list

    Returns:
        float: List of numbers
    """
    for i in range(len(mph)):
        formula = mph[i] * 1.609
        kmph.append(round(formula, 1))
    return kmph


def converting_to_MPH(kmph: List[float], mph: List[float]) -> float:

    """Multiply a list of values by a set value

    Args:
        kmph (List[float]): Non-empty list of numbers
        mph (List[float]): an empty list

    Returns:
        float: List of numbers
    """
    for i in range(len(kmph)):
        formula = kmph[i] / 1.609
        mph.append(round(formula, 1))
    return mph
