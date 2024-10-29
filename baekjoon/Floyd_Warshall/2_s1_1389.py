# 케빈 베이컨의 6단계 법칙

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().rstrip().split())

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# 케빈 베이컨의 수
numbers = []

def bfs(v) :
    q = deque([v])
    dist[v] = 0

    while q :
        target = q.popleft()

        # 친구 관계를 확인하고 탐색하지 않은 친구라면 탐색
        for i in graph[target] :
            if dist[i] == -1 :
                # 케빈 베이컨
                dist[i] = dist[target] + 1
                q.append(i)

for i in range(1, n+1) :
    dist = [-1] * (n+1)
    bfs(i)
    numbers.append(sum(dist))

print(numbers.index(min(numbers))+1)
