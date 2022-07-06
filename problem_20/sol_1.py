"""
Project Euler Problem 20: https://projecteuler.net/problem=20

... Factorial digit sum ...
n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!


References [Optional]:
- [Wikipedia link to the topic]
- [Stackoverflow link]
...

"""

def factorial(num: int = 10) -> int:
    '''
    Calculates the factorial of num
    
    Parameters:
        num
    
    Returns: 
        The factorial of num
        
    >>> factorial(4)
    24
    '''
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

def solution(num: int = 100) -> int:
    '''
    Calculates solution for the problem

    Returns:
        The sum of the digits in the factorial of num
    '''
    fact = factorial(num)

    digit_sum = 0

    while(fact != 0):
        digit_sum += fact % 10
        fact = fact//10
    
    return digit_sum


if __name__ == "__main__":
    print(f"{solution(10) = }")