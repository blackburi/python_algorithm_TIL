# 운동


# now : 현재 위치하고 있는 집의 번호
# total : 지금까지 도로 길이의 합
# finish : 최종적으로 돌아와야 하는 지점
def dfs(now, total, finish) :
    global answer

    if answer >= 0 and total >= answer :
        return

    if total > 0 and now == finish :
        if answer == -1 :
            answer = total
        else : # answer != -1
            answer = min(answer, total)

    for (end, cost) in graph[now] :
        if visited[now][end] == True :
            visited[now][end] = False
            dfs(end, total+cost, finish)
            visited[now][end] = True
        

T = int(input())
for tc in range(1, T+1) :
    # 건물의 수, 도로의 수
    n, m = map(int, input().split())
    # 간선 check
    graph = [[] for _ in range(n+1)]
    # 한번 지나간 road인지 확인, True는 아직 안감, False는 갔음
    visited = [[True]*(n+1) for _ in range(n+1)]
    # 정답 출력 (cycle이 없다면 -1을 출력하기 때문에 -1로 설정)
    answer = -1
    # m개의 줄을 걸쳐 s, e, c
    for _ in range(m) :
        s, e, c = map(int, input().split())
        # 시작점과 도착점이 같은 간선이라면 -> graph에 넣지 않고 바로 제외 시킴(cycle만 확인)
        if s == e :
            if answer == -1 :
                answer = c
            else : # answer != -1
                answer = min(answer, c)
        else :
            graph[s].append((e, c))


    # 시작점이 i
    for i in range(1, n+1) :
        dfs(i, 0, i)

    print(f'#{tc} {answer}')