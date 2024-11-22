# 이중우선순위큐

from heapq import *

def solution(operations):
    # heap 구조
    q = []
    
    for operation in operations :
        op, num = operation.split()
        num = int(num)
        
        if op == 'I' :
            heappush(q, num)
        else : # op == 'D'
            # q가 비어있다면 연산 무시
            if q :
                if num == 1 :
                    q.sort()
                    q.pop()
                elif num == -1 :
                    heappop(q)
    
    if q :
        return [max(q), min(q)]
    else : # q가 비어있다면
        return [0, 0]