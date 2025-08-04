# 2024는 무엇이 특별할까?

"""
<문제 풀이>

X(n) : n의 약수이면서 홀수인 양의 정수의 개수
Y(n) : n의 약수이면서 짝수인 양의 정수의 개수
Y(n) = X(n) * K 를 만족해야 함

n을 소인수 분해 하였을 때 소인수 2와 나머지를 묶는다고 생각하면
n = (2**m) * p      (이 떄 p는 홀수 소인수들의 곱)
X(n) : p에서 나올 수 있는 약수의 개수
Y(n) : 전체 약수의 개수 - X(n)

약수의 개수는 (지수+1)의 곱으로 이루어 지므로
(전체 약수의 개수) = (m+1) * X(n)
Y(n) = (전체 약수의 개수) - X(n) = m * X(n)
위의 식을 Y(n) = X(n) * K 에 대입하면
m * X(n) = X(n) * K
따라서 m = K

즉 n을 소인수분해 하였을 때, 2의 지수가 K가 되어야 한다.
"""

import sys
input = sys.stdin.readline


tc = int(input())
for _ in range(tc) :
    n, k = map(int, input().split())

    ans = (n >> k) - (n >> (k+1))

    print(ans)