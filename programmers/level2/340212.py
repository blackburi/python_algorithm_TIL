# 퍼즐 게임 챌린지

# mid값에 대해서 limit을 비교하는 함수
def check(dif, time, limit, level) :
    # index
    idx = 0
    # 퍼즐을 해결하는데 걸리는 시간
    now = 0

    while idx < len(dif) :
        if level >= dif[idx] :
            now += time[idx]
        else : # level < dif[idx]
            k = dif[idx] - level
            now += k*(time[idx-1] + time[idx]) + time[idx]

        if now >= limit :
            idx += 1
        else :
            break

    if idx == len(dif) :
        return True
    else : # idx != len(dif)
        return False


def solution(diffs, times, limit):
    answer = 0

    bot = 1
    top = 100000

    while bot <= top :
        mid = (bot + top) // 2

        if check(diffs, times, limit, mid) is True :
            answer = mid
            top = mid - 1
        else : # check(diffs, times, limit, mid) is False
            bot = mid + 1

    return answer