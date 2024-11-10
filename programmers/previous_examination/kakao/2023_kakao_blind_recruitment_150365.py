# 미로 탈출 명령어

def solution(n, m, x, y, r, c, k):
    answer = ''

    # 거리가 k로 도달 불가능한 경우
    if (k - (abs(x-r) + abs(y-c)))%2 or (abs(x-r) + abs(y-c)) > k :
        return "impossible"
    
    # 알파벳 순서
    down, left, right, up = 0, 0, 0, 0
    
    # 가야하는 d, l, r, u 최소 개수 저장
    if r >= x :
        down = r-x
    else :
        up = x-r
    if c >= y :
        right = c-y
    else :
        left = y-c
        
    # 남은 이동 거리
    dist = k - (abs(r-x) + abs(c-y))
    
    # d를 최대한 이동
    answer += 'd'*down
    down = min(dist//2, n-(x+down))
    answer += 'd'*down
    up += down
    dist -= 2*down
    
    # l을 최대한 이동
    answer += 'l'*left
    left = min(dist//2, y-left-1)
    answer += 'l'*left
    right += left
    dist -= 2*left
    
    # 남은거리는 l, r로 채워야 한다. u->d를 넣으면 사전 순서에서 밀린다.
    answer += 'rl'*(dist//2)
    answer += 'r'*right
    answer += 'u'*up
    
    return answer