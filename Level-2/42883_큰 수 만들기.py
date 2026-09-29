def solution(number, k):
    
    
    # 임의의 k개 수 제거
    # 제거 후 비교 및 큰 수 남기기

    result = []



    
    for num in number:
        while result and k > 0 and result[-1] < num:
            result.pop(-1)
            k -= 1
        result.append(num)
    
    if k > 0:
        result = result[:-k]
    
    return ''.join(result)