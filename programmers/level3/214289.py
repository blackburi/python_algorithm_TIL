# 에어컨 : 2023 현대모비스 알고리즘 경진대회 예선


def solution(temperature, t1, t2, a, b, onboard):
    # index를 맞추기 위해 전부 0이상의 정수로 바꿔준다
    temperature += 10
    t1 += 10
    t2 += 10

    length = len(onboard)

    # 현재 시점 i, 현재 온도 j인 최소비용 dp[i][j]를 저장할 dp
    INF = float("inf")
    dp = [[INF]*51 for _ in range(length)]
    # 초기 setting
    dp[0][temperature] = 0

    # 조건에 부합하는지 check 하는 함수
    def check(idx, tmp) :
        if not onboard[idx] :
            return True
        elif onboard[idx] and t1 <= tmp <= t2 :
            return True
        else :
            return False

    for i in range(length-1) :
        for j in range(51) :
            # 갱신되지 않은 곳 -> 온도 변화로 갈 수 없는 곳
            if dp[i][j] == INF :
                continue

            # 에어컨 off했을 때 다음 온도 k
            if j < temperature :
                k = j+1
            elif j > temperature :
                k = j-1
            else : # j == temperature
                k = j

            # 다음이 조건을 만족한다면
            if check(i+1, k) :
                dp[i+1][k] = min(dp[i+1][k], dp[i][j])

            # 에어컨을 on했을 때 다음 온도 k
            for k, cost in ((j+1, a), (j-1, a), (j, b)) :
                # 조건을 만족하지 않는 경우
                if not check(i+1, k) or not -1 < k < 51 :
                    continue
                # 조건을 만족하는 경우
                dp[i+1][k] = min(dp[i+1][k], dp[i][j] + cost)

    return min(dp[-1])