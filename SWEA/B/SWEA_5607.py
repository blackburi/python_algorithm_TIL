# 조합


c = 1234567891

# 팩토리얼 계산
def fac(x) :
    re = 1
    for i in range(2, x+1) :
        re = (re*i) % c
    return re

# 거듭제곱 계산
def square(n, k) :
    if r == 0 :
        return 1
    elif k == 1 :
        return n

    tmp = square(n, k//2)
    if k % 2 :
        return tmp * tmp * n % c
    else :
        return tmp * tmp % c

T = int(input())
for tc in range(1, T+1) :
    n, r = map(int, input().split())

    tn = fac(n)
    bn = fac(n-r) * fac(r) % c

    ans = tn * square(bn, c-2) % c

    print(f'#{tc} {ans}')