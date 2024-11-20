# 모의고사

def solution(answers):
    answer = []
    
    # 정답을 맞춘 갯수
    sol = [0, 0, 0]
    
    one = [1, 2, 3, 4, 5] * 2000
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    for i in range(len(answers)) :
        ans = answers[i]
        if one[i] == ans :
            sol[0] += 1
        if two[i] == ans :
            sol[1] += 1
        if three[i] == ans :
            sol[2] += 1
            
    M = max(sol)
    
    for i in range(3) :
        if M == sol[i] :
            answer.append(i+1)
    
    return answer