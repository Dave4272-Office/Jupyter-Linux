"""
https://www.hackerearth.com/practice/math/number-theory/primality-tests/tutorial/
"""

import math


def is_prime_naive(n: int) -> bool:
    """
    Naive Prime Checker using upper limit of sqrt(n)
    """
    if abs(n) < 2:
        return False
    for i in range(2, int(math.sqrt(abs(n)) + 1)):
        if n % i == 0:
            return False
    return True


T = int(input())
while T:
    T -= 1
    N = int(input())
    if is_prime_naive(N):
        print("prime")
    else:
        print("composite")
