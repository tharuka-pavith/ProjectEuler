'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import math
def isPrime(num): #2,3,5,7
    if (num<=1 or num==4): return False
    if (num==2): return True

    num = math.ceil(math.sqrt(num))
    for i in range(2, num ):
        if num%i == 0: return False
    
    return True

num = 600_851_475_143
largest_prime = 2
prime_num = 2
sq_num = math.ceil(math.sqrt(num))
for i in range(2, sq_num ):
    if isPrime(i): prime_num = i

    if num % prime_num == 0 : largest_prime = prime_num

print(largest_prime)

'''
for i in range(1, 100):
    if isPrime(i):
        print(i)
'''
