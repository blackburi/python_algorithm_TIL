# 2558. Take Gifts From the Richest Pile

import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort()

        while k :
            # 제일 큰 선물
            gift = gifts.pop()
            # 제곱근을 취하고 정수로 만든다.
            gifts.append(int(math.sqrt(gift)))
            # 다시 정렬
            gifts.sort()

            k -= 1

        return sum(gifts)