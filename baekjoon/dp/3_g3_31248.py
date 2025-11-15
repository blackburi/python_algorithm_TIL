# 3+1 하노이 탑

import sys
input = sys.stdin.readline


n = int(input().rstrip())

#
dp = [0, 1]
for i in range(2, 21) :
    dp.append(2**(i-2)+2+dp[i-2])
print(dp[n])

# start, end는 각각 기둥의 index를 보여줌
def move(disks:int, start:int, end:int) :
    if disks == 0 :
        return
    
    move(disks-1, start, 3-start-end)
    print("ABC"[start], "ABC"[end])
    move(disks-1, 3-start-end, end)

# 현재 disks가 쌓여있는 기둥의 index
pos = 0
while n >= 2 :
    move(n-2, pos, 2-pos)
    print("ABC"[pos], "B")
    print("ABC"[pos], "D")
    print("B", "D")

    n -= 2
    pos = 2-pos

# 남은 disk 처리
if n == 1 :
    print("ABC"[pos], "D")