# 식당 입구 대기 줄

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
# 줄의 길이가 최대일 때 길이 및 맨 뒤 번호
length = 0
number = float('inf')

# 학생 대기줄
q = deque()

for _ in range(n) :
    lst = list(map(int, input().rstrip().split()))
    # 1번 인 경우
    if lst[0] == 1 :
        q.append(lst[1])
        # 대기줄의 길이가 이전 최대 대기줄의 길이와 같은 경우
        if len(q) == length :
            length = len(q)
            # 번호가 작은 학생의 번호로 갱신
            number = min(number, q[-1])
        # 대기줄의 길이가 이전 최대 대기줄의 길이보다 긴 경우
        elif len(q) > length :
            length = len(q)
            number = q[-1]
    # 2번의 경우
    else : # lst[0] == 2
        q.popleft()

print(length, number)