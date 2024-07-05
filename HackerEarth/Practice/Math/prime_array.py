"""
https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/practice-problems/algorithm/prime-array-5e448ef6/
"""

import math


def is_prime(n: int) -> bool:
    """
    Naive Prime Checker with divisor in between 2 and sqrt(n)
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


T = int(input())
while T > 0:
    T -= 1
    N = int(input())
    A = input()
    A = [int(x) for x in A.split()]

    no_of_ones = A.count(1)
    if no_of_ones < 2:
        print(0)
        continue

    no_of_prime = 0
    for i in range(len(A)):
        if is_prime(A[i]):
            no_of_prime += 1

    print((no_of_prime * no_of_ones * (no_of_ones - 1)) // 2)
