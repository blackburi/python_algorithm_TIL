# 우주 탐사선

import sys
input = sys.stdin.readline


def find(now, cnt, total) :
    global answer

    if cnt == n :
        answer = min(answer, total)
        return
    
    for next in range(n) :
        if visited[next] is False :
            visited[next] = True
            find(next, cnt+1, total+graph[now][next])
            visited[next] = False


n, k = map(int, input().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

# floyd-warshall
for r in range(n) :
    for p in range(n) :
        for q in range(n) :
            graph[p][q] = min(graph[p][q], graph[p][r] + graph[r][q])

# 방문 처리
visited = [False] * n
visited[k] = True
# 초기값 설정
answer = 1e9

find(k, 1, 0)
print(answer)