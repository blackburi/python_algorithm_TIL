# 모바일 광고 입찰

import sys
input = sys.stdin.readline


n, k = map(int, input().split())


mols = [list(map(int, input().rstrip().split())) for _ in range(n)]

def check(k, mols:list, add:int) :
    total = 0
    for mol in mols :
        if mol[0]+add >= mol[1] :
            total += 1
        if total >= k :
            return add
    else :
        return -1
    
start, end = 0, 10**9-1

while start < end :
    mid = (start + end)//2

    result = check(k, mols, mid)

    if result == -1 :
        start = mid+1
    else : # result != -1
        end = mid

print(end)
