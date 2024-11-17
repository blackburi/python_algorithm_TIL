# 기술 연계마스터 임스

import sys
input = sys.stdin.readline
from collections import deque


n = int(input())
skills = deque(list(input().rstrip()))

# 총 사용한 스킬 횟수
answer = 0

# 숫자 skill이 아닌 문자 skill을 저장하는 deque
# L -> R, S -> K
l, s = 0, 0

while skills :
    skill = skills.popleft()

    if skill in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] :
        answer += 1
        continue

    if skill == 'L':
        l += 1
    elif skill == 'S' :
        s += 1
    elif skill == 'R' and l :
        l -= 1
        answer += 1
    elif skill == 'K' and s :
        s -= 1
        answer += 1
    else :
        break

print(answer)