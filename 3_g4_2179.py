# 비슷한 단어

import sys
input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]

# 유사도 비교
cnt = 0

ans_word1 = ''
ans_word2 = ''

for i in range(n-1) :
    word1 = words[i]
    for j in range(i+1, n) :
        # 유사도 비교
        tmp = 0
        word2 = words[j]

        if word1 == word2 :
            continue

        for k in range(min(len(word1), len(word2))) :
            if word1[k] == word2[k] :
                tmp += 1
            else :
                break
        if tmp > cnt :
            cnt = tmp
            ans_word1 = words[i]
            ans_word2 = words[j]

print(ans_word1)
print(ans_word2)