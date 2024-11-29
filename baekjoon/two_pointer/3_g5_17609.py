# 회문

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n) :
    word = input().rstrip()
    # 좌측과 우측 pointer
    left, right = 0, len(word)-1

    # 회문, 유사회문을 확인하는 변수
    flag = 0

    for _ in range(len(word)) :
        if left >= right :
            break
        if word[left] == word[right] :
            left += 1
            right -= 1
            continue

        # 뒷문자를 제거하여 같은 경우
        if word[left] == word[right-1] :
            # 남은 구간을 체크하도록 새로운 word인 tmp 생성
            tmp = word[left:right]
            # 회문이라면
            if tmp[:] == tmp[::-1] :
                flag = 1
                break
        # 앞문자를 제거하여 같은 경우
        if word[left+1] == word[right] :
            tmp = word[left+1:right+1]
            if tmp[:] == tmp[::-1] :
                flag = 1
                break
        
        flag = 2
        break

    print(flag)