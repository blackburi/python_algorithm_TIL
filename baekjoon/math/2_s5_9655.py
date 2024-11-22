# 돌 게임

import sys
input = sys.stdin.readline

n = int(input())

if n % 4 == 0 :
    print('CY')
elif n % 4 == 1 or n % 4 == 3 :
    print('SK')
else : # n % 4 == 2
    print('CY')