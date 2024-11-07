def solution(participant, completion):
    dic = {}
    sum = 0
    
    # 1. Hash: Participant의 dictionary 만들기
    # 2. Participant의 sum 더하기
    for name in participant :
        dic[hash(name)] = name
        sum += hash(name)
        
    # 3. completion에서 sum 빼기
    for name in completion :
        sum -= hash(name)
    return dic[sum]