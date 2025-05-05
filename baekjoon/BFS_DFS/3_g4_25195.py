# Yes or yes

import sys
input = sys.stdin.readline
from collections import deque

# 정점, 간선 수
n, m = map(int, input().split())

# graph
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)

# 곰곰의 위치
s = int(input())
gomgom = list(map(int, input().rstrip().split()))

# 방문 처리
visited = [False] * (n+1)

def bfs() :
    q = deque()

    # 시작 위치는 1번 정점
    q.append(1)

    # 1번 정점에 곰곰이가 있는 경우
    if visited[1] :
        return 'Yes'
    
    visited[1] = True
    while q :
        v = q.popleft()

        # 곰곰을 만나지 않은 경우
        if not graph[v] :
            return 'yes'
        
        for next in graph[v] :
            if not visited[next] :
                visited[next] = True
                q.append(next)
    return 'Yes'

for gom in gomgom :
    visited[gom] = True

print(bfs())