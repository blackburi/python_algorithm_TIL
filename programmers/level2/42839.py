# 소수 찾기

from itertools import permutations

# 소수인지 체크하는 함수
def check(x) :
    if x < 2 :
        return False
    
    for i in range(2, x) :
        if x % i == 0 :
            return False
    return True


def solution(numbers):
    answer = []
    
    # 1~len(numbers)자리수를 갖는 수를 생성
    for i in range(1, len(numbers)+1) :
        # i자리수 정수 list 생성
        number = list(map(''.join, permutations(numbers, i)))
        # 동일한 수가 있다면 제거
        number = set(number)
        
        for num in number :
            if check(int(num)) :
                answer.append(int(num))
                
    answer = set(answer)
    return len(answer)