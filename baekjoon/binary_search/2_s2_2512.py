# 예산

import sys
input = sys.stdin.readline

n = int(input())
budgets = list(map(int, input().rstrip().split()))
m = int(input())

answer = 0

bot = 0
top = max(budgets)

while bot <= top :
    mid = (bot + top) // 2

    total = 0
    for budget in budgets :
        if budget <= mid :
            total += budget
        else : # budget > mid
            total += mid

    if total < m :
        answer = mid
        bot = mid + 1
    elif total > m :
        top = mid - 1
    else : # total == m
        answer = mid
        break

print(answer)