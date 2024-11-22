# 오목

import sys
input = sys.stdin.readline

mat = [list(map(int, input().rstrip().split())) for _ in range(19)]

# 오른쪽, 아랫쪽, 우상단, 우하단
dx = (0, 1, -1, 1)
dy = (1, 0, 1, 1)

for x in range(19) :
    for y in range(19) :
        # 바둑돌이 놓인 경우
        if mat[x][y] != 0 :
            # 바둑알의 색을 저장
            color = mat[x][y]

            # 방향 지정
            for i in range(4) :
                # 같은 바둑알의 수
                tmp = 1
                nx = x + dx[i]
                ny = y + dy[i]

                while 0 <= nx < 19 and 0 <= ny < 19 and mat[nx][ny] == color:
                    tmp += 1

                    if tmp == 5:
                        # 육목 체크
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and mat[x - dx[i]][y - dy[i]] == color:
                            break
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and mat[nx + dx[i]][ny + dy[i]] == color:
                            break
                        # 육목이 아니라면 -> 종료
                        print(color)
                        print(x + 1, y + 1)
                        sys.exit(0)

                    nx += dx[i]
                    ny += dy[i]

print(0)