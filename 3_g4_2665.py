# 미로만들기

import sys
input = sys.stdin.readline
from collections import deque


n = int(input())

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

mat = [list(map(int, input().rstrip())) for _ in range(n)]

# 검은 벽 -> 흰 벽으로 바꾼 횟수를 저장하여 방문 처리
visited = [[-1]*n for _ in range(n)]
visited[0][0] = 0

# x, y
q = deque([(0, 0)])

while q :
    x, y = q.popleft()

    # 목표 지점에 도착한 경우
    if x == n-1 and y == n-1 :
        break
    
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 :
            # 흰 방을 지날 경우
            if mat[nx][ny] == 1 :
                # 흰 방 우선탐색을 위해 appendleft
                q.appendleft((nx, ny))
                visited[nx][ny] = visited[x][y]
            # 검은 방을 지날 경우
            else :
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

print(visited[n-1][n-1])