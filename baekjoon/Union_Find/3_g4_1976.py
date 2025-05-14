# 여행 가자

import sys
input = sys.stdin.readline


# 최적의 경로가 아닌 방문 가능성을 묻는 문제이기 때문에 union find를 활용하여 같은 묶음에 있는지 확인하면 된다.

n = int(input())
m = int(input())

parents = [i for i in range(n+1)]

# 대표 node를 찾는 함수
def find(x) :
    if parents[x] != x :
        parents[x] = find(parents[x])
    return parents[x]

# 대표 node가 동일하도록 합치는 함수 -> 번호가 작은 node를 대표 node로 설정
def union(x, y) :
    x = find(x)
    y = find(y)

    if x > y :
        parents[x] = y
    else : # y < x
        parents[y] = x

for i in range(1, n+1) :
    link = list(map(int, input().rstrip().split()))
    for j in range(n) :
        if link[j] == 1 :
            union(i, j+1)

for i in range(n+1) :
    find(i)

# 목표 도시들
cities = list(map(int, input().rstrip().split()))
# 가능한지 확인하는 변수
flag = 0

for city in cities :
    if flag == 0 :
        flag = parents[city]
    elif flag == parents[city] :
        continue
    else : # flag != parents[city]
        flag = -1
        break

if flag == -1 :
    print("NO")
else :
    print("YES")