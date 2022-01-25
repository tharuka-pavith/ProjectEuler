"""
Project Euler Problem 006: https://projecteuler.net/problem=6

---Sum square difference---
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers 
and the square of the sum is $3025 - 385 = 2640$.
Find the difference between the sum of the squares of the first one hundred natural numbers 
and the square of the sum.

Solution: 25164150

... [Solution explanation - Optional] ...

References:
- [Wikipedia link to the topic]
- [Stackoverflow link]
...
"""

def solution(n: int = 100):
    """
    Returns the difference between the sum of the squares of the first 'n' natural numbers 
    and the square of the sum.
    """
    sum = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            sum += i*j

    return 2*sum



if __name__ == "__main__":
    print(f"{solution() = }")