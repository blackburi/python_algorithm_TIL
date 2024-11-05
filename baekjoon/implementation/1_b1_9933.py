# 민균이의 비밀번호

import sys
input = sys.stdin.readline

n = int(input())
# 단어list
words = []
# 비밀번호
password = ''
for _ in range(n) :
    word = input().rstrip()
    words.append(word)
    for i in range(len(word)//2) :
        if word[i] != word[len(word)-i-1] :
            break
    else :
        password = word
else :
    for word in words :
        new = word[::-1]
        if new in words :
            password = word
            break

print(len(password), password[len(password)//2])