# 센서

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensors = list(map(int, input().rstrip().split()))
sensors.sort()

"""
sensors가 [1, 5, 10]에 있다고 가정하고 이때 집중국 1개를 위치 시킨다고 가정하자.
만약 집중국을 4에 위치 시킨다고 가정하면 수신 가능 영역의 합은 3+1+6=10이 된다.
집중국을 3에 위치 시킨다고 가정하면 수신 가능 영역의 합은 2+2+7=11이 된다.
집중국을 5에 위치시킨다고 가정하면 수신 가능 영역의 합은 4+5=9가 된다.
즉 집중국은 sensor와 겹치게 두는것이 좋다.

sensors가 [1, 5, 10, 16]이고 2개의 집중국을 위치 시킨다고 가정하자.
sensor 사이의 거리는 [4, 5, 6]이 된다. 집중국을 5, 16에 두면 되는데
이때 수신 가능 영역의 합은 4+5=9가 된다.
즉 sensors 사이의 거리를 확인하고 0 ~ (n-k-1)까지 더하면 된다.
-> 거리의 값이 큰 순서대로 차래대로 제외시키면 된다.
"""

distance = []
for i in range(n-1) :
    distance.append(sensors[i+1]-sensors[i])

distance.sort()
print(sum(distance[:n-k]))