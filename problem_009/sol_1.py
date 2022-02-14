'''
Project Euler Problem 006: https://projecteuler.net/problem=9

---Special Pythogorean Triplet---
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Solution: 31875000 Done!

References: 
    - 
'''
from math import sqrt

def solution() -> int:
    '''
    Returns Pythagorean triplet for which a + b + c = 1000 where a^2 + b^2 = c^2
    '''

    '''
    From c^2 = a^2 + b^2, a+b+c = 1000;

    ab = 500(1000 - 2c)  ==>  c < 500

    Let c = P and ab = R then,
    b = R/a

    => a^2 + b^2 = P^2
    => a^2 + R^2/a^2 = P^2
    => a^4 - P^2 * a^2 + R^2 = 0 (quadratic equation)

    From x = -b +- sqrt(b^2 - 4ac)

    First let k = aqrt(P^4 - 4R^2)
    Then a^2 = (P^2 +- k) / 2

    From above equation find, a, b
    '''
    for c in range(1, 500):
        P = c
        R =500 * (1000 - 2 * c) # R = ab

        k = sqrt(P**4 - 4*(R**2)) if P**4 - 4*(R**2) > 0 else 'invalid' # sqrt( b^2 - 4ac)
        if k == 'invalid': continue

        a_squared_1 = (P**2 - k)/2
        a_squared_2 = (P**2 + k)/2

        a = sqrt(a_squared_1)
        b = sqrt(a_squared_2)
        
        if a.is_integer():
            return int(a*b*c)
    
    return None

if __name__ == "__main__":
    print(f'{solution() = }')


