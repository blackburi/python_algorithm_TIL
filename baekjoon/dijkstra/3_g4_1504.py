# 특정한 최단 경로

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

u, v = map(int, input().split())

def dijkstra(start) :
    # 초기 설정
    distance = [INF] * (n+1)
    q = []

    # dist = 0
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q :
        dist, now = heapq.heappop(q)

        if distance[now] < dist :
            continue

        for (next_node, next_cost) in graph[now] :
            cost = dist + next_cost

            if distance[next_node] > cost :
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    # 거리 배열 반환
    return distance

# 출발점이 1, u, v일때 최단 거리 배열
start_distance = dijkstra(1)
u_distance = dijkstra(u)
v_distance = dijkstra(v)

# 1 -> u -> v -> n
u_v_path = start_distance[u] + u_distance[v] + v_distance[n]
# 1 -> v -> u -> n
v_u_path = start_distance[v] + v_distance[u] + u_distance[n]
# total path
total = min(u_v_path, v_u_path)

if total >= INF :
    print(-1)
else :
    print(total)