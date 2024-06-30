"""
https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/tutorial/
https://www.hackerearth.com/problem/algorithm/riyas-birthday-party-1/?source=list_view
"""

# a(1) = 1; a(2) = 6;
# sequence not in AP or GP
# 1 6 15 28 45 ...
#
# S = a1+a2+a3
# S = a1+a2+a3
# D1 => S-S = a1+[(a2-a1)+(a3-a2)]-a3
#
# D1 => 5 9 13 17 ... => d = 4
#
# since 1st Difference is in AP with d=4 and 1st Term a=5
# Sn = n/2[2a + (n − 1) × d]
# => Sn = n/2[2(5) + (n − 1) × 4]
# => Sn = n/2[10+4n-4] = n/2[6+4n] = n[(6+4n)/2]
# => Sn = n[3+2n]
#
# t(n) = a(1) + Sn = 1+n[3+2n]
# t(n) = 1+3n+2n^2
#
# Since, t(n) = a(n+1)
# => a(n) = t(n-1); because no of D1(n) is 1 less than a(n)
# a(n) = 1+3(n-1)+2(n-1)^2 = 1+3n-3+2(n^2-2(n)(1)+1^2)
# a(n) = 3n+1-3+2(n^2+1-2n) = 3n-2+2n^2+2-4n = 3n-2+2+2n^2-4n
# a(n) = 3n+2n^2-4n = 2n^2+3n-4n
# a(n) = 2n^2-n


def mod_multiplication(a: int, b: int, m: int) -> int:
    """
    Mod Multiplication
    (a*b)%M = ((a%M)*(b%M))%M
    """
    return ((a % m) * (b % m)) % m


def mod_substraction(a: int, b: int, m: int) -> int:
    """
    Mod Substraction
    (a-b)%M = ((a%M)-(b%M)+M)%M
    """
    return ((a % m) - (b % m) + m) % m


M = 1000000007  # 10^9 + 7
T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    answer = mod_substraction(
        mod_multiplication(2, mod_multiplication(n, n, M), M), n, M
    )
    print(answer)
