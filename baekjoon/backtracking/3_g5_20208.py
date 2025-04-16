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
            mints.append([i, j, 0])
print(mints)
# (x, y), 체력, 민트초코의 수
def dfs(x:int, y:int, stamina:int, cnt:int) :
    global ans

    # 집으로 갈 수 있는 경우
    if x == home_x and y == home_y :
        ans = max(ans, cnt)
        return
    
    for mint in mints :
        # 방문하지 않고, 갈 수 있는 민트 초코
        if mint[2] == 0 and abs(mint[0]-x)+abs(mint[1]-y) <= stamina :
            # 방문하는 경우
            mint[2] = 1
            new_stamina = stamina + h - (abs(mint[0]-x)+abs(mint[1]-y))
            # stamina는 초기 체력 이상으로 올라갈 수 없음
            new_stamina = min(m, new_stamina)
            dfs(mint[0], mint[1], new_stamina, cnt+1)
            # 방문하지 않는 경우
            mint[2] = 0
            continue


dfs(home_x, home_y, m, 0)
print(ans)