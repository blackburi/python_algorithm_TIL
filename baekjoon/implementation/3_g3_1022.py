# 소용돌이 예쁘게 출력하기

import sys
input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().split())
arr = [[0]*(c2-c1+1) for _ in range(r2-r1+1)]
# 자릿수를 저장하는 함수
cnt = 0


def cal(r, c) :
    # 가장 바깥줄을 기준으로 센다.
    tmp = max(abs(r), abs(c))
    # 가장 왼쪽의 가장 상단의 수
    num = (tmp*2-1)**2 + 1

    if r == tmp :
        return num + tmp*7 + c - 1
    elif c == -tmp :
        return num + tmp * 5 + r - 1
    elif r == -tmp :
        return num +  tmp * 3 - c - 1
    else : # c == tmp
        return num + tmp - r - 1

# 각 행열에 해당하는 수를 cal함수를 통해 찾아준다.
for i in range(r1, r2+1) :
    for j in range(c1, c2+1) :
        arr[i-r1][j-c1] = cal(i, j)
        # 최댓값의 자릿수에 맞추기 위해 최댓값으 자릿수 갱신
        cnt = max(cnt, arr[i-r1][j-c1])

for i in range(r2-r1+1) :
    for j in range(c2-c1+1) :
        # 수들을 오른쪽 정렬하고, 자릿수가 맞지 않는 수들은 자릿수를 맞춰준다.
        print(str(arr[i][j]).rjust(len(str(cnt))), end=' ')
    print()