from typing import List
from collections import deque

def init(N:int, mRange:int, mMap:List[List[int]]) -> None:
    # 지도의 크기, 최대 이동 가능 거리, 지도

    global n, move, mat, location

    n = N
    move = mRange
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
    start_x, start_y = location[mFrom]
    end_x, end_y = location[mTo]

    directions = ((0, 1), (1, 0), (-1, 0), (0, -1))

    # (x, y, 이동 가능 거리, 총 이동 거리) 형태로 저장
    q = deque([(start_x, start_y, move, 0)])
    # 방문 체크, 대여소의 경우 2번 방문할 필요가X -> (-1, -1)로 방문 체크
    visited = [[(0, 0) for _ in range(n)] for _ in range(n)]

    visited[start_x][start_y] = (-1, -1)

    while q :
        x, y, l, total = q.popleft()
        
        # 더이상 이동이 불가한 경우
        if l == 0 :
            continue

        for dx, dy in directions :
            # 지도 내에서 이동 가능한 경우
            if 0 <= x+dx < n and 0 <= y+dy < n and mat[x+dx][y+dy] != 1 :
                # 대여소에 도착하는 경우
                if mat[x+dx][y+dy] >= 10 :
                    # 최종 목적지에 도착하는 경우
                    if x+dx == end_x and y+dy == end_y :
                        return total + 1
                    # 최종 목적지가 아닌 대여소에 도달하는 경우
                    # 똑같은 대여소를 2번 방문할 필요 X
                    if visited[x+dx][y+dy] == (-1, -1) :
                        continue
                    # 대여소 방문 처리
                    visited[x+dx][y+dy] = (-1, -1)
                    # q에 추가
                    q.append((x+dx, y+dy, move, total+1))
                # 방문하지 않은 통로에 도착하는 경우
                elif visited[x+dx][y+dy] == (0, 0) :
                    # 방문 처리
                    visited[x+dx][y+dy] = (l-1, total+1)
                    # q에 추가
                    q.append((x+dx, y+dy, l-1, total+1))
                # 방문한 통로에 도착하는 경우
                else :
                    # 이동 가능 거리가 더 먼 경우에만 갱신
                    if l-1 > visited[x+dx][y+dy][0] :
                        # 방문 처리 갱신
                        visited[x+dx][y+dy] = (l-1, total+1)
                        # q에 추가
                        q.append((x+dx, y+dy, l-1, total+1))
    return -1