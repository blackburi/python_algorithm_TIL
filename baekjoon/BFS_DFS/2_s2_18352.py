# 특정 거리의 도시 찾기

import sys
input = sys.stdin.readline
from collections import deque

# 도시의 수, 도로의 수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())

answer = []
visited = [False] * (n+1)
visited[x] = True

graph = [[] for _ in range(n+1)]
for _ in range(m) :
    s, e = map(int, input().split())
    graph[s].append(e)

q = deque([(x, 0)])
while q :
    v, dist = q.popleft()

    for c in graph[v] :
        if visited[c] is False :
            visited[c] = True

            # 거리가 k와 동일 하다면
            if dist+1 == k :
                answer.append(c)
            # 거리가 k보다 작다면
            else :
                q.append((c, dist+1))

answer.sort()
if len(answer) :
    for ans in answer :
        print(ans)
else :
    print(-1)