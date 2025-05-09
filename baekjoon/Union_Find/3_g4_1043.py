# 거짓말

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
know_num, *knows = list(map(int, input().rstrip().split()))

# parents : 0은 사실을 아는 사람들
parents = [i for i in range(n+1)]

for know in knows :
    parents[know] = 0

def find(x) :
    if parents[x] != x :
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y) :
    x = find(x)
    y = find(y)
    if x > y :
        parents[x] = y
    else : # y <= x
        parents[y] = x

# party 저장 및 같은 party 참석자끼리 union
parties = []
for _ in range(m) :
    _, *members = list(map(int, input().rstrip().split()))
    parties.append(members)
    if len(members) >= 2 :
        standard = members.pop()
        for i in range(len(members)) :
            union(members[i], standard)

# parents 갱신
for i in range(1, n+1) :
    find(i)

ans = 0

for party in parties :
    # member가 사실을 알고 있다면 break, 모든 파티원이 사실을 모른다면 +1
    for mem in party :
        if parents[mem] == 0 :
            break
    else :
        ans += 1

print(ans)