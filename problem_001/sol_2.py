"""
Project Euler Problem 001: https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Solution: 234168

References :
- [Wikipedia link to the topic]
- [Stackoverflow link]

"""


def solution(limit: int = 1000) -> int:
    """
    Returns the sum of multiples of 3 or 5 below the given limit.

    You can have a detailed explanation about the solution in the
    module-level docstring.

    >>> solution(1)
    0
    >>> solution(10)
    23
    >>> solution(-1)
    0

    """
    return sum( i for i in range(0, limit) if i%3==0 or i%5==0)


if __name__ == "__main__":
    print(f"{solution() = }")

