# 할리갈리

import sys
input = sys.stdin.readline

n = int(input())

dic = {}

for i in range(n) :
    word, number = input().split()
    if word in dic.keys() :
        dic[word] += int(number)
    else :
        dic[word] = int(number)

for key in dic.keys() :
    if dic[key] == 5 :
        print('YES')
        break
else :
    print('NO')