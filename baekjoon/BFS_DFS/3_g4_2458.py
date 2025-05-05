# 키순서

# solution1 - floyd warshall : pypy 통과, python 시간 초과
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
height = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m) :
    tall, short  = map(int, input().split())
    height[tall][short] = 1

# floyd warshall
for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            if height[i][j] == 1 or (height[i][k] == 1 and height[k][j] == 1) :
                # 자신보다 작은 경우
                height[i][j] = 1

answer = 0
for i in range(1, n+1) :
    # 내 키의 순서를 알고 있는 경우
    know = 0
    for j in range(1, n+1) :
        # 나보다 작은 사람 + 큰 사람
        know += height[i][j] + height[j][i]
    # 자신의 키의 순서를 아는 경우
    if know == n-1 :
        answer += 1

print(answer)



# solution2 - DFS : python, pypy 모두 통과
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
height = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, input().split())
    if b not in height[a] :
        height[a].append(b)

# 키 순서 체크 함수
def dfs(i, idx, height) :
    for j in height[idx] :
        if not check[i][j] :
            check[i][j], check[j][i] = 1, 1
            dfs(i, j, height)

# 키 순서 check
check = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1) :
    check[i][i] = 1
    dfs(i, i, height)

answer = 0
for row in check :
    if row == [0]+[1]*n :
        answer += 1

print(answer)