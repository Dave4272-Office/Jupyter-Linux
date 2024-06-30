"""
https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/tutorial/
https://www.hackerearth.com/problem/algorithm/calculate-the-power/?source=list_view
"""
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


M = 1000000007  # 10^9 + 7
inp = input()
inp = [int(x) for x in inp.split()]
A = inp[0]
B = inp[1]
answer = fast_power(A, B, M)
print(answer)
