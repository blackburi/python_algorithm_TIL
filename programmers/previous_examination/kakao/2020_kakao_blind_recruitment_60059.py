# 자물쇠와 열쇠

# lock을 3*3 배열로 만들고 key를 돌려가며 맞춰봤을 때
# 중앙 lock을 모두 채울 수 있다면 true, 안된다면 false이다.

# key를 90도 회전하는 함수
def rotate(key) :
    n = len(key)
    turn = [[0]*n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            turn[j][n-i-1] = key[i][j]
    return turn

# lock을 3*3으로 만들었을 때 중앙 lock이 모두 1이 되는지 확인하는 함수
def check(lock) :
    n = len(lock)//3
    for i in range(n, 2*n) :
        for j in range(n, 2*n) :
            if lock[i][j] != 1 :
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    sizeup_lock = [[0]*(3*n) for _ in range(3*n)]
    # 어차피 중앙 lock만 확인하면 되기 때문에 다른 부분은 채울 필요 없다.
    for i in range(n) :
        for j in range(n) :
            sizeup_lock[i+n][j+n] = lock[i][j]
            
    for rotation in range(4) :
        # 90도 회전
        key = rotate(key)
        
        # 마찬가지로 중앙 lock만 확인하면 되기 때문에
        # 중앙 lock과 겹치는 부분만 생각해도 된다.
        for x in range(2*n) :
            for y in range(2*n) :
                for i in range(m) :
                    for j in range(m) :
                        sizeup_lock[i+x][j+y] += key[i][j]
                # 문제 조건을 성립하는 경우
                if check(sizeup_lock) is True :
                    return True
                # 성립하지 않는 경우 -> 원상태로 돌려준다.
                else :
                    for i in range(m) :
                        for j in range(m) :
                            sizeup_lock[i+x][j+y] -= key[i][j]
    return False