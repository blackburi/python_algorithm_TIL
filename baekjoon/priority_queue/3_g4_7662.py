# 이중 우선순위 큐

import sys
input = sys.stdin.readline
import heapq


tc = int(input())
for _ in range(tc) :

    # 초기 설정 : 삽입한 숫자(존재하는 숫자)는 True, 삭제되거나 삽입한적 없는 숫자는 False
    visited = [False]*1000001
    # 초기 설정 : 이중 heapq
    minH, maxH = [], []

    process = int(input())
    for p in range(process) :
        func, num = input().split()
        # 삽입
        if func == "I" :
            heapq.heappush(minH, (int(num), p))
            heapq.heappush(maxH, (-int(num), p))
            visited[p] = True
        # 최댓값 삭제
        elif num == "1" :
            # maxH가 존재하고, visited가 False인 경우(minH에서 버려진 경우)
            while maxH and not visited[maxH[0][1]] :
                heapq.heappop(maxH)
            if maxH :
                visited[maxH[0][1]] = False
                heapq.heappop(maxH)
        # 최솟값 삭제
        elif num == "-1" :
            # minH가 존재하고, visited가 False인 경우(maxH에서 버려진 경우)
            while minH and not visited[minH[0][1]] :
                heapq.heappop(minH)
            if minH :
                visited[minH[0][1]] = False
                heapq.heappop(minH)

        # 모든 연산이 끝난 후 동기화
        while maxH and not visited[maxH[0][1]] :
            heapq.heappop(maxH)
        while minH and not visited[minH[0][1]] :
            heapq.heappop(minH)

    if minH and maxH :
        print(-maxH[0][0], minH[0][0])
    else :
        print("EMPTY")
