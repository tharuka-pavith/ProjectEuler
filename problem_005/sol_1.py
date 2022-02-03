'''
Project Euler Problem 006: https://projecteuler.net/problem=5

---Smallest Multiple---
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Solution: 232792560

References: 
    - https://en.wikipedia.org/wiki/Least_common_multiple

'''

def generate_prime_factors(num : int) -> list:
    '''
    Generates a list of prime factors of num and returns as a list
    '''
    if num < 2: return []

    primes = [2,3,5,7,11,13,17,19]
    l = []
    for i in primes:
        if num == 1: break
        c = 0
        while num % i == 0:
            num = num // i
            c += 1
        l.append( (i, c) )
    
    return l



def solution() -> int:
    '''
    Returns the smallest positive number that is evenly divisible by all of the numbers from 1 to 20
    '''
    pass

if __name__ == "__main__":
    print(generate_prime_factors(4))
    print(generate_prime_factors(10))
    print(generate_prime_factors(18))


