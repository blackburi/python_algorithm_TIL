# 다단계 칫솔 판매

def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    dic = {}

    for idx, name in enumerate(enroll) :
        dic[name] = idx
    
    for s, a in zip(seller, amount) :
        m = a*100
        while s != "-" and m>0 :
            idx = dic[s]
            answer[idx] += m - m//10
            m //= 10
            s = referral[idx]        
    return answer