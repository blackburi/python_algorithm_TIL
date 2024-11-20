# 강의실

import sys
input = sys.stdin.readline
import heapq

n = int(input())

# 강의 정보를 담는 list
lectures = []

for _ in range(n) :
    _, s, e = map(int, input().rstrip().split())
    lectures.append((s, e))

# 시작 시간이 작은 순서대로 정렬
lectures.sort(key = lambda x : x[0])

# 필요한 강의실의 수
cnt = 0

q = []
for lecture in lectures :
    # 가장 일찍 끝나는 시간보다 시작 시간이 크면 -> 겹치지 않는다면
    while q and q[0] <= lecture[0] :
        heapq.heappop(q)
    # 끝나는 시간을 넣어준다. -> 처음에 시작 시간을 기준으로 정렬했기 때문에
    heapq.heappush(q, lecture[1])
    # 현재 q에 담긴 강의 정보는 모두 시간이 겹치는 것
    cnt = max(cnt, len(q))

print(cnt)