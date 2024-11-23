# 지름길

import sys
input = sys.stdin.readline

n, d = map(int, input().split())

dp = [i for i in range(d+1)]

# 지름길 저장
roads = []
for _ in range(n) :
    start, end, length = map(int, input().split())
    # 지름길인 경우
    if end - start > length :
        roads.append((start, end, length))

# start, end 순서대로 정렬
roads.sort()

for start, end, length in roads :
    for i in range(1, d+1) :
        # end의 경우 지름길로 갱신
        if end == i :
            dp[i] = min(dp[i], dp[start]+length)
        # end가 아닌경우 +1
        else :
            dp[i] = min(dp[i], dp[i-1]+1)

print(dp[-1])