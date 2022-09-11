
from typing import List


def mergesort(items):
    """
    Source: Udacity Sorting Algorithms lesson

    """
    
    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

def rearrange_digits(input_list):       
    if len(input_list) == 0:
        return 0, 0
    if len(input_list) == 1:
        return input_list[0], 0
    new = mergesort(input_list)
    digit1 = ""
    digit2 = ""
    while len(new) > 0:
        digit1 += str(new.pop())
        if len(new) == 0:
            return int(digit1), int(digit2)
        digit2 += str(new.pop())
    return int(digit1), int(digit2)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Test cases 
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

# edge case 1: Null list
test_function([[], [0, 0]])

# edge case 2: One input
test_function([[5], [5, 0]])

# test case 3: 
test_function([[1,3,4,5,6,7,8,9,0,11,34,5,6,7,7], [349776530, 11876541]])
