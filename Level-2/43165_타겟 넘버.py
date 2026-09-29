
        
    

def solution(numbers, target):
    answer = 0
    total = 0
    n = len(numbers)
    # 처음 number[0]도 경우의 수로 넣기 위해 앞에 0추가
    numbers.insert(0,0)
    
    def dfs(index, total):
        nonlocal answer

        #종료 조건
        if index == n:
            if total == target:
                answer += 1
            return
        
        index += 1
        #더하는 경우
        dfs(index, total+numbers[index])
        #빼는 경우
        dfs(index, total-numbers[index])
    
    dfs(0,0)
    return answer