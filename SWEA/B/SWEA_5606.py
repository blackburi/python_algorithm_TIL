# 두 개의 미로


# 방향 설정
dir = ['N', 'E', 'W', 'S']

# 한명이 못움직이는 경우
stop = [
    ('N', 'E'),
    ('N', 'W'),
    ('S', 'E'),
    ('S', 'w'),
    ('E', 'N'),
    ('E', 'S'),
    ('W', 'N'),
    ('W', 'S'),
]

T = int(input())
for tc in range(1, T+1) :
    n = int(input())

    # 현민이의 미로 형태
    hm = list(map(str, input()))
    # 정우의 미로 형태
    jw = list(map(str, input()))

    # 현민이의 현재 위치 index
    now_hm = 0
    # 정우의 현재위치 index
    now_jw = 0

    while now_hm < n or now_jw < 0 :
        if hm[now_hm] == jw[now_jw] :
            now_hm += 1
            now_jw += 1
        elif 