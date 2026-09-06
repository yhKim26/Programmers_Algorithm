def solution(phone_book):
    answer = True
    
    phone_book.sort()

# 앞 번호가 뒷 번호의 일치하는 부분이 있는 지 체크
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            
            answer = False
            return answer
        
        
        # 일치할 시 True
        else:
            answer = True
    return answer
        
    