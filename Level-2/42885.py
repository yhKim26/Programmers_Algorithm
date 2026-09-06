def solution(people, limit):
    people.sort()
    lo, hi = 0, len(people)-1

    answer = 0
    boat = 0 
    total = 0
    
    while lo <= hi:
        if lo == hi:
            boat +=1 
            break
        total = people[lo] + people[hi]
        if total <= limit:
            boat += 1
            lo += 1
            hi -= 1
        if total > limit:
            boat += 1
            hi -= 1
    answer = boat
        
    return answer


# firts 합쳤을 때 == limit인 경우
# second limit에 가장 근접한 경우
# thrid 나머지

