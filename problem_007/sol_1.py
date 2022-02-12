'''
Project Euler Problem 006: https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

Solution: 104743
'''

from math import sqrt, ceil

def is_prime(num: int) -> bool:
    '''
    Checks whether a num is prime or not.
    Returns True if the number is prime.
    '''
    if num < 2 or num == 4: return False
    elif num == 2 or num == 3: return True
    elif num%2==0 or num%3 == 0: return False
    
    n = ceil(sqrt(num))

    for i in range(3, n+1, 2):
        if num % i == 0: return False
    
    return True

def solution(n: int= 10_001) -> int:
    '''
    Returns the n th prime number
    '''
    prime_count = 0
    i = 2

    while True:
        if is_prime(i): 
            prime_count += 1
            if prime_count == n: 
                return i
        i += 1

if __name__ == "__main__":
    print(f"{solution() = }") 


