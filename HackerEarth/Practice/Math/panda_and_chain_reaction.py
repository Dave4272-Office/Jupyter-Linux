"""
https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/tutorial/
https://www.hackerearth.com/problem/algorithm/panda-and-chain-reaction/?source=list_view
"""
def mod_multiplication(a: int, b: int, m: int) -> int:
    """
    Mod Multiplication
    (a*b)%M = ((a%M)*(b%M))%M
    """
    return ((a % m) * (b % m)) % m


M = 1000003  # 10^6 + 3
T = int(input())
# storing factorials till M-1
factStore = [1] * 1000003
for i in range(2, 1000003):
    factStore[i] = mod_multiplication(factStore[i - 1], i, M)
while T > 0:
    T = T - 1
    A = input()
    A = [int(x) for x in A.split()]
    N, X = A[0], A[1]
    # the problem is this series
    # X, 1*X, 2*1*X, 3*2*1*X, ... , i*i-1*...*2*1*X, ... , N*N-1*...*2*1*X
    # => 0!X, 1!X, 2!X, 3!X, ... , i!X, ... , N!X
    # required term is N => N!*X
    # answer = (N! * X)mod M
    # if N >= M then N has a factor of M; so N!mod M = 0 => answer = 0
    if N >= M:
        answer = 0
    else:
        answer = mod_multiplication(factStore[N], X, M)
    print(answer)
