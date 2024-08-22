# 구간합


# 1~num 까지 모든 숫자의 각 자리를 합하는 함수
def hap(num) :
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9의 개수
    number = [0] * 10

    # 자릿수에 따라 갯수는 10의 거듭제곱만큼 많아진다
    # 5 : 일의 자리에 5가 1개
    # 5_ : 십의 자리에 5가 10개 (50~59)
    # 5__ : 백의 자리에 5가 100개 (500~599)
    # 자리수를 세는 변수
    digit = 1

    # 1페이지 부터 세기 시작
    start = 1

    # 0으로 끝나는 수와 9로 끝나는 수를 짝지어 주면 세기 편하다.
    # 1157의 경우 1140~1149까지 세고, 1150~1157을 따로 센다.
    def plus(x, digit) :
        while x > 0 :
            number[x % 10] += digit
            x //= 10

    while start <= num :
        # 마지막 페이지가 9로 끝나지 않는 경우
        while num % 10 != 9 :
            plus(num, digit)
            num -= 1

        # 세야 하는 start가 넘어가면 stop
        if num < start :
            break


        # 세기 시작하는 start가 0으로 시작하지 않는 경우
        while start % 10 != 0 :
            plus(start, digit)
            start += 1

        start //= 10
        num //= 10
        for i in range(10) :
            number[i] += (num - start + 1) * digit
        digit *= 10

    # 모든 수를 더하는 변수
    total = 0
    for i in range(10) :
        total += i * number[i]

    return total


T = int(input())
for tc in range(1, T+1) :
    a, b = map(int, input().split())

    if a == 0 :
        print(f'#{tc}', hap(b)-hap(a))
    else : # a != 0
        print(f'#{tc}', hap(b)-hap(a-1))