"""
Project Euler Problem 013: https://projecteuler.net/problem=13

---Large Sum---
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers
    [data is in the data.txt]

Solution: 5537376230

References [Optional]:
- [Wikipedia link to the topic]
- [Stackoverflow link]
"""

def solution(n: int = 10) -> int:
    """
    Returns the first n digits of the sum of the numbers

    n  the number of digits required

    >>> solution()
    5537376230
    >>> solution(5)
    55373
    >>> solution(100)
    length of the total is less than 100 digits
    None
    >>> solution(-2)
    0
    """
    fp = open('problem_013/data.txt')
    l_lines = (int(l) for l in fp.readlines()) #generator of lines

    total = 0  
    for l in l_lines:
        total += l    #take sum of the numbers
    
    l_digits = [] #list of digits
    while total > 0:
        #mod = total % 10
        #total = total // 10
        total, mod = divmod(total, 10)
        l_digits.append(mod)

    l_digits = l_digits[::-1] #reverse
    itr_digits = iter(l_digits) #iterator for l_digits
    g_multipl = (10**i for i in range(n-1, -1, -1))   #[generator] (10^9, 10^8, ..., 1)
    
    result = 0
    for mul in g_multipl:
        try:
            result += next(itr_digits) * mul
        except StopIteration:
            print(f"length of the total is less than {n} digits")
            return None
    
    return result


if __name__ == "__main__":
    print(f"{solution() = }")
    print(f"{solution(5) = }")
    print(f"{solution(20) = }")
    print(f"{solution(100) = }")
    print(f"{solution(-2) = }")
    