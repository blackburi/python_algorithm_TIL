# 최소힙

import sys
input = sys.stdin.readline
import heapq

n = int(input())
q = []

for _ in range(n) :
    number = int(input())

    if number == 0 :
        if len(q) == 0 :
            print(0)
        else : # len(q) != 0
            tmp = heapq.heappop(q)
            print(tmp)
    else : # number가 자연수
        heapq.heappush(q, number)