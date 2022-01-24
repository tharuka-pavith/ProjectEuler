"""
Project Euler Problem 03: https://projecteuler.net/problem=4

---Largest Palindrome Product---

A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers

Solution: 906609

... [Solution explanation - Optional] ...

References:
- [Wikipedia link to the topic]
- [Stackoverflow link]
...

"""

def is_palindrome(num: int) -> bool:
    '''Check whether the num is a palindrome number.'''
    if num<11: return False
    org_num = int(num)
    rev_num = 0
    digits_count = 0
    l = []
    while num > 0:
        digits_count += 1
        digit = num % 10
        l.append(digit)
        num = num // 10
    for i in l:
        rev_num += i * ( 10**(digits_count-1) )
        digits_count -= 1
    
    if org_num == rev_num: return True
    else: return False

def solution(no_of_digits: int = 3) -> int:
    '''Returns the largest palindrome made from the product of two 3-digit numbers '''
    palindrome_list = []
    for i in range(999, 0, -1):
        for j in range(999, 0, -1):
            x = i*j
            if is_palindrome(x):
                palindrome_list.append(x)

    return(max(palindrome_list))

if __name__ == '__main__':
    print(f'{solution() = }')
    