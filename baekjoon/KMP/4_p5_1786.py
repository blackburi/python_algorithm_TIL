# 찾기

import sys
input = sys.stdin.readline


text = input().rstrip()
pattern = input().rstrip()

n = len(text)
m = len(pattern)

table = [0]*m
idx = 0

# pattern 내 동일한 부분을 찾아 table에 기록
for i in range(1, m) :
    while idx > 0 and pattern[i] != pattern[idx] :
        idx = table[idx-1]
    if pattern[i] == pattern[idx] :
        idx += 1
        table[i] = idx

# 초기 설정
idx = 0
cnt = 0 # 총 개수
location = [] # pattern이 나오는 위치

# text에서 pattern 찾기
for i in range(n) :
    while idx > 0 and text[i] != pattern[idx] :
        idx = table[idx-1]

    if text[i] == pattern[idx] :
        if idx == m-1 :
            cnt += 1
            location.append(i-m+2)
            idx = table[idx]
        else :
            idx += 1

print(cnt)
print(*location)

