# 입국 심사

def check(n, t, times) :
    total = 0
    for time in times :
        total += t // time
        if total >= n :
            break
    return total


def solution(n, times):
    answer = 0
    
    bot = 0
    top = max(times)*n
    
    while bot <= top :
        mid = (bot+top)//2
        tmp = check(n, mid, times)
        if tmp >= n :
            top = mid-1
            answer = mid
        else : # tmp < n
            bot = mid+1
    return answer