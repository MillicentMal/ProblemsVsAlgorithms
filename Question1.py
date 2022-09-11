def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return -1 
    if number == 1:
        return 1
    start = 0
    end = number // 2
    while start <= end:
        middle = (start + end ) // 2
        if middle * middle == number:
            return middle
        if middle * middle < number:
            start = middle + 1
            result = middle
        elif middle * middle > number:
            end = middle - 1 

    return result
    
    

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# edge cases 
# case 1: Negative number
print ("Pass" if  (-1 == sqrt(-5)) else "Fail")
#  case 2: 1
print ("Pass" if  (1 == sqrt(1)) else "Fail")


