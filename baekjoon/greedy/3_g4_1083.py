# 소트

import sys
input = sys.stdin.readline


n = int(input())
numbers = list(map(int, input().rstrip().split()))
s = int(input())


for i in range(n-1) :
    if s == 0 :
        break

    number, idx = numbers[i], i
    for j in range(i+1, min(n, i+s+1)) :
        if number < numbers[j] :
            number = numbers[j]
            idx = j
    s -= idx - i
    for k in range(idx, i, -1) :
        numbers[k] = numbers[k-1]
    numbers[i] = number

print(*numbers)