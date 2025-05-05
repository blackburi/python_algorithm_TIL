# 빙산

import sys
input = sys.stdin.readline
from collections import deque

# 주변 바다를 체크하고 빙산의 높이를 낮추는 함수
def bfs(x, y) :
    q = deque([(x, y)])
    visited[x][y] = True
    # 주변 바다의 수를 체크하고 한번에 연산하기 위해 담아두는 list
    decrease = []

    while q :
        x, y = q.popleft()
        # 주변 바다의 수
        cnt = 0

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                # 바다인 경우
                if mat[nx][ny] == 0 :
                    cnt += 1
                # 바다는 아니지만 방문하지 않은 경우
                elif mat[nx][ny] != 0 and visited[nx][ny] is False :
                    q.append((nx, ny))
                    visited[nx][ny] = True
            
        if cnt > 0 :
            decrease.append((x, y, cnt))

    # 빙산의 높이를 낮춤
    for x, y, cnt in decrease :
        mat[x][y] = max(0, mat[x][y]-cnt)

    # 한 덩어리의 빙산임을 체크
    return 1



n, m = map(int, input().split())
mat = [list(map(int, input().rstrip().split())) for _ in range(n)]

ice = []
for i in range(n) :
    for j in range(m) :
        # 빙산이 있는 경우
        if mat[i][j] :
            ice.append((i, j))

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)
year = 0

while ice :
    # 방문 체크
    visited = [[False]*m for _ in range(n)]
    # 빙산이 다 녹은 경우
    delete = []
    # 덩어리 수
    group = 0

    for i, j in ice :
        # 빙산이 있고, 방문하지 않은 경우
        if mat[i][j] and visited[i][j] is False :
            group += bfs(i, j)
        # bfs로 인해 한번 얼음이 녹았음 -> 빙산이 녹은 경우가 존재
        if mat[i][j] == 0 :
            delete.append((i, j))

    # 빙산이 두 덩어리 이상인 경우
    if group > 1 :
        print(year)
        break

    # 빙산이 다 녹은 경우 제거
    ice = list(set(ice) - set(delete))
    # 1년 추가
    year += 1

# group이 2개 미만인 경우
if group < 2 :
    print(0)