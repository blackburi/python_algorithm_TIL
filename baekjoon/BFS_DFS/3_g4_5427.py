# 불

import sys
from collections import deque
input = sys.stdin.readline


# sf : 상근 or fire
def bfs(sf:str, q:deque, visited:list) :
    while q :
        x, y, time = q.popleft()
        for move in moves :
            nx = x + move[0]
            ny = y + move[1]
            if 0 <= nx < n and 0 <= ny < m :
                if matrix[nx][ny] in [".", "@"] :
                    if visited[nx][ny] > time+1 :
                        visited[nx][ny] = time + 1
                        q.append((nx, ny, visited[nx][ny]))
            # 상근이가 범위를 벗어나는 순간 -> 탈출 성공
            elif sf == "s" :
                print(time+1)
                return
    # 상근이가 탈출하지 못하는 경우
    if sf == "s" :
        print("IMPOSSIBLE")


moves = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
)

INF = float("inf")

tc = int(input())
for _ in range(tc) :
    m, n = map(int, input().split())

    # 초기 설정
    matrix = []
    visited = [[INF]*m for _ in range(n)]
    fire = deque()
    sg = deque()

    for i in range(n) :
        line = list(input().rstrip())
        matrix.append(line)
        for j in range(m) :
            if line[j] == "@" :
                sg.append((i, j, 0))
            elif line[j] == "*" :
                visited[i][j] = 0
                fire.append((i, j, 0))

    bfs('f', fire, visited)
    bfs('s', sg, visited)

