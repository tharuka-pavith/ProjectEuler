'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
import timeit


# Method 1

ls = [i for i in range(3, 1000) if (i % 3 == 0 or i %5 == 0)]  # list comprehension
sum = 0
for i in ls:
    sum += i
print(sum)



# Method-2


sum = 0
for i in range(3, 1000):
    if (i % 3 == 0 or i % 5 == 0):
        sum += i
print(sum)