**Write a function that checks whether a number is in a given range (inclusive of high and low)**

def ran_check(num,low,high):
    for x in range(low, high + 1):
        if x == num:
            if low <= x <= high:
                print(f'{x} is in the range between {low} and {high}')
            else:
                print(f'{x} is NOT in the range between {low} and {high}')
        else:
            continue
            
