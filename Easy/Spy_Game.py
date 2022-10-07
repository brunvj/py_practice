#### SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

     spy_game([1,2,4,0,0,7,5]) --> True
     spy_game([1,0,2,4,0,5,7]) --> True
     spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    # final verdict, true or false?
    final_verdict = False
    # if index of 0 0 7 is equal to n, n+1, and n+2, then return true (later changed to reverse index)
    for x in range(len(nums)):
        # if we reached the end of the range of our list, break the loop and return False, or return True
        if x == len(nums) - 1:
            if nums[x] != 7 and nums[x-1] != 0 and nums[x-2] != 0:
                break
            else: 
                final_verdict = True
        #if nums[x] == 0 and nums[x+1] == 0 and nums[x+2] == 7:
        #    final_verdict = True
        # Otherwise, continue
	else:
            continue
    return final_verdict
