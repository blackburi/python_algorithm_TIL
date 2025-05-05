# 촌수계산

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
s, e = map(int, input().split())
m = int(input())

# 부모, 자식 관계로 연결되어 있음을 확인하는 graph
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 부모, 자식 관계로 연결되어 있지 않을경우 -1을 출력해야 하기 때문에
# default값을 -1로 설정
visited = [-1] *(n+1)
visited[s] = 0
q = deque([s])

while q :
    v = q.popleft()
    # 찾아야 하는 관계를 찾은 경우
    if v == e :
        break
    for num in graph[v] :
        if visited[num] == -1 :
            visited[num] = visited[v] + 1
            q.append(num)

print(visited[e])