def subtract(x: int, y: int) -> int:
    """
    >>> subtract(5, 6)
    -1
    >>> subtract(55, 66)
    -11
    >>> subtract(8, 7)
    1
    """
    ### BEGIN SOLUTION
    return x - y
    ### END SOLUTION

def convert_celsius_to_fahrenheit(x: int) -> float:
    """
    >>> convert_celsius_to_fahrenheit(0)
    32.0
    >>> convert_celsius_to_fahrenheit(100)
    212.0
    """
    ### BEGIN SOLUTION
    return x * 9/5 + 32
    ### END SOLUTION

def sort_a_list(x: list) -> list:
    """
    >>> unsorted_list = [3, 2, 5]
    >>> sort_a_list(unsorted_list)
    [2, 3, 5]
    >>> unsorted_list = [13, 7, 11]
    >>> sort_a_list(unsorted_list)
    [7, 11, 13]
    """
    ### BEGIN SOLUTION
    return sorted(x)
    ### END SOLUTION