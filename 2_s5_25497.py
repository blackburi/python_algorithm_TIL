# 기술 연계마스터 임스

import sys
input = sys.stdin.readline

n = int(input())
skills = list(input().rstrip())

dic = {
    'R' : 0,
    'K' : 0,
}

# 사용한 스킬 수
answer = 0

while skills :
    skill = skills.pop()
    if skill not in ['L', 'R', 'S', 'K'] :
        answer += 1
    elif skill == 'R' :
        dic['R'] += 1
    elif skill == 'K' :
        dic['K'] += 1
    elif skill == 'L' and dic['R'] :
        dic['R'] -= 1
        answer += 1
    elif skill == 'S' and dic['K'] :
        dic['K'] -= 1
        answer += 1
    else :
        dic['R'] = 0
        dic['K'] = 0

print(answer)