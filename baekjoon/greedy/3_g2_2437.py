# 저울

import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().rstrip().split()))
numbers.sort()

check = 1

for num in numbers :
    if check < num :
        break
    check += num

print(check)