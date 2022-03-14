"""
Project Euler Problem 013: https://projecteuler.net/problem=13

---Longest Collatz sequence---
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Solution: 837799 [got the solution but algorithm is slow]

References [Optional]:
- [Wikipedia link to the topic]
- [Stackoverflow link]
"""
def generate_collatz(n: int = 13)-> None:
    '''Generates collatz sequence
    
    n   starting number'''
    while n != 1:
        if n % 2 == 0: #even
            n = n // 2
            yield n
        else: #odd
            n = 3*n +1
            yield n
    return None

def solution() -> int:
    max_count = 0
    strt_num = 0
    for num in range(1_000_000, 1, -1):
        count = 0
        for i in generate_collatz(num):
            count += 1
        if count > max_count:
            max_count = count
            strt_num = num

    return strt_num


if __name__ == "__main__":
    print(f'{solution()= }')
    