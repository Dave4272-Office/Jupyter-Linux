"""
https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/tutorial/
https://www.hackerearth.com/problem/algorithm/the-confused-monk/?source=list_view
"""
def euler_gcd(a: int, b: int) -> int:
    """
    Euler's Method to calculate gcd
    gcd(a,b)
    1) if b = 0 then: gcd = a
    2) else: gcd = gcd(b,a%b)
    """
    if b == 0:
        return a
    return euler_gcd(b, a % b)


def fast_power(a: int, e: int, m: int) -> int:
    """
    Calculates (a^e)%M.

    Using:
    1) if e is even then:
        a) a^e = ((a^2)^(e/2))
        b) (a^e)%M = ((a^2)^(e/2))%M = (((a^2)%M)^(e/2))%M
    2) else:
        a) a^e = a*a^(e-1); e-1 becomes even;
        b) (e-1) / 2 => e // 2;
        c) (a^e)%M = (a*a^(e-1))%M = ((a%M)*((a^(e-1))%M))%M 
            = ((a%M)*((((a^2)%M)^((e-1)/2))%M))%M = ((a%M)*((((a^2)%M)^(e//2))%M))%M
    """
    if e == 0:
        return 1
    elif e == 1:
        return a % m
    elif e % 2 == 0:
        return fast_power(((a * a) % m), e // 2, m)
    else:
        return (a * fast_power(((a * a) % m), e // 2, m)) % m


def euler_gcd_list(list_num: list[int]) -> int:
    """
    calculate gcd of a list of numbers using Euler's method
    """
    if len(list_num) == 1:
        return list_num[0]
    elif len(list_num) == 2:
        return euler_gcd(list_num[0], list_num[1])
    else:
        return euler_gcd(list_num[0], euler_gcd_list(list_num[1:]))


def fast_power_list(list_num: list[int], e: int, m: int) -> list[int]:
    """
    Returns the fast power of a list of numbers to the power of e
    """
    return [fast_power(x, e, m) for x in list_num]


def mod_multiplication(a: int, b: int, m: int) -> int:
    """
    Mod Multiplication
    (a*b)%M = ((a%M)*(b%M))%M
    """
    return ((a % m) * (b % m)) % m


def mod_multiplication_list(list_num: list[int], m: int) -> int:
    """
    Returns the mod multiplication of a list of numbers
    """
    if len(list_num) == 1:
        return list_num[0] % m
    elif len(list_num) == 2:
        return mod_multiplication(list_num[0], list_num[1], m)
    else:
        return mod_multiplication(
            list_num[0], mod_multiplication_list(list_num[1:], m), m
        )


M = 1000000007  # 10^9 + 7
N = int(input())
A = input()
A = [int(x) for x in A.split()]
gx = euler_gcd_list(A)  # gx = gcd(list of num);
# answer = (fx^gx) mod M; fx = multiplication of list of numbers
answer = mod_multiplication_list(fast_power_list(A, gx, M), M)
print(answer)
