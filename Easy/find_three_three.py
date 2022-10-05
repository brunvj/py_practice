#### FIND 33: 

Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

    has_33([1, 3, 3]) → True
    has_33([1, 3, 1, 3]) → False
    has_33([3, 1, 3]) → False
    
    
def has_33(nums):
    # initialize range value
    x = len(nums)
    # for n in the range of the length of the list
    for n in range(x):
        print(n)
        # if nums[n] == 3
        if nums[n] == 3:
            # if nums[n] == nums[n+1] or nums[n] == nums[n-1], return True
            if nums[n] == nums[n+1] or nums[n] == nums[n+1]:
                return True
            # else, return false
            else:
                return False
        # else, continue
        else:       
            continue
