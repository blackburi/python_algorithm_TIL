# 나는 친구가 적다(Large)


import sys
input = sys.stdin.readline


word = input().rstrip()
need = input().rstrip()

for i in range(10) :
    word = word.replace(str(i), "")

if need in word :
    print(1)
else :
    print(0)