# 영역 구하기

import sys
input = sys.stdin.readline
from collections import deque


m, n, k = map(int, input().split())
matrix = [[0]*n for _ in range(m)]
for _ in range(k) :
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(m-y1-1, m-y2-1, -1) :
        for j in range(x1, x2) :
            matrix[i][j] = 1

moves = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
)

# 결과 저장
result = []

def bfs(x, y) :
    # 초기 설정
    q = deque([(x, y)])
    matrix[x][y] = 1
    size = 1

    while q :
        x, y = q.popleft()
        for move in moves :
            nx = x + move[0]
            ny = y + move[1]
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] == 0 :
                matrix[nx][ny] = 1
                size += 1
                q.append((nx, ny))

    result.append(size)


for i in range(m) :
    for j in range(n) :
        if matrix[i][j] == 0 :
            bfs(i, j)

result.sort()
print(len(result))
print(*result)