# 모음 사전

def solution(word):
    answer = 0
    letters = ['A', 'E', 'I', 'O', 'U']
    for i in range(len(word)) :
        tmp = 0
        for j in range(0, 5-i) :
            tmp += 5**j
        answer += tmp*letters.index(word[i]) + 1
    return answer