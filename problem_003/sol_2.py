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
def solution(n: int = 600851475143):
    """
    Returns the largest prime factor of n

    ...
    [Doctest as mentioned above]
    ...

    """
    if n < 2:
        raise ValueError('Invalid number!')

    prime = 1
    i = 2
    while i * i <= n:
        while n % i == 0:
            prime = i
            n //= i
        i += 1
    if n > 1:
        prime = n
    return int(prime)

if __name__ == "__main__":
    print(f"{solution() = }")
