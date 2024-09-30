import heapq


def init(N):
    global free, file
    # 빈구간
    free = [(0, N-1)]
    # file 별로 할당된 구간 관리 {mId : []}
    file = dict()
    return


def add(mId, mSize):
    # mId가 할당된 구간 list
    lst = []
    remember = -1

    while mSize > 0 and free :
        start, end = heapq.heappop(free)
        available = end - start + 1

        if remember == -1 :
            remember = start + 1

        if available >= mSize :
            # 필요한 구간을 할당
            lst.append((start, start + mSize - 1))

            # 남은 구간 처리
            if available > mSize :
                heapq.heappush(free, (start + mSize, end))

            mSize = 0
            break
        else :
            # 할당 가능한 부분만 할당
            lst.append((start, end))
            mSize -= available

    if mSize > 0 :
        for block in lst :
            heapq.heappush(free, block)
        return -1

    file[mId] = lst
    return remember


def remove(mId):
    segments = file[mId]
    del file[mId]

    # 빈 공간을 리스트에 추가
    for segment in segments :
        heapq.heappush(free, segment)

    # free에 (0, 1), (2, 3)처럼 같이 있다면 (0, 3)로 병합
    merge = []
    while free :
        start, end = heapq.heappop(free)
        if merge and merge[-1][1] + 1 == start :
            merge[-1] = (merge[-1][0], end)
        else :
            merge.append((start, end))
    for block in merge :
        heapq.heappush(free, block)

    return len(segments)


def count(mStart, mEnd):
    unique = set()
    for mId, segments in file.items():
        for start, end in segments:
            if start <= mEnd - 1 and end >= mStart - 1:
                unique.add(mId)
                break
    return len(unique)