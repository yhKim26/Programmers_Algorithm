from itertools import permutations

# 소수 판별 함수
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:     
        if n % i == 0:
            return False
        i += 1
    return True



def solution(numbers):
    answer = 0
    answer_lst = []

    # 먼저 문자열 분해
    nums = list(numbers)
    
    # 분해된 숫자들을 합치기
    for length in range(1, len(nums)+1):
        for number in permutations(nums, length):
            num = int(''.join(number))
            
            # 소수 판별
            if is_prime(num):
                # 중복 확인
                for i in range(len(answer_lst)):
                    if answer_lst[i] == num:
                        break
                else:
                    answer += 1
                    answer_lst.append(num)
    
    return answer