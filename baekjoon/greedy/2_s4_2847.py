# 게임을 만든 동준이

import sys
input = sys.stdin.readline

n = int(input())
score = [int(input()) for _ in range(n)]
# 큰 점수부터 확인하기 위해 reverse
score = score[::-1]

answer = 0

for i in range(n-1) :
    if score[i] <= score[i+1] :
        answer += score[i+1] - (score[i]-1)
        score[i+1] = score[i]-1

print(answer)