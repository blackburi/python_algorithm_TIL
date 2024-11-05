# 나이트의 이동

import sys
input = sys.stdin.readline
from collections import deque

dx = (-2, -2, -1, -1, 1, 1, 2, 2)
dy = (-1, 1, -2, 2, -2, 2, -1, 1)

tc = int(input())
for _ in range(tc) :
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    visited = [[False]*l for _ in range(l)]
    answer = 0

    q = deque([(sx, sy, 0)])
    while q :
        x, y, cnt = q.popleft()
        if x == ex and y == ey :
            answer = cnt
            break

        for i in range(8) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] is False :
                visited[nx][ny] = True
                q.append((nx, ny, cnt+1))

    print(answer)