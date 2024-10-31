# 웜홀

import sys
input = sys.stdin.readline

def bellman_ford() :
    for i in range(n) :
        for (s, e, t) in edges :
            if times[e] > times[s] + t :
                times[e] = times[s] + t
                # n번째에 값이 또 갱신된다면 사이클이 존재한다는 뜻
                if i == n-1 :
                    return True
    return False

tc = int(input())

for _ in range(tc) :
    # 지점, 도로, 웜홀
    n, m, w = map(int, input().rstrip().split())

    edges = []
    times = [1e9]*(n+1)

    # 도로
    for _ in range(m) :
        s, e, t = map(int, input().rstrip().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    # 웜홀
    for _ in range(w) :
        s, e, t = map(int, input().rstrip().split())
        edges.append((s, e, -t))

    if bellman_ford() :
        print('YES')
    else :
        print('NO')