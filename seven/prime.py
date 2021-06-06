import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,   int(math.sqrt(n)) +1):
        ## % means divide the number and get the reminder 
        if n % i == 0:
            return False
    return True

        
        