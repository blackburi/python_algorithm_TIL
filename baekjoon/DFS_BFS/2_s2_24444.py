# 알고리즘 수업 - 너비 우선 탐색1

import sys
input = sys.stdin.readline
from collections import deque


n, m, r = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
# 정점 번호가 작은 순서대로 방문하기 위해서 정렬
for i in range(1, n+1) :
    graph[i].sort()

# 방문 처리
visited = [0] * (n+1)
visited[r] = 1

# 방문 number -> 시작점은 이미 방문 했기 때문에 2부터 시작
idx = 2

q = deque([r])
while q :
    v = q.popleft()
    for i in graph[v] :
        # 방문한 적이 없는 경우만 생각하면 된다.
        if visited[i] == 0 :
            visited[i] = idx
            idx += 1
            q.append(i)

for i in range(1, n+1) :
    print(visited[i])