# 1, 2, 3 더하기 4

import sys
input = sys.stdin.readline

"""
1만 사용하는 경우는 반드시 존재 -> dp를 1로 초기화
2와 3이 추가되는 경우는 dp[i-2], dp[i-3]이다
중복해서 더해지면 안되므로 따로 더해준다.
"""

tc = int(input())

# 초기 설정 : 1만 사용하는 경우는 반드시 존재
dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]
    
for i in range(3, 10001):
    dp[i] += dp[i - 3]

for _ in range(tc):
    n = int(input())
    print(dp[n])