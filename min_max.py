def find_max_min(num_list):
    """" 
        Program to return the max and min in a numbers array
    """

    """ Return the number of elements in the list in a new list if the `min` and `max` are equal """
    if min(num_list) == max(num_list):
        return [len(num_list)]

    """ Return min then max """
    return [min(num_list), max(num_list)]