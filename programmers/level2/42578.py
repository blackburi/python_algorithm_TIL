# 의상

def solution(clothes):
    answer = 1
    
    # 의상을 종류별로 저장
    dic = {}
    
    for i in range(len(clothes)) :
        name, category = clothes[i]
        if category in dic.keys() :
            dic[category] += 1
        else :
            dic[category] = 1
    
    for key in dic.keys() :
        answer *= dic[key]+1

    return answer-1