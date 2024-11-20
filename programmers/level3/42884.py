# 단속카메라

def solution(routes):
    answer = 0
    # 끝부분 순서로 정렬
    routes.sort(key = lambda x : x[1])
    print(routes)
    
    # 범위가 -30000~30000이기 때문에
    pos = -30001
    
    for route in routes :
        # 시작 지점이 현재 cctv 위치를 지나친 경우
        if route[0] > pos :
            answer += 1
            pos = route[1]
        
    return answer