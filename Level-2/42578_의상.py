def solution(clothes):
    count = {}
    for name, kind in clothes:
        count[kind] = count.get(kind, 0) + 1
    
    answer = 1
    for i in count.values():
        answer = answer * (i + 1)
    answer = answer - 1
    return answer

# 옷의 종류가 몇 개 있는지
# 각각 종류별로 몇 가지의 의상이 있는지
