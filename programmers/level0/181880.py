# 1로 만들기

def div(k) :
    cnt = 0
    while k > 1 :
        k = (k - 1) // 2 if k % 2 else k // 2
        cnt += 1
    return cnt

def solution(num_list):
    answer = 0
    answer += sum(div(num) for num in num_list)
    return answer