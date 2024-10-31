# 숫자 문자열과 영단어

# sol1 : replace() 함수를 활용한 풀이
dic = {
    'zero' : '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9',
}

def solution(s):
    for key in dic :
        s = s.replace(key, dic[key])
    return int(s)


# sol2 : replace() 함수를 모르는 경우
dic = {
    'zero' : '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9',
}

def solution(s):
    answer = ''
    tmp = ''
    for i in s :
        # i가 숫자(형태의 문자)인 경우
        if i in '0123456789' :
            answer += i
        # i가 문자인 경우
        else :
            # 임시 문자열에 저장
            tmp += i
            # 만약 i가 dic에 있는 key값이라면
            if tmp in dic :
                # 정답에 넣어주고
                answer += dic[tmp]
                # 임시 문자열 초기화
                tmp = ''
                
    return int(answer)