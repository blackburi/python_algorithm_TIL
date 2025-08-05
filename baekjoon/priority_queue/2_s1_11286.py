# 절댓값 힙

import sys, heapq
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n) :
    k = int(input())
    if k != 0 :
        heapq.heappush(q, (abs(k), k))
    elif q == [] : # k == 0
        print(0)
    else : # q != [] and k == 0
        out = heapq.heappop(q)
        print(out[1])