def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for a, b in zip(participant, completion):
        if a != b:
            return a
    return participant[-1]  


# participant - 마라톤에 참여한 선수들의 이름
# completion - 완주한 선수들의 이름
# 완주하지 못한 선수의 이름 찾기