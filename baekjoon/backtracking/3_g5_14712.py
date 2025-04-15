# 넴모넴모 (Easy)

## python으로 풀리지 않음(시간초과) -> pypy로는 통과
## 실제 시험에서는 이런 경우 없음 : 이런 경우는 pypy로 제출하여도 무방
## 알아둘 것 : pypy는 python보다 약 4.8배 빠름
## 마지막 main함수를 활용하면 조금 더 빠름

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# index를 맞춰 주기 위해서
matrix = [[0]*(m+1) for _ in range(n+1)]

ans = 0

def dfs(x, y) :
    global ans

    # matrix 행, 열의 끝까지 간 경우
    if (x, y) == (n+1, 1) :
        ans += 1
        return
    
    # matrix 행의 끝까지 간 경우
    if y == m :
        nx, ny = x+1, 1
    # 그 외의 경우
    else :
        nx, ny = x, y+1

    # 현재 위치(x, y)에 넣을 수 있는 경우
    if matrix[x][y-1] == 0 or matrix[x-1][y] == 0 or matrix[x-1][y-1] == 0 :
        matrix[x][y] = 1
        dfs(nx, ny)
        matrix[x][y] = 0

    # 현재 위치(x, y)를 넣지 않는 경우
    dfs(nx, ny)

def main() :
    dfs(1, 1)
    print(ans)

if __name__ == "__main__" :
    main()