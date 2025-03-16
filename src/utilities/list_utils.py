from typing import List


def flatten_list_of_lists(two_dimensional_list: List[list]) -> list:
    """
    Flattens the items in a list of list into a singular list with list comprehension.

    args:
        two_dimensional_list: a list of lists

    return:
        returns a list
    """

    flattened_list = [item for list_item in two_dimensional_list for item in list_item]
    return flattened_list
