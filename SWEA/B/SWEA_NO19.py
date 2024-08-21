# 단어가 등장하는 횟수


# 부분 일치 테이블(LPS)를 계산하는 함수
def kmp_lps(word) :
    lps = [0] * len(word)
    length = 0 # 이전 lps 길이
    i = 1

    while i < len(word) :
        if word[i] == word[length] :
            length += 1
            lps[i] = length
            i += 1
        else : # word[i] != word[length]
            if length != 0 :
                length = lps[length - 1]
            else : # length == 0
                lps[i] = 0
                i += 1

    return lps


# 책 내에서 단어를 찾는 KMP 알고리즘
def kmp(book, word) :
    global ans

    lps = kmp_lps(word)
    # book index
    i = 0
    # word index
    j = 0

    while i < len(book) :
        if word[j] == book[i] :
            i += 1
            j += 1

        if j == len(word) :
            ans += 1
            j = lps[j - 1]
        elif i < len(book) and word[j] != book[i] :
            if j == 0 :
                i += 1
            else : # j != 0
                j = lps[j-1]


T = int(input())
for tc in range(1, T+1) :
    book = list(map(str, input()))
    word = list(map(str, input()))

    # 단어의 수를 세는 변수
    ans = 0

    kmp(book, word)

    print(f'#{tc} {ans}')