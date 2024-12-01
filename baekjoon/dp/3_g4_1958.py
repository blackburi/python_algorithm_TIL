# LCS 3

import sys
input = sys.stdin.readline

word1 = input().rstrip()
word2 = input().rstrip()
word3 = input().rstrip()

a, b, c = len(word1), len(word2), len(word3)

# 공통 부분을 저장하는 3차원 matrix
lcs = [[[0]*(c+1) for _ in range(b+1)] for _ in range(a+1)]

for i in range(1, a+1) :
    for j in range(1, b+1) :
        for k in range(1, c+1) :
            # lcs에 해당하는 공통 부분이 있다면
            if word1[i-1] == word2[j-1] and word2[j-1] == word3[k-1] :
                lcs[i][j][k] = lcs[i-1][j-1][k-1] + 1
            # 공통부분이 존재하지 않는다면
            else :
                lcs[i][j][k] = max(lcs[i][j][k-1], lcs[i][j-1][k], lcs[i-1][j][k])

# 공통 부분 문자수열 길이 초기화
answer = -1

# 공통된 부분의 길이를 갱신
for i in range(a+1) :
    for j in range(b+1) :
        answer = max(max(lcs[i][j]), answer)

print(answer)