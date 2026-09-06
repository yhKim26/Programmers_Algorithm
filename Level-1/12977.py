def solution(nums):
    answer = 0
    size = len(nums)
    for i in range(size - 2):
        for j in range(i+1, size - 1):
            for k in range(j+1, size):
                    total = nums[i] + nums[j] + nums[k]
                    if is_prime(total):
                        answer += 1
    return answer

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
    

