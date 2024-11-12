# 카드1

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

q = deque([i for i in range(1, n+1)])

answer = deque([])

while len(q) > 1 :
    tmp = q.popleft()
    # answer.append(tmp)
    answer.append(str(tmp))
    q.append(q.popleft())

if n == 1 :
    print(1)
elif q :
    # print(*answer, q.pop())
    print(' '.join(answer), q.pop())
else :
    # print(*answer, tmp)
    print(' '.join(answer), tmp)