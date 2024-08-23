from typing import List
from collections import deque

def init(N:int, mRange:int, mMap:List[List[int]]) -> None:
    # 지도의 크기, 최대 이동 가능 거리, 지도

    global n, length, mat, location

    n = N
    length = mRange
    mat = mMap

    # 충전소의 위치와 번호를 저장 {mID : (x, y)}
    location = dict()
    return

def add(mID:int, mRow:int, mCol:int)-> None:
    # 지도에서 이동 가능한 지점 0과 대여소 0을 구분하기 위함
    mat[mRow][mCol] = mID + 10
    location[mID] = (mRow, mCol)
    return

def distance(mFrom:int, mTo:int)-> int:
    dir = (
        (0, 1),
        (1, 0),
        (-1, 0),
        (0, -1)
    )

    start_x, start_y = location[mFrom]
    end_x, end_y = location[mTo]

    # 방문 체크
    # (이동 가능 거리, 총 이동거리) 형태로 저장
    visited = [[(0, 0) for _ in range(n)] for _ in range(n)]

    # 이동 가능한 곳 (x, y, 이동 가능 거리, 총 이동 거리)를 계산
    q = deque([(start_x, start_y, length, 0)])

    while q :
        x, y, l, total = q.popleft()
        
        # 더이상 이동이 불가능한 경우
        if l == 0 :
            continue

        for dx, dy in dir :
            # 지도 범위 안에 있다면
            if 0 < x+dx < n and 0 < y+dy < n and mat[x+dx][y+dy] != 1 :
                # 전기차 대여소 도착하는 경우
                if mat[x+dx][y+dy] >= 10 :
                    # 목적지에 도착한 경우
                    if x+dx == end_x and y+dy == end_y :
                        return total+1
                    # 같은 대여소를 2번 방문할 필요 없음
                    if visited[x+dx][y+dy] != (0, 0) :
                        continue

                    # 위치를 q에 삽입
                    q.append((x+dx, y+dy, l-1, total+1))
                    # 대여소 방문처리
                    visited[x+dx][y+dy] = (l-1, total+1)
                # 한번도 방문하지 않은곳
                elif visited[x+dx][y+dy] == (0, 0) :
                    visited[x+dx][y+dy] = (l-1, total+1)
                    q.append((x+dx, y+dy, l-1, total+1))
                # 이미 한번 방문 한 곳(이동 가능한 거리가 더 많이 남아야 갱신)
                else :
                    # 기존 방문했을 때보다 이동 가능 거리가 더 멀때만 갱신
                    before_length, _ = visited[x+dx][y+dy]
                    if l-1 > before_length :
                        visited[x+dx][y+dy] = (l-1, total+1)
                        q.append((x+dx, y+dy, l-1, total+1))
    return -1