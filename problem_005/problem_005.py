'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import math

def isPrime(num): #2,3,5,7
    if (num<=1 or num==4): return False
    if (num==2): return True

    for i in range(2, num ):
        if num%i == 0: return False
    return True

nums = [i for i in range(2,21)]
prime_numbers = [i for i in nums if isPrime(i)]
#print(prime_numbers)


