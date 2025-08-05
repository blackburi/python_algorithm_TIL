# 겹치는 건 싫어

import sys
from collections import defaultdict
input = sys.stdin.readline


n, m = map(int, input().split())
numbers = defaultdict(int)
numberList = list(map(int, input().rstrip().split()))
start = 0

ans = 0

for end in range(n):
    numbers[numberList[end]] += 1

    # m번을 초과하면 start를 앞으로 이동
    while numbers[numberList[end]] > m:
        numbers[numberList[start]] -= 1
        start += 1

    ans = max(ans, end - start + 1)

print(ans)