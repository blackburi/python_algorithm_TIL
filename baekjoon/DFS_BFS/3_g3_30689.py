# 미로 보수

import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

maze = [list(input().rstrip()) for _ in range(n)]
cost = [list(map(int, input().rstrip().split())) for _ in range(n)]

# 방문 처리
visited = [[False]*m for _ in range(n)]
# 사이클임을 판별하기 위한 list
q = deque()

dic = {
    'U' : (-1, 0),
    'D' : (1, 0),
    'R' : (0, 1),
    'L' : (0, -1),
}

# 필요한 cost 총량
total = 0

def dfs(x, y) :
    global total

    nx = x + dic[maze[x][y]][0]
    ny = y + dic[maze[x][y]][1]

    if 0 <= nx < n and 0 <= ny < m :
        # 방문한 적이 없는 경우
        if visited[nx][ny] is False :
            visited[nx][ny] = True
            q.append((nx, ny))
            dfs(nx, ny)
            q.pop()
        # 방문한 적이 있는 경우
        else :
            # 이번 cycle 또는 탈출 가능한 미로에서의 cost
            min_cost = float('inf')
            idx = len(q) - 1

            while idx >= 0 and (q[idx][0] != nx or q[idx][1] != ny) :
                # 사이클의 경우 cost가 가장 작은 값을 찾는다.
                i, j = q[idx]
                min_cost = min(min_cost, cost[i][j])
                idx -= 1

            # 저장해둔 배열이 있다면
            if idx >= 0 and q[idx][0] == nx and q[idx][1] == ny :
                # 점프대 설치
                total += min(min_cost, cost[q[idx][0]][q[idx][1]])

# matrix를 순회하며 방문처리하고, total값을 갱신한다.
for i in range(n) :
    for j in range(m) :
        if visited[i][j] is False :
            visited[i][j] = True
            q.append((i, j))
            dfs(i, j)
            q.pop()

print(total)