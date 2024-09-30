def init(N:int, M:int, mType:list, mTime:list) -> None:
    global n, type, time

    # 개수
    n = N
    # 도로의 type, 길이 : N-1 (M가지 종류 0 ~ M-1)
    type = mType
    # 각 구간의 현재 통과 예상 시간, 길이 : N-1
    time = mTime
    return

def destroy() -> None:
    return

def update(mID:int, mNewTime:int) -> None:
    time[mID] = mNewTime
    return

def updateByType(mTypeID:int, mRatio256:int) -> int:
    total = 0
    for i in range(n-1) :
        if type[i] == mTypeID :
            time[i] = (time[i] * mRatio256) // 256
            total += time[i]
    return total

def calculate(mA:int, mB:int)-> int:
    mA, mB = min(mA, mB), max(mA, mB)
    return sum(time[mA:mB])