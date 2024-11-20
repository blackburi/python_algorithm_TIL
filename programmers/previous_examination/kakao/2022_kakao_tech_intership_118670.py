# 행렬과 연산

from collections import deque

def solution(rc, operations):
    rc = deque(rc)
    # 행, 열
    r, c = len(rc), len(rc[0])
    # column 기준으로 좌측, 우측, 중앙을 나눠서 관리
    # 세로 첫번째 줄
    left_col = deque([rc[i][0] for i in range(r)])
    # 세로 마지막 줄
    right_col = deque([rc[i][c - 1] for i in range(r)])
    # 나머지 중앙 부분
    rows = deque([deque(rc[i][1:c - 1]) for i in range(r)])

    for operation in operations :
        if operation == 'ShiftRow' :
            left_col.appendleft(left_col.pop())
            right_col.appendleft(right_col.pop())
            rows.appendleft(rows.pop())
        else :  # operation == 'Rotate'
            rows[0].appendleft(left_col.popleft())
            right_col.appendleft(rows[0].pop())
            rows[r - 1].append(right_col.pop())
            left_col.append(rows[r - 1].popleft())
            
    # matrix 다시 병합
    answer = []
    for i in range(r):
        answer.append([left_col[i]] + list(rows[i]) + [right_col[i]])
    return answer