from math import inf


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return -1, -1
    if len(ints) == 1:
        minimum = maximum = ints[0]
        return minimum, maximum
    minimum  = inf
    maximum = 0
    for i in ints:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i
    return minimum, maximum

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# list of duplicate elements only
llist = [10 for i in range(0, 3)]
print ("Pass" if ((10, 10) == get_min_max(llist)) else "Fail")

# One item list
list2 = [2]
print ("Pass" if ((2, 2) == get_min_max(list2)) else "Fail")

# empty list
empty = []
print ("Pass" if ((-1, -1) == get_min_max(empty)) else "Fail")




