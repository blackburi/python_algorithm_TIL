# 최단 경로


import sys
input = sys.stdin.readline
import heapq
sys.setrecursionlimit(10**6)

# 정점의 개수, 간선의 개수
n, m = map(int, input().split())

# 시작 정점의 번호
start = int(input())

# 그래프
graph = [[] * (n+1) for _ in range(n+1)]

# 최단 거리
distance = [float('inf')] * (n+1)

# 간선 정보 입력
for _ in range(m) :
    s, e, c = map(int, input().split())
    # s -> e , c 비용
    graph[s].append((e, c))


def dijkstra(start) :
    q = []

    # 시작 노드로 가기 위한 최단 경로는 0으로 설정, q에 삽입
    # (0, start)형태로 넣는 이유는 python에서는 최소힙이 default
    # 따라서 (a, b)에서 a가 작을수록, b가 클수록 heappop을 사용시 먼저 나옴
    # cost가 작은 순서대로 원하기 때문에 0을 앞에, start를 뒤에 둔다.
    heapq.heappush(q, (0, start))

    distance[start] = 0

    while q :
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        # 이미 최단 거리라면
        if distance[now] < dist :
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now] :
            cost = dist + i[1]

            # 현재 노드를 거쳐서, 다른 노드로이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# dijkstra 실행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1) :
    if distance[i] == float('inf') :
        print("INF")
    else :
        print(distance[i])