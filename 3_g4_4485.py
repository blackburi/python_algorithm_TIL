# 녹색 옷 입은 애가 젤다지?

import sys
input = sys.stdin.readline
import heapq

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

problem = 1

while True :
    n = int(input())
    if n == 0 :
        break

    mat = [list(map(int, input().rstrip().split())) for _ in range(n)]
    # 비용을 저장
    distance = [[float('inf')]*n for _ in range(n)]
    distance[0][0] = mat[0][0]

    # cost 기준으로 heap을 사용할 것이기 때문에 cost를 제일 앞에 둔다.
    q = []
    heapq.heappush(q, (mat[0][0], 0, 0))

    while q :
        cost, x, y = heapq.heappop(q)

        if x == n-1 and y == n-1 :
            break

        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < n and 0 <= ny < n :
                if cost + mat[nx][ny] < distance[nx][ny] :
                    distance[nx][ny] = cost + mat[nx][ny]
                    heapq.heappush(q, (cost+mat[nx][ny], nx, ny))

    print(f'Problem {problem}: {distance[n-1][n-1]}')
    problem += 1