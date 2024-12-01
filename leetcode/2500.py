# 2500. Delete Greatest Value in Each Row

class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        k = len(grid[0])

        # 오름차순으로 정렬
        for lst in grid :
            lst.sort()
        
        answer = 0

        while k :
            # 각 행에서 최대 정수를 넣어두는 list
            tmp = []
            for lst in grid :
                tmp.append(lst.pop())

            answer += max(tmp)
            k -= 1

        return answer