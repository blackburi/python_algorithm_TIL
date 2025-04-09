# 소풍

import sys
input = sys.stdin.readline

def dfs(idx:int, relation:list):
    # 조건을 충족하는 경우
    if len(relation) == k:
        for re in relation:
            print(re)
        exit()

    for i in range(idx+1, n+1) :
        # i가 relation의 모든 사람과 친구인지 확인
        for re in relation:
            if re not in graph[i]:
                break
        # 친구라면
        else:
            # relation에 추가
            relation.append(i)
            dfs(i, relation)
            # relation에서 삭제
            relation.pop()


k, n, f = map(int, input().split())

graph = {i: [] for i in range(1, n+1)}
for _ in range(f):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1) :
    dfs(i, [i])

print(-1)