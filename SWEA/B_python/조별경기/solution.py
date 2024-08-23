# 점수를 전부 갱신하는 것이 아닌
# 점수의 차를 갱신 + find함수를 실행했을때 parent가 갱신되므로
# 그에 따라 점수 차이도 갱신되어야 하는데 제대로 갱신되지 않음

def init(N):
    global parent, score_dif, find

    # 선수 번호를 index와 맞춘다.
    # 각 선수는 자기 자신이 팀의 root가 된다.
    parent = [i for i in range(N+1)]

    # 개별 선수 score
    # 점수를 바로 계산하지 않고 루트 노드와의 점수 차이만을 저장
    score_dif = [0] * (N+1)

    def find(x):
        if parent[x] != x:
            # 경로가 최신화 -> 점수도 최신화 되어야 한다.
            score = score_dif[x]
            y = x
            while True :
                root = parent[y]
                if root == parent[root] :
                    break
                score += score_dif[root]
                y = root
            score_dif[x] = score
            # parent[x] 값 갱신
            parent[x] = find(parent[x])
    return parent[x]


def updateScore(mWinnerID, mLoserID, mScore):
    rootWinner = find(mWinnerID)
    rootLoser = find(mLoserID)

    # 최상단 노드만 점수를 갱신
    score_dif[rootWinner] += mScore
    score_dif[rootLoser] -= mScore
    return


def unionTeam(mPlayerA, mPlayerB):
    rootA = find(mPlayerA)
    rootB = find(mPlayerB)

    # 같은 팀원인 경우는 주어지지 않음

    # 팀을 합칠때, 최상단 노드 번호가 작은 순서대로 배치한다.
    # 점수는 갱신하지 않고 부모 노드와의 점수 차만 갱신
    if rootA < rootB :
        parent[rootB] = rootA
        score_dif[rootB] -= score_dif[rootA]
    else :
        parent[rootA] = rootB
        score_dif[rootA] -= score_dif[rootB]
    return


def getScore(mID):
    find(mID)
    return score_dif[mID]