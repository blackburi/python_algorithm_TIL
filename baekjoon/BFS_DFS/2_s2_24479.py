# 알고리즘 수업 - 깊이 우선 탐색

# solution1 : 재귀
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, r = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]

for _ in range(m) :
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1) :
    graph[i].sort()

# 방문 순서 list
visited = [0]*(n+1)
visited[r] = 1

# 방문 순서
turn = 2

# 시작 정점, 방문 순서 list
def dfs(v, visited) :
    global turn
    for i in graph[v] :
        if visited[i] == 0 :
            visited[i] = turn
            turn += 1
            dfs(i, visited)
    return

dfs(r, visited)

for i in range(1, n+1) :
    print(visited[i])



# solution2 : stack
import sys
input = sys.stdin.readline
from collections import deque

n, m, r = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]

for _ in range(m) :
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1) :
    # 번호가 작은 순서부터 출력되어야 하기 때문에
    # 역순으로 q에 넣어주기 위해 reverse=True를 이용한다.
    graph[i].sort(reverse=True)

# 방문 순서 list
visited = [0]*(n+1)
# 방문 순서 번호
turn = 1

q = deque([r])
while q :
    v = q.pop()

    # 방문한 적이 없다면 방문 처리 후 turn += 1
    if visited[v] == 0 :
        visited[v] = turn
        turn += 1

    # 방문한 적이 없는 정점만 넣어준다.
    for i in graph[v] :
        if visited[i] == 0 :
            q.append(i)

for i in range(1, n+1) :
    print(visited[i])
