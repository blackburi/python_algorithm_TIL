# 징검다리

import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc) :
    n = int(input())

    answer = 0

    bot = 0
    top = 10**16

    while bot <= top :
        mid = (bot + top) // 2

        if (mid * (mid+1))//2 < n :
            answer = mid
            bot = mid + 1
        elif (mid * (mid+1))//2 == n :
            answer = mid
            break
        else : # (mid * (mid+1))//2 > n
            top = mid - 1

    print(answer)