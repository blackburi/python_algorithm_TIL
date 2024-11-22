# K번째 수

import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))
numbers.sort()

print(numbers[k-1])