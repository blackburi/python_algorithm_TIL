# 크기가 작은 부분 문자열

def solution(t, p):
    answer = 0
    n = len(p)
    
    for i in range(len(t)-n+1) :
        number = int(t[i:i+n])
        if number <= int(p) :
            answer += 1
    
    return answer