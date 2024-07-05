"""
https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-2/tutorial/
"""

import math
from collections.abc import Callable


class PrimeSieve(object):
    """
    Sieve data type for prime data
    buffer: list of boolean
    max: stores the value till which sieve already calculated
    """

    buffer: list[bool]
    max: int

    def __init__(self, m: int) -> None:
        self.buffer = [True] * m
        self.buffer[0] = False
        self.buffer[1] = False
        self.max = 1


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


def sieve_of_eratosthenes_prime(n: int, sieve: PrimeSieve) -> None:
    """
    Sieve of Eratosthenes only prime
    """
    for i in range(2, int(math.sqrt(n) + 1)):
        if sieve.buffer[i]:
            for j in range(max(i * i, sieve.max - (sieve.max % i)), n + 1, i):
                sieve.buffer[j] = False
    sieve.max = n


def sieve_of_eratosthenes_factor(n: int, sieve: FactorSieve) -> None:
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


def sieve_of_eratosthenes(n: int, m: int, sieve: PrimeSieve | FactorSieve) -> None:
    """
    Sieve of Eratosthenes
    """
    if n <= sieve.max:
        return
    if n >= m:
        return
    if isinstance(sieve, PrimeSieve):
        sieve_of_eratosthenes_prime(n, sieve)
    else:
        sieve_of_eratosthenes_factor(n, sieve)


def is_prime(
    n: int,
    m: int,
    sieve_fn: Callable[[int, int, PrimeSieve | FactorSieve], None],
    sieve: PrimeSieve | FactorSieve,
) -> bool:
    """
    Calculates the sieve using the given method and returns if the given number is prime
    """
    sieve_fn(n, m, sieve)

    if isinstance(sieve, FactorSieve):
        return sieve.buffer[abs(n)] == abs(n)
    else:
        return sieve.buffer[abs(n)]


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


def factorize(
    n: int,
    m: int,
    sieve_fn: Callable[[int, int, FactorSieve], None],
    sieve: FactorSieve,
) -> list[int]:
    """
    Calculates the sieve using the given method and returns the prime factors of given number
    """
    sieve_fn(n, m, sieve)
    factors: list[int] = []
    x = abs(n)
    while x != 1:
        factors.append(sieve.buffer[x])
        x //= sieve.buffer[x]
    if n < 0:
        factors = [-1] + factors
    return factors


def factorize_naive(n: int) -> list[int]:
    """
    Calculates Factors of a number naive approach
    """
    factors: list[int] = []
    x = abs(n)
    while x != 1:
        if is_prime_naive(x):
            factors.append(x)
            break
        for i in range(2, int(math.sqrt(x) + 1)):
            if x % i == 0:
                factors.append(i)
                x //= i
                break
    if n < 0:
        factors = [-1] + factors
    return factors


# M = 1000000007  # 10^9 + 7
# sieve = FactorSieve(M)

# while True:
#     N = input("Enter Value: ")
#     if N == "q" or N == "Q":
#         break
#     N = int(N)

#     print("For input: ", N)
#     print("Is Prime: ", is_prime(N, M, sieve_of_eratosthenes, sieve))
#     print("Factors: ", factorize(N, M, sieve_of_eratosthenes, sieve))
#     print("Is Prime Naive: ", is_prime_naive(N))
#     print("Factors Naive: ", factorize_naive(N))
#     print()
#     print()

M = 1000000
sieve = PrimeSieve(M)
N = int(input())
sieve_of_eratosthenes(N, M,sieve)
print(sieve.buffer[1:N+1].count(True))
