# 카드 문자열

import sys
input = sys.stdin.readline
from collections import deque

TC = int(input())
for tc in range(TC) :
    n = int(input())
    letters = deque(list(input().rstrip().split()))

    # 앞에 넣을지 뒤에 넣을지 기준이 되는 letter
    comparison = letters.popleft()
    answer = deque([comparison])

    while letters :
        next = letters.popleft()

        # 아스키코드를 활용하여 사전 순서 비교
        # 아스키코드가 작은 값일 경우
        if ord(next) <= ord(comparison) :
            answer.appendleft(next)
            comparison = next
        # 아스키코드가 큰 값일 경우
        else :
            answer.append(next)
    print(''.join(answer))