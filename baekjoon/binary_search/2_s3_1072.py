# 게임

import sys
input = sys.stdin.readline

x, y = map(int, input().rstrip().split())

z = (y*100)//x

answer = -1
bot = 0
top = 1000000000

while bot <= top :
    mid = (bot+top) // 2

    tmp = ((y+mid)*100) // (x+mid)
    if tmp > z :
        answer = mid
        top = mid - 1
    else : # tmp <= z
        bot = mid + 1

print(answer)