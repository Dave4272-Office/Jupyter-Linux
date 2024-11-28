"""
https://www.hackerearth.com/problem/algorithm/a-simple-task/?source=list_view
"""

from functools import reduce
from math import sqrt


def successive_difference(list_nums: list[int]) -> list[int]:
    """
    Return the list of all difference between successive elements in a circular fashion.
    1) all successive numbers difference arr[i] - arr[i-1].
    2) difference between first(arr[0]) & last(arr[-1]) element.
    """
    sd = [abs(list_nums[i] - list_nums[i - 1]) for i in range(0, len(list_nums))]
    return sd


def factors(n: int) -> set[int]:
    """
    Finds all factors of N.

    the logic is as follows:
    1) if N is even then:
        a) factors are in the list of even numbers.
        b) any odd numbers is found as the other factor of N.
    2) else: factors may be both even or odd

    3) the logic of list comprehension is:
        a) add 2 numbers each time if its completely divisible:
            i) i*a = N && N%i = 0.
            ii) a = N//i.
            iii) both i & N//i are factors of N.
    """
    step = 2 if n % 2 else 1
    return set(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if not n % i),
        )
    )


def all_factors(list_nums: list[int]) -> set[int]:
    """
    Find all factors of a list of numbers.
    """
    factor_set = set()
    for i in list_nums:
        factor_set = factor_set.union(factors(i))
    return factor_set


M = 1000000007  # 10^9 + 7
N = int(input())
A = [int(input()) for _ in range(N)]
succDiff = successive_difference(A)
print(succDiff)

factorList = all_factors(succDiff)

req = []
for factor in factorList:
    if factor == 1:
        continue
    sumStore = []
    for d in succDiff:
        sumStore.append(d % factor)
    if max(sumStore) == 0:
        req.append(factor)
req.sort()
answer = " ".join([str(i) for i in req])
print(answer)
