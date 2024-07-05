"""
https://www.hackerearth.com/practice/math/number-theory/totient-function/tutorial/
"""

import math


class FactorSieve(object):
    """
    Sieve data type for prime data
    buffer: list of boolean
    max: stores the value till which sieve already calculated
    """

    buffer: list[int]
    max: int

    def __init__(self, m: int) -> None:
        self.buffer = [0] * m
        self.buffer[0] = -1
        self.buffer[1] = -1
        self.max = 1


def sieve_of_eratosthenes(n: int, m: int, sieve: FactorSieve) -> None:
    """
    Sieve of Eratosthenes both prime and factor
    """
    for i in range(2, int(math.sqrt(n) + 1)):
        if sieve.buffer[i] == 0 or sieve.buffer[i] == i:
            for j in range(max(i * i, sieve.max - (sieve.max % i)), n + 1, i):
                if sieve.buffer[j] == 0:
                    sieve.buffer[j] = i
    for i in range(2, n + 1):
        if sieve.buffer[i] == 0:
            sieve.buffer[i] = i
    sieve.max = n


def factorize(
    n: int,
    m: int,
    sieve: FactorSieve,
) -> list[int]:
    """
    Calculates the sieve using the given method and returns the prime factors of given number
    """
    if n > sieve.max and n < m:
        sieve_of_eratosthenes(n, m, sieve)
    factors: list[int] = []
    x = abs(n)
    while x != 1:
        factors.append(sieve.buffer[x])
        x //= sieve.buffer[x]
    if n < 0:
        factors = [-1] + factors
    return factors


def totient(
    n: int,
    m: int,
    sieve: FactorSieve,
) -> int:
    """
    Euler's Totient / ϕ Function

    ϕ(n) = n * Π(1-1/p),
    p is from set of all prime factors of n
    """
    unique_factors = set(factorize(n, m, sieve))
    ans = n
    for i in unique_factors:
        ans *= 1 - (1 / i)
    return int(ans)


M = 1000003  # 10^6 + 3
sieve = FactorSieve(M)
N = int(input())
print(totient(N, M, sieve))
