# 회장 뽑기

import sys
input = sys.stdin.readline
from collections import deque

# 회원의 수
n = int(input())
graph = [[] for _ in range(n+1)]

while True :
    a, b = map(int, input().rstrip().split())
    if a == -1 :
        break

    graph[a].append(b)
    graph[b].append(a)

# 회장 후보의 점수
point = float('inf')
# 제일 작은 점수의 index
idx = []

# 회원 번호가 idx인 회원의 점수
def check(idx) :
    points = [0]*(n+1)
    
    q = deque([idx])

    while q :
        num = q.popleft()
        for i in graph[num] :
            if not points[i] :
                q.append(i)
                points[i] = points[num] + 1

    # 자기 자신은 초기화
    points[idx] = 0

    return max(points)

for number in range(1, n+1) :
    tmp = check(number)
    if point == tmp :
        idx.append(number)
    elif point > tmp :
        idx = [number]
        point = tmp

print(point, len(idx))
print(*idx)