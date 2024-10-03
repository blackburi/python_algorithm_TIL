# 낚시왕

import sys
input = sys.stdin.readline

r, c, m = map(int, input().split())

# 낚시 정보
mat = [[[0, 0, 0, 0, 0] * c] for _ in range(r)]
# 상어의 위치(r, c), 속력, 이동방향, 크기
# 1위, 2아래, 3오른쪽, 4왼쪽
for _ in range(m) :
    a, b, s, d, z = map(int, input().split())
    sharks.append([a, b, s, d, z])

# 낚시왕이 있는 열
king = 1
# 낚시왕이 잡은 상어의 크기의 합
total = 0

# 상어를 이동
def move() :
    new_mat = [[[0, 0, 0, 0, 0] * c] for _ in range(r)]
    for i in range(r) :
        for j in range(c) :
            if mat[i][j] != [0, 0, 0, 0, 0] :
                a, b, s, d, z = mat[i][j]
                if d == 1 :
                    a = 
                elif d == 2 :

                elif d == 3 :

                else : # d == 4

    return

# 낚시왕을 이동 -> 상어를 잡는다
def catch(total) :
    return

# 낚시왕이 오른쪽 열보다 오른쪽으로 가면 멈춘다.
while king > c :
    move()
    catch()
    king += 1