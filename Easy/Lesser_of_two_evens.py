#### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd
    lesser_of_two_evens(2,4) --> 2
    lesser_of_two_evens(2,5) --> 5
    
def lesser_of_two_evens(a,b):
    # bigger number to return
    bn = 0
    # smaller number
    sn = 0
    # comparison
    if a > b:
        bn = a
        sn = b
    else:
        bn = b
        sn = a
    # if a is even, test b
    if a % 2 == 0:
        # if b and a is even, return smaller number
        if b % 2 == 0:
            return sn
        # if b is not even, return greater number
        else:
            return bn
    # otherwise if a is not even, return greater number
    else:
        return bn
