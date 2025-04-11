# 넴모넴모 (Easy)

# 좌 -> 우, 상 -> 하 순서대로 배열
# 네모네모로 지워지지 않는 경우를 계속 count

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

ans = 0

grid = [[0]*m]*n

# 좌 -> 우, 상 -> 하 순서대로 네모 배열
# (a, b)를 확인하고 싶다면 (a-1, b-1), (a-1, b), (a, b-1) 확인
def check_nemo(a, b, n, m) :
    if 0 <= a-1 and a < n and 0 <= b-1 and b < m :
        if grid[a-1][b-1] and grid[a-1][b] and grid[a][b-1] :
            # 둘 수 없음
            return False
    # 둘 수 있음
    return True

def dfs(a, b, n, m) :
    global ans
    if a == n-1 and b == m-1 :
        ans += 1
        return

    if b+1 < m :
        can = check_nemo(a, b+1, n, m)
        if can is True :
            dfs(a, b+1, n, m)
            grid[a][b+1] = 1
            dfs(a, b+1, n, m)
            grid[a][b+1] = 0
        else :
            dfs(a, b+1, n, m)
    else : # b+1 >= m 즉 b == m-1
        dfs(a+1, 0, n, m)
        grid[a+1][b] = 1
        dfs(a+1, 0, n, m)
        grid[a+1][b] = 0

dfs(0, 0, n, m)
grid[0][0] = 1
dfs(0, 0, n, m)
print(ans)