# 연결 요소의 개수


import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 대표 node 설정
parents = [i for i in range(n+1)]


def find(x) :
    if parents[x] != x :
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y) :
    x = find(x)
    y = find(y)

    # 작은 수를 대표자 node로 지정
    if x > y :
        parents[x] = y
    else : # x <= y
        parents[y] = x

for _ in range(m) :
    a, b = map(int, input().split())
    if find(a) != find(b) :
        union(a, b)

for i in range(1, n+1) :
    find(i)

parents = set(parents)
# 0 제외
answer = len(parents) - 1

print(answer)