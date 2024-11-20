# N번째 큰수

import sys
input = sys.stdin.readline
import heapq

n = int(input())
q = list(map(int, input().rstrip().split()))
for _ in range(n-1) :
    lst = list(map(int, input().rstrip().split()))
    for num in lst :
        heapq.heappush(q, num)
        heapq.heappop(q)

print(q[0])