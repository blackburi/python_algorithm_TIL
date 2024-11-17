# 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리를 모두 건너는데 걸리는 시간
    answer = 0
    
    # 다리 위에 있는 트럭
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    
    # 현재 다리 위 트럭의 무게 합
    total = 0
    
    while len(truck_weights) :
        answer += 1
        
        # 가장 왼쪽에 있는 트럭이 도착함
        total -= bridge.popleft()
        # 새로 들어오는 트럭이 들어올 수 있는 경우
        if total + truck_weights[0] <= weight :
            total += truck_weights[0]
            bridge.append(truck_weights.popleft())
        # 새로 들어오는 트럭이 들어올 수 없는 경우
        else :
            bridge.append(0)
    
    # truck_weights에 원소가 없더라도 마지막 트럭은 다리를 건너는 중이다.
    # 남은 시간을 더해줘야 한다.
    answer += bridge_length
    return answer