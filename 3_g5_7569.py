# 토마토

import sys
input = sys.stdin.readline
from collections import deque

m, n, h = map(int, input().split())
# 저장되어 있는 상태
mat = [[list(map(int, input().rstrip().split())) for _ in range(n)] for _ in range(h)]
# 방문 처리
visited = [[[False]*m for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 다 익는데까지 걸리는 시간
answer = 0
# 초기 설정
q = deque()

# 토마토가 익어나가는 것을 보여주는 함수
def bfs() :
    while q :
        x, y, z = q.popleft()
        for i in range(6) :
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m :
                if mat[nx][ny][nz] == 0 and visited[nx][ny][nz] is False :
                    q.append((nx, ny, nz))
                    mat[nx][ny][nz] = mat[x][y][z] + 1
                    visited[nx][ny][nz] = True

# 초기 상태에서 익은 토마토
for x in range(h) :
    for y in range(n) :
        for z in range(m) :
            if mat[x][y][z] == 1 and visited[x][y][z] is False :
                q.append((x, y, z))
                visited[x][y][z] = True

bfs()

# 안익은 토마토가 있는 경우를 확인하는 변수
flag = 0

# 토마토 확인
for x in range(h) :
    for y in range(n) :
        for z in range(m) :
            if mat[x][y][z] == 0 :
                flag = 1
            if flag == 1 :
                break
            answer = max(answer, mat[x][y][z])
        if flag == 1 :
            break
    if flag == 1 :
        break

if flag == 1 :
    print(-1)
else :
    print(answer - 1)