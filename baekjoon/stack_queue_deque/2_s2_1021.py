# 회전하는 큐

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
q = deque(list(map(int, input().rstrip().split())))

answer = 0
lst = [(i+1) for i in range(n)]

while q :
    number = q.popleft()

    # 이동의 횟수를 체크
    tmp = 0

    for i in range(n) :
        if lst[i] == number :
            # lst, answer 변경
            lst = lst[i+1:] + lst[:i]

            if i > n//2 :
                answer += (n-i)
            else :
                answer += i

            n -= 1
            break

print(answer)