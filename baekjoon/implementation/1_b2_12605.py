# 단어순서 뒤집기

import sys
input = sys.stdin.readline

TC = int(input())
for tc in range(1, TC+1) :
    words = list(input().rstrip().split())
    words = words[::-1]
    print(f'Case #{tc}:', ' '.join(words))