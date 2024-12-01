# 피로도

# k : 피로도, cnt : 방문한 던전 수
def dfs(k, cnt, dungeons, visited) :
    global answer
    
    # 방문한 최대 던전 개수 갱신
    if cnt > answer :
        answer = cnt
        
    for i in range(len(dungeons)) :
        # 아직 방문하지 않았고, 필요 피로도 이상 가지고 있는 경우
        if (visited[i] is False) and (k >= dungeons[i][0]) :
            visited[i] = True
            dfs(k-dungeons[i][1], cnt+1, dungeons, visited)
            visited[i] = False

def solution(k, dungeons):
    global answer
    
    answer = 0
    # 방문 처리
    visited = [False] * len(dungeons)
    
    dfs(k, 0, dungeons, visited)
    
    return answer