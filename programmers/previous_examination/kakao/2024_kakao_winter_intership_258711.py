# 도넛과 막대 그래프

def solution(edges):
    # 생성 정점, 도넛, 막대, 8자
    answer = [0, 0, 0, 0]
    
    # 생성 정점의 간선 수 = 도넛 + 막대 + 8자
    # 생성 정점 : 들어오는 간선 0개, 나가는 간선 2개 이상
    # 막대 그래프 : 마지막 노드에서 들어오는 간선 1개, 나가는 간선 없음
    # 8자 그래프 : 중앙 노드에서 들어오는 간선 2개 이상, 나가는 간선 2개
    # 도넛 그래프 : 생성 정점의 간선 수 - 막대 - 8자
    
    # 노드 번호의 최댓값
    max_node = 0
    for i in range(len(edges)) :
        max_node = max(max_node, max(edges[i]))
        
    # 각 노드에서 나가고 들어오는 간선의 수를 check
    in_line = [0] * (max_node+1)
    out_line = [0] * (max_node+1)
    
    # 간선 정보 저장
    for out_node, in_node in edges :
        in_line[in_node] += 1
        out_line[out_node] += 1
        
    # 순회하며 각 경우를 체크
    for node in range(1, max_node+1) :
        # 생성 노드의 경우
        if in_line[node] == 0 and out_line[node] >= 2 :
            answer[0] = node
        # 막대 그래프
        elif in_line[node] >= 1 and out_line[node] == 0 :
            answer[2] += 1
        # 8자 그래프
        elif in_line[node] >= 2 and out_line[node] == 2 :
            answer[3] += 1
    # 도넛 그래프
    answer[1] = out_line[answer[0]] - answer[2] - answer[3]
    return answer