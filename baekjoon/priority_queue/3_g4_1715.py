# 카드 정렬하기

"""
a, b, c 세 묶음이 있을 때
a, b, c 순서대로 합치는 경우 : (a+b) + (a+b+c)
a, c, b 순서대로 합치는 경우 : (a+c) + (a+c+b)

즉 카드 수가 적은 묶음을 먼저 묶어야 한다.
"""

import sys, heapq
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n) :
    cards = int(input())
    heapq.heappush(q, cards)

# 카드 묶음이 1개인 경우
if len(q) == 1 :
    print(0)
else : # len(q) >= 2
    ans = 0
    while len(q) >= 2 :
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        ans += a+b
        heapq.heappush(q, a+b)
    print(ans)