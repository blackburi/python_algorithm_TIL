# 요세푸스 문제

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

q = deque([(i+1) for i in range(n)])

ans = '<'
tmp = 0

while q :
    cnt = q.popleft()
    tmp += 1

    if tmp == k :
        if len(q) == 0 :
            ans += str(cnt)
            break
        ans += str(cnt) + ',' + ' '
        tmp = 0
    else :
        q.append(cnt)
ans += '>'
print(ans)