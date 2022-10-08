#### SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
 
    summer_69([1, 3, 5]) --> 9
    summer_69([4, 5, 6, 7, 8, 9]) --> 9
    summer_69([2, 1, 6, 9, 11]) --> 14
    
def summer_69(arr):
    # initialize value to hold sum
    total = 0
    # start add condition with True to be triggered later
    add = True
    # for every integer in the array
    for num in arr:
        # while we are still allowed to add
        while add:
            # if we dont run into a six at this integer, continue to add
            # and exit loop to go to next int
            if num != 6:
                total += num
                break
            # otherwise, trigger add and go down to next while loop
            else:
                add = False
            # while add is False
        while not add:
            # if we do not find a 9, continue to the next integer with
            # add condition still False
            if num != 9:
                break
            # otherwise, if we find a 9, break out of loop and "reset" add condition
            # and continue summing again
            else:
                add = True
                break
    # after iterating through the list, return our sum
    return total
