# 사이클 게임

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n, m = map(int, input().split())

parents = [i for i in range(n)]

def find(x) :
    if parents[x] != x :
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y) :
    x = find(x)
    y = find(y)

    if x < y :
        parents[y] = parents[x]
    else : # y < x
        parents[x] = parents[y]

# 몇 번째에 끝났는지 확인
turn = 0

for _ in range(m) :
    turn += 1
    a, b = map(int, input().split())

    # 조건을 만족하는 경우
    if find(a) == find(b) :
        print(turn)
        break
    # 조건을 만족하지 않는 경우
    union(a, b)
else :
    print(0)