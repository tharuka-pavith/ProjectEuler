"""
Project Euler Problem 03: https://projecteuler.net/problem=3

---Largest Prime Factor---

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Solution: 6857

... [Solution explanation - Optional] ...

References:
- [Wikipedia link to the topic]
- [Stackoverflow link]
...

"""
from math import sqrt, ceil

def is_prime(num: int) -> bool: ## WRONG
    '''
    Checks whether a num is prime or not.
    Returns True if the number is prime.
    '''
    if num < 2 or num == 4: return False
    elif num == 2 or num == 3: return True

    n = ceil(sqrt(num))

    for i in range(3, n+1, 2):
        if num % i == 0: return False
    
    return True

def is_factor(num: int, div: int) -> bool:
    '''
    Checks whether div is a factor of num.
    Returns True if div is a factor of num.
    '''
    return num % div == 0

def solution(number: int = 600851475143):
    """
    Returns the largest prime factor of the number

    ...
    [Doctest as mentioned above]
    ...

    """
    for i in range(int(sqrt(number)), 1, -1):
        if number % i == 0:
            if is_prime(i): return i


if __name__ == "__main__":
    print(f"{solution(600851475143) = }")
