def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    digit1 = ""
    digit2 = ""
    while len(input_list) > 0:
        digit1 += str(max(input_list))
        input_list.remove(max(input_list))
        if len(input_list) == 0:
            return int(digit1), int(digit2)
        digit2 += str(max(input_list))
        input_list.remove(max(input_list))
    return int(digit1), int(digit2)

print(rearrange_digits([4, 6, 2, 5, 9, 8]))
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]

