# 좋다

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))
arr.sort()

answer = 0
for i in range(n) :
    goal = arr[i]
    start = 0
    end = len(arr)-1

    while start < end :
        # arr에 0이 포함된 경우도 생각해야 한다.
        if arr[start] + arr[end] == goal :
            # start에 자기 자신이 되는 경우
            if start == i :
                start += 1
            # end에 자기 자신이 되는 경우
            elif end == i :
                end -= 1
            else :
                answer += 1
                break
        elif arr[start] + arr[end] > goal :
            end -= 1
        else : # arr[start] + arr[end] < goal
            start += 1
print(answer)