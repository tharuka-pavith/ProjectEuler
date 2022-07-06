"""
Project Euler Problem 016: https://projecteuler.net/problem=16

---Power digit sum---
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

Solution: 1366 Done!

References [Optional]:
- [Wikipedia link to the topic]
- [Stackoverflow link]
"""

def solution(power: int = 1000) -> int:
    '''
    Returns the sum of digits of 2^power
    
    >>> solution()
    1366
    >>> solution(10)
    7
    '''
    ls = list(int(i) for i in str(pow(2,power)))
    return sum(ls)


if __name__ == "__main__":
    print(f'{solution(10)= }')
    