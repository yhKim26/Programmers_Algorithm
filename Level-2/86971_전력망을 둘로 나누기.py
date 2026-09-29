def bfs(start, n, wires):
    
    #송전탑의 연결상태를 나타내는 그래프
    graph = {i:[] for i in range(n+1)}
        #graph = 1:[] 2:[] ...
        
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        #1번 송전탑과 연결된 정보 1:[], 2번 송전탑과 연결된 정보 2:[]...
    
    #방문처리    
    visited = [False] * (n+1)
    visited[start] = True
    
    #연결갯수확인을 위해 시작
    queue = [start]
    count1 = 1
    
    #시작한 송전탑과 묶여있는 송전탑들 갯수 확인
    while queue:
        node = queue.pop(0)
        for wire in graph[node]:
            if not visited[wire]:
                visited[wire] = True
                queue.append(wire)
                count1 += 1
                
    #전체값에서 한 묶음의 송전탑들 갯수 빼기            
    count2 = n - count1
    result = abs(count2-count1)
    return result

def solution(n, wires):
    answer = -1
    best = n
    
    #연결된 전선 하나씩 제거
    for wires_num in range(len(wires)):
        removed = wires.pop(wires_num)
        
        #제거시 가장 비슷하게 나눠지는 경우 탐색
        best = min(best, bfs(1, n, wires))
        wires.insert(wires_num, removed)
        
    answer = best
    return answer



#시행착오
#처음에는 송전탑을 기준으로 판단
#것보다 전선을 기준으로 판단하는 것이 더 좋아보임
#전선을 하나씩 잘라보며 나뉘어지는 송전탑의 갯수를 비교
#비교 후 차이값(절댓값기준)이 가장 낮은 값 반환

