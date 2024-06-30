"""
https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/tutorial/

Modular arithmetic:
    Properties:
        1) (a + b) % M = (a % M + b % M) % M
        2) (a * b) % M = ((a % M) * (b % M)) % M
        3) (a - b) % M = ((a % M) - (b % M) + M) % M
        4) (a / b) % M = ((a % M) * (b⁻¹ % M)) % M
            b⁻¹ => Modulo Multiplicative Inverse of b.

Modulo Multiplicative Inverse:
    (b * b⁻¹) % M = 1 % M
        b⁻¹ => Modulo Multiplicative Inverse of b.
"""


def extended_gcd(a: int, b: int) -> dict:
    """
    Calculates gcd using Euler's method and also the Bezout coefficients.
    ax + by = gcd(a, b)
    x,y => Bezout coefficients.

    gcd(a,b)
    1) if b = 0 then: gcd = a, x = 1, y = 0
    2) else: gcd = gcd(b,a%b), x = old_y, y = old_x - quotient(a,b) * old_y

    for a = q*b + r; a,q,b,r => integer
    quotient(a,b) = q = (a - r) / b = lower_bound(a/b) = a//b
    """
    if b == 0:
        return {"gcd": a, "x": 1, "y": 0}
    ext_gcd = extended_gcd(b, a % b)
    x = ext_gcd["y"]
    y = ext_gcd["x"] - ((a // b) * ext_gcd["y"])
    return {"gcd": ext_gcd["gcd"], "x": x, "y": y}


def euler_mod_multiplicative_inverse(a: int, m: int) -> int:
    """
    Calculates Modular Multiplicative Inverse using Euler's method to calculate extended gcd
    MMI = ((Bezout coefficient x of extended gcd(a,M))%M + M)%M
    M => Modulo Factor
    """
    ext_gcd = extended_gcd(a, m)
    return ((ext_gcd["x"] % m) + m) % m


def fast_power_mod(a: int, e: int, m: int) -> int:
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
        return fast_power_mod(((a * a) % m), e // 2, m)
    else:
        return ((a % m) * fast_power_mod(((a * a) % m), e // 2, m)) % m


inp = input()
inp = inp.split()
A, B, C, M = int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3])
answer = (
    fast_power_mod(A, B, M) * euler_mod_multiplicative_inverse(C, M)
) % M  # answer = ((A^B)/C)mod M
print(answer)
