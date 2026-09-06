
def solution(progresses, speeds):
    answer = []
    
    #남은 작업 확인
    while progresses:
        count = 0
        
        #각 속도별로 진도 상승
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]
        
        
        #진도 100이상일 시 배포
        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            
            #하루 배포 수
            count += 1
            
            #전체 작업 완료시
            if not progresses:
                break
        
        #배포한 작업 있을 시
        if count != 0:
            answer.append(count)
        
    return answer

# 진도 100%일 때 서비스에 반영
# 개발속도 모두 다름
# 뒤에 있는 기능 먼저 개발 완료 시
# 앞 기능 배포할 때 같이 배포
# 기능 순서대로 작업 진도가 적힌 정수 배열 progresses
# 작업 개발 속도 speed
# 배포 별 몇 개의 기능 배포되는지 return
# 배포는 하루에 1번