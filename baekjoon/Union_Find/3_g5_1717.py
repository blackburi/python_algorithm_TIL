# 집합의 표현

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

parents = [i for i in range(n+1)]

def find(x) :
    if parents[x] != x :
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y) :
    x = find(x)
    y = find(y)

    # 작은 수를 대표 node로 지정
    if x > y :
        parents[x] = y
    else : # x <= y
        parents[y] = x

for _ in range(m) :
    idx, a, b = map(int, input().split())
    if idx == 0 :
        union(a, b)
    elif idx == 1 :
        if find(a) == find(b) :
            print("YES")
        else :
            print("NO")