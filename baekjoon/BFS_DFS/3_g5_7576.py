# 토마토

import sys
from collections import deque
input = sys.stdin.readline


moves = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
)

m, n = map(int, input().split())
answer = 0

matrix = []
for _ in range(n) :
    sub = list(map(int, input().rstrip().split()))
    matrix.append(sub)

q = deque()
for i in range(n) :
    for j in range(m) :
        if matrix[i][j] == 1 :
            q.append((i, j))

while q :
    x, y = q.popleft()
    for move in moves :
        nx = x+move[0]
        ny = y+move[1]
        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0 :
            matrix[nx][ny] = matrix[x][y] + 1
            q.append((nx, ny))

for line in matrix :
    for num in line :
        if num == 0 :
            print(-1)
            exit(0)
    answer = max(answer, max(line))
print(answer-1)