# 더 맵게

from heapq import heapify, heappush, heappop

def solution(scoville, K):
    # heapq로 변환
    heapify(scoville)
    # 횟수
    answer = 0
    
    while len(scoville) > 1 :
        a = heappop(scoville)
        if a >= K :
            heappush(scoville, a)
            break
        
        b = heappop(scoville)
        heappush(scoville, a+2*b)
        answer += 1
        
    if scoville[0] >= K :
        return answer
    else :
        return -1