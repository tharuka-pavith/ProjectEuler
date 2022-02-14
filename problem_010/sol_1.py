"""
Project Euler Problem 10: https://projecteuler.net/problem=10

... Summation of Primes ...
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Solution: 142913828922

References [Optional]:
- [Wikipedia link to the topic]
- [Stackoverflow link]
...

"""

from math import sqrt, ceil

def is_prime(num: int) -> bool:
    '''
    Returns true if num is a prime number and vice versa

    >>> is_prime(23)
    True
    >>> is_prime(-2)
    False
    >>> is_prime(100)
    False

    '''
    if num == 2 or num == 3: return True
    if num%2 == 0 or num%3 == 0 or num < 2: return False

    sqrt_num = ceil(sqrt(num))
    for i in range(5, sqrt_num+1, 2):
        if num % i == 0: return False
    
    return True

def solution(ulimit: int = 2_000_000) -> int:
    '''
    Returns the sum of all the primes below upper limit (ulimit) provided

    >>> solution()
    142913828922
    >>> solution(10)
    17
    '''
    sum = 0

    for i in range(2, ulimit):
        if is_prime(i):
            sum += i
    
    return sum



if __name__ == "__main__":
    print(f'{solution() = }')