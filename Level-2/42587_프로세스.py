# priorities = 프로세스 중요도 배열

def solution(priorities, location):
    answer = 0
    count = 0
    queue = []
    
    
    # 프로세스별 시작 위치 체크
    for i in range(len(priorities)):
        queue.append((priorities[i], i))

    # 대기 큐에서 꺼내기
    while queue:
        work = queue.pop(0)
        priorities.pop(0)
        
        # 꺼낸 프로세스보다 대기 큐에 높은 중요도 프로세스가 있을 시
        for j in range(len(priorities)):
            if work[0] < priorities[j]:
                queue.append(work)                
                priorities.append(work[0])
                break
                              
        # 없다면        
        else:
            count += 1
            
            # 실행된 프로세스가 알고싶은 프로세스인지
            if work[1] == location:
                answer = count
                break
            
    return answer
   
    

# 처음 location의 위치 및 값 저장
# 앞에서부터 조회
# 조회한 숫자가 뒤에 있는 것보다 중요도 낮은 경우 맨 뒤에 다시 넣기
