def solution(nums):
    answer = 0
    tot = len(nums) / 2
    type = len(set(nums))
    if type >= tot:
        return tot
    else:
        return type


