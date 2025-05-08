# 최소비용 구하기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 도시 수
n = int(input())
# 버스 수
m = int(input())

# 비용을 저장하는 graph : graph[a] = [(b, c)] : a번 노드에서 b번 노드로 가는 비용 c
graph = [[] for _ in range(n+1)]

for _ in range(m) :
    s, e, c = map(int, input().rstrip().split())
    graph[s].append((e, c))

start, end = map(int, input().rstrip().split())

# 비용
INF = int(1e9)
cost = [INF] * (n+1)
cost[start] = 0
# 방문처리
visited = [False] * (n+1)

def dijkstra(node) :
    # 비용 갱신
    for (e, c) in graph[node] :
        cost[e] = min(cost[e], cost[node]+c)

    # 방문 처리
    visited[node] = True

    min_cost = INF
    next_node = INF
    for i in range(1, n+1) :
        # 방문하지 않은 노드 중 가장 비용이 작으면서 번호가 작은 node선택
        if cost[i] < min_cost and visited[i] is False :
            next_node = i
            min_cost = cost[i]

    if next_node == INF :
        return

    dijkstra(next_node)

dijkstra(start)
print(cost[end])