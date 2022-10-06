#### BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
    blackjack(5,6,7) --> 18
    blackjack(9,9,9) --> 'BUST'
    blackjack(9,9,11) --> 19
    
def blackjack(a,b,c):
    # sum of numbers
    sum = a + b + c
    # list to test if 11 is in
    x = list([a,b,c])
    # if sum <= 21, return sum
    if sum <= 21:
        return sum
    # else if sum > 21 and 11 exists in tuple, reduce sum by 10
    elif sum > 21 and 11 in x:
        sum = sum - 10
        return sum
    # else return 'Bust'
    else:
        return 'Bust'
