# 고양이는 많을수록 좋다

import sys
input = sys.stdin.readline

# 마도카가 취할수 있는 경우
# k마리 고양이 -> (k+1)~(2*k)

n = int(input())

if n == 0 :
    print(0)
else :
    # 횟수
    cnt = 1

    while n > 1 :
        if n % 2 :
            n = n//2 + 1
        else :
            n //= 2
        cnt += 1

    print(cnt)