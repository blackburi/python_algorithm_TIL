# 밤양갱

import sys
input = sys.stdin.readline

# daldidalgo : d, a, l, d, i, dal, g, o -> 8초
# 이후 daldidalgo : 1초
# daldidan : daldida, n -> 2초

n = int(input())

# 처음 입력하는 daldidalgo 8초
answer = 8

# 두번째부터 입력하는 daldidalgo는 복사를 할 수 있다.
i = 1

while True :
    if n == 2**i :
        # 2배씩 복사하고 마지막 daldidan 2초
        answer += i+2
        break
    elif n < 2**i :
        # 2배씩 복사하는 위의 경우보다 1번 적게 하면 갈 수 있다.
        answer += (i-1) + 2
        break
    
    # 위 두가지의 경우에 모두 해당되지 않는 다면
    i += 1

print(answer)