# AC

import sys
input = sys.stdin.readline
from collections import deque


tc = int(input())
for _ in range(tc) :
    process = input().rstrip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(","))

    if n == 0 :
        arr = deque()

    # error일때 break할 변수
    flag = 0
    # reverse 횟수
    cnt = 0

    for pro in process :
        if pro == "R" :
            cnt += 1
        else : # pro == "D"
            if len(arr) == 0 :
                flag = 1
                print("error")
                break
            else : # len(arr) > 0
                if cnt % 2 == 0 :
                    arr.popleft()
                else : # cnt % 2 == 1
                    arr.pop()

    if flag == 0 :
        if cnt % 2 == 0 :
            print("["+",".join(arr)+"]")
        else : # cnt % 2 == 1
            arr.reverse()
            print("["+",".join(arr)+"]")