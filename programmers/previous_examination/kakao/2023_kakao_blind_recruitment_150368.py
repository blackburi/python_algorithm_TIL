# 이모티콘 할인 행사

def solution(users, emoticons):
    answer = [0, 0]
    sales = [10, 20, 30, 40]
    # 할인 조합
    discounts = []

    # 이모티콘 할인율 구하기
    def dfs(lst, depth):
        if depth == len(lst) :
            discounts.append(lst[:])
            return

        for sale in sales:
            lst[depth] += sale
            dfs(lst, depth + 1)
            lst[depth] -= sale

    dfs([0] * len(emoticons), 0)

    for d in range(len(discounts)):
        # 가입자 수
        join_user = 0
        # 이익
        profit = 0

        for user in users:
            # 사용자의 총 구매 가격
            buy_emoticons = 0
            for i in range(len(emoticons)):
                if discounts[d][i] >= user[0]:
                    buy_emoticons += emoticons[i] * ((100 - discounts[d][i]) / 100)
            # 구매가격이 일정금액을 넘은 경우 -> 가입
            if user[1] <= buy_emoticons:
                join_user += 1
            # 구매가격이 일정금액을 넘지 못한 경우 -> 이익
            else:
                profit += buy_emoticons
        
        # 가입자 수 갱신
        if answer[0] < join_user :
            answer = [join_user, int(profit)]
        # 가입자 수는 동일, 이익 갱신
        elif answer[0] == join_user and answer[1] < profit :
            answer = [join_user, int(profit)]
        # 가입자 수가 적거나, 가입자 수가 동일하지만 이익이 적은 경우는 생각할 필요 없다.

    return answer