# 거스름돈

import sys
input = sys.stdin.readline

n = int(input())

if n == 1 or n == 3:
    print(-1)
# 5원으로 최대한 바꿀수 있는 경우 ex) 12원
elif (n % 5) % 2 == 0 :
    print(n//5 + (n%5)//2 )
# 5원으로 최대한 바꿀수 없는 경우 ex) 13원
else : # (n % 5) % 2 == 1
    # 5원짜리 동전의 개수
    five = n//5 - 1
    two = (n - five*5)//2
    print(five + two)