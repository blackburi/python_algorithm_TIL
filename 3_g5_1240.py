# 노드사이의 거리

import sys
input = sys.stdin.readline
from collections import deque

# 최단 거리
def bfs(start, end) :
    q = deque([(start, 0)])

    visited = [False]*(n+1)
    visited[start] = True

    while q :
        v, d = q.popleft()
        # 도착 노드와 동일한 경우
        if v == end :
            return d

        for node, distance in graph[v] :
            # 방문한 적이 없는 노드의 경우
            if not visited[node] :
                visited[node] = True
                # 노드와의 거리를 기록하며 저장
                q.append((node, d+distance))


n, m = map(int, input().split())

# 거리를 나타내는 graph
graph = [[] for _ in range(n+1)]

for _ in range(n-1) :
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

for _ in range(m) :
    n1, n2 = map(int, input().split())
    print(bfs(n1, n2))