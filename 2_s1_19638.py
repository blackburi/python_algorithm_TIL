# 센티와 마법의 뿅망치

import sys
input = sys.stdin.readline


n, h, t = map(int, input().split())
heights = [int(input().rstrip()) for _ in range(n)]
heights.sort()

# 뿅망치 사용 횟수
tmp = 0

while tmp < t :
    height = heights.pop()
    
    if height == 1 or height < h :
        break

    height //= 2
    heights.append(height)
    heights.sort()

    tmp += 1

if heights[-1] >= h :
    print('NO')
    print(heights[-1])
else :
    print('YES')
    print(tmp)