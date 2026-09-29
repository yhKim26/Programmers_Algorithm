
        

def solution(sequence, k):
    answer = []
                           
    left = 0
    total = 0
    best = len(sequence)+1
    best_left = 0
    best_right = 0
    for right in range(len(sequence)):
        total += sequence[right]
        while total > k:
            total -= sequence[left]
            left += 1
        if total == k:
            if best > right - left +1:
                best = right - left + 1
                best_left = left
                best_right = right
        
    answer.append(best_left)
    answer.append(best_right)
    
    return answer
    

# sequence = 비내림차순의 정수 배열
# k = 임의의 두 인덱스 포함 사이의 원소들의 합
# 경우의 수가 여러개인 경우 짧은 수열 찾기
# 또한 길이가 똑같은 경우 시작 인덱스가 작은 수열
