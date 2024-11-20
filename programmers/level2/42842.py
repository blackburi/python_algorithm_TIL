# 카펫

import math

def solution(brown, yellow):
    # 노란색 타일의 가로와 새로 길이를 각각 r, c라 하면 (r >= c)
    # r*c = yellow
    # 2*(r+c)+4 = brown
    brown = (brown-4)//2
    # r == c 인 경우
    if brown**2 == 4*yellow :
        r = brown//2
        c = brown//2
    # r != c 인 경우
    else :
        r = (brown + math.sqrt(brown**2-4*yellow))//2
        c = (brown - math.sqrt(brown**2-4*yellow))//2
    
    answer = [r+2, c+2]
    return answer