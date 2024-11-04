# 전주 듣고 노래 맞히기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

musics = {}

for _ in range(n) :
    _, name, *letters = input().rstrip().split()
    musics[name] = letters

for _ in range(m) :
    lst = list(input().rstrip().split())

    check = 0
    answer = ''
    for name, value in musics.items() :
        if value[:3] == lst :
            answer = name
            check += 1
    
    if check == 0 :
        print('!')
    elif check == 1 :
        print(answer)
    else :
        print('?')