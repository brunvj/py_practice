#### COUNT PRIMES: Write a function that returns the *number* of prime numbers that exist up to and including a given number
    count_primes(100) --> 25

By convention, 0 and 1 are not prime.

def count_primes(num):
    # initialize count value
    count = 0
    # for numbers within the range of 0 and the input value (inclusive)
    for number in range (num + 1):
        # if the number is not 0 or 1, continue to evaluate the input
        if number > 1: 
            # for numbers in the range of 2 to the index of the range
            for i in range (2, number):  
                # if the number itself has a divisor, stop the program and exit the loop
                if (number % i) == 0:  
                    break  
            # otherwise, add this number, which is prime, to the count
            else:  
                count += 1
    # Finally, print the total count of numbers leading up to the input number
    print(count)
    
    
# More efficient:

def count_primes(num):
    # Check for 0 or 1 input
    if num < 2:
        return 0
    # Check for 2 or greater
    
    # Store our prime numbers
    primes = [2]
    # Counter going up to the input num
    x = 3
    # x is going through every number up to input num
    while x <= num:
        # Check if x is prime
        for y in primes:
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
