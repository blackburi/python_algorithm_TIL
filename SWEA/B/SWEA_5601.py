# 쥬스 나누기


T = int(input())
for tc in range(1, T+1) :
    n = int(input())

    ans = []
    for _ in range(n) :
        ans.append(f'1/{n}')

    print(f'#{tc}', ' '.join(ans))