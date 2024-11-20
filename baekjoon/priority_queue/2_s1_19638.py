# 센티와 마법의 뿅망치

import sys
input = sys.stdin.readline
import heapq

n, h, t = map(int, input().rstrip().split())

# python은 최소힙을 지원 -> 최대값을 찾기 위해서는 음수로 삽입
giants = [-int(input()) for _ in range(n)]
# list -> heapq로 변환
heapq.heapify(giants)

# 망치로 때린 횟수
cnt = 0

for i in range(t) :
    # 가장 큰 거인의 키가 1이거나 이미 센티보다 키가 작은 경우
    if -giants[0] == 1 or -giants[0] < h :
        break
    # 가장 큰 거인의 키가 센티보다 큰 경우
    else :
        # 가장 큰 키의 거인의 키를 반으로 줄인다.
        heapq.heapreplace(giants, -(-giants[0]//2))
        cnt += 1

if -giants[0] >= h :
    print('NO')
    print(-giants[0])
else : # -giant[0] < h
    print('YES')
    print(cnt)