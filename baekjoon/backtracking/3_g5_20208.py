# 진우의 민트초코우유

import sys
input = sys.stdin.readline
from collections import deque

# n*n, 기초체력, 증가량
n, m, h = map(int, input().split())

# 집
home_x = -1
home_y = -1
# 민트 초코 위치
mints = []
# 마실 수 있는 최대 민트초코
ans = 0

for i in range(n) :
    row = list(map(int, input().split()))
    for j in range(n) :
        if row[j] == 1 :
            home_x = i
            home_y = j
        if row[j] == 2 :
            # x, y, 방문 check
            mints.append([i, j, False])

# (x, y), 체력, 민트초코의 수
def dfs(x:int, y:int, stamina:int, cnt:int) :
    global ans

    for mint in mints :
        # 해당 민트 초코까지의 거리
        dist = abs(mint[0]-x) + abs(mint[1]-y)

        # 갈 수 없는 경우
        if dist > stamina :
            continue

        # 아직 방문하지 않은 경우
        if mint[2] is False :
            # 방문 처리
            mint[2] = True
            new_stamina = stamina + h - dist
            dfs(mint[0], mint[1], new_stamina, cnt+1)
            mint[2] = False

    # 집으로 갈 수 있는 경우
    if stamina >= abs(x-home_x)+abs(y-home_y) :
        ans = max(ans, cnt)


dfs(home_x, home_y, m, 0)
print(ans)