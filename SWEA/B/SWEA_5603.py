# 건초더미


T = int(input())
for tc in range(1, T+1) :
    n = int(input())

    lst = []
    for _ in range(n) :
        lst.append(int(input()))

    # 목표 건초더미 1개당 크기
    one = sum(lst) // n

    ans = 0

    for i in range(n) :
        if lst[i] > one :
            ans += lst[i] - one

    print(f'#{tc} {ans}')