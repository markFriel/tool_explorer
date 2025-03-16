def merge_two_dictionaries(dict1: dict, dict2: dict) -> dict:
    """
    Create a copy of dict1 and merges dict2 into copy. A copy is made to avoid mutating
    dictionary parameters passed in. dict1 and dict2 will remain unchanged.

    args:
        dict1: a dictionary collection
        dict2: a dictionary collection

    return:
        returns a dictionary collection
    """
    new_dictionary = dict1.copy()
    new_dictionary.update(dict2)

    return new_dictionary
