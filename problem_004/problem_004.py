'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers
'''

def isPalindrome(num):
    if num<11: return False
    str_num = str(num)
    rev_str_num = str_num[-1: -1*len(str_num)-1: -1]
    if(str_num == rev_str_num):
        return True
    else:
        return False

largest = 11
for i in range(999, 99, -1):

    for j in range(999, 99, -1):
        x = j*i
        if isPalindrome(x) and x>largest:
            largest = x

print(largest)