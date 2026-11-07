def solution(bridge_length, weight, truck_weights):
    # bridge_length : 다리에 올라올 수 있는 트럭 수 = 트럭이 다리를 건너는 시간
    # weight : 다리가 버틸 수 있는 최대 무게
    # truck_weight : 트럭별 무게
    
    #변수명 단축
    bl = bridge_length
    w = weight
    tw = truck_weights[:]
    
    count = 0
    queue = []
    time_queue = []
    
    while tw or queue:
        count += 1
            
        # 다리 위 트럭 남은 시간 감소
        for i in range(len(time_queue)):
            time_queue[i] -= 1
            
        # 다리 건넌 트럭 제거
        while time_queue and time_queue[0] == 0:
            queue.pop(0)
            time_queue.pop(0)
            
        # 새 트럭 태울 수 있으면 태우기
        if tw and sum(queue) + tw[0] <= w:
            queue.append(tw.pop(0))
            time_queue.append(bl)
            
            
    return count



