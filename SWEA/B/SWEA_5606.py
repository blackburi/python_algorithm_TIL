# 두 개의 미로


from collections import deque

# 방향 설정
dir = ['N', 'E', 'W', 'S']

T = int(input())
for tc in range(1, T+1) :
    n = int(input())

    # 현민이의 미로 형태
    hm = deque(list(map(str, input())))
    print(hm)