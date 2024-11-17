# 센서

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensors = list(map(int, input().rstrip().split())).sort()
print(sensors)
# 집중국의 수가 센서의 수보다 많은 경우
if k >= n :
    print(0)
    sys.exit()

dist = []
for i in range(1, n) :
    # 센서 사이의 거리를 계산
    dist.append(sensors[i] - sensors[i-1])

# 센서 사이의 거리를 큰 순서대로 정렬
dist.sort()
for _ in range(k) :
    # 제일 큰 값부터 제거해 나간다.
    dist.pop()

# 제거되지 않은 값을 모두 더하면 최소 길이 합이 된다.
print(sum(dist))