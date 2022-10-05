#### MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 *or* if one of the integers is 20. If not, return False

    makes_twenty(20,10) --> True
    makes_twenty(12,8) --> True
    makes_twenty(2,3) --> False

def makes_twenty(n1,n2):
    # sum the integers
    nsum = n1 + n2
    # if integer sum is greater than or equal to 20, return true
    if nsum >= 20:
        return True
    # else return false
    else:
        return False
