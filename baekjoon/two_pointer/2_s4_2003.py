# 수들의 합2

import sys
input = sys.stdin.readline


n, m = map(int, input().split())
numbers = list(map(int, input().rstrip().split()))

start, end = 0, 0

# 정답의 수
ans = 0

while end <= n :
    total = sum(numbers[start:end])

    if total < m :
        end += 1
    elif total > m :
        start += 1
    else : # total == m
        ans += 1
        end += 1

print(ans)