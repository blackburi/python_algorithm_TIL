# 폰켓몬

def solution(nums):
    kind = len(nums)//2
    nums = set(nums)
    if len(nums) >= kind :
        answer = kind
    else : # len(nums) < kind
        answer = len(nums)
    return answer