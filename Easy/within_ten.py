#### ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

    almost_there(90) --> True
    almost_there(104) --> True
    almost_there(150) --> False
    almost_there(209) --> True
    
NOTE: `abs(num)` returns the absolute value of a number
  
def almost_there(n):
    # if 100 +- 10 = n or 200 +- 10
    if 90 <= n <=110 or 190 <= n <= 210:
    # return True
        return True
    else:
        return False
