# 도서관

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
books = list(map(int, input().rstrip().split()))

# 음수와 양수를 분할
minus, plus = [], []
for book in books :
    if book < 0 :
        minus.append(-book)
    elif book > 0 :
        plus.append(book)
    # 0인 경우는 옮길 필요가 없기 때문에 바로 제거

minus.sort(reverse = True)
plus.sort(reverse = True)

# 이동해야 하는 거리를 저장하는 list
# list로 만드는 이유는 가장 멀리 이동해야 하는 경우를 1번만 더하기 위해서
# 다른 경우에는 책을 가지러 다시 0의 위치로 와야 한다.
distance = []

# m권씩 묶어서 다닌다.
for i in range(len(minus)//m) :
    distance.append( minus[m*i])
for j in range(len(plus)//m) :
    distance.append(plus[m*j])
# 남은 책이 있다면
if len(minus) % m :
    distance.append(minus[(len(minus)//m)*m])
if len(plus) % m :
    distance.append(plus[(len(plus)//m)*m])

distance.sort()
answer = distance.pop()
for dis in distance :
    answer += 2*dis

print(answer)