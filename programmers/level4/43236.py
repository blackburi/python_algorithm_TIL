# 징검다리

def solution(distance, rocks, n):
    answer = 0
    # 돌의 순서 정렬
    rocks.sort()
    # 마지막 계산을 위해 추가
    rocks.append(distance)
    
    left, right = 0, distance

    while left <= right :
        # 이전 돌
        prev_rock = 0
        # 돌 사이 거리의 최솟값
        min_length = 10**9
        # 제거한 돌의 수
        delete = 0
        
        # 바위 사이의 최소 거리
        mid = (left+right) // 2
        # rocks를 순회하며 제거
        for i in range(len(rocks)) :
            # 바위 사이의 최소 거리보다 거리가 작을 경우 돌 삭제
            if rocks[i] - prev_rock < mid :
                delete += 1
            else :
                min_length = min(min_length, rocks[i] - prev_rock)
                prev_rock = rocks[i]
                
        # 제거한 돌의 수가 기준보다 많을 경우
        if delete > n :
            right = mid - 1
        # 제거한 돌의 수가 기준보다 적을 경우
        else :
            answer = min_length
            left = mid + 1
    
    return answer