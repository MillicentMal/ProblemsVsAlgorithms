def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1
    end = len(input_list)
    start = 0
    while start < end:
        middle = (start + end) // 2
        if input_list[middle] ==  number:
            return middle
        if input_list[start] < input_list[middle]:
            if number >= input_list[start] and number < input_list[middle]:
                end = middle
            else:
                start = middle + 1
        else:
            if number <= input_list[end - 1] and number < input_list[middle]:
                start = middle + 1
            else:
                end = middle
    return -1
        
        

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# edge case: sorted array with no value found
# expected output -1
test_function([[5, 1, 2, 3, 4], 10])

# empty list
test_function([[], -1])