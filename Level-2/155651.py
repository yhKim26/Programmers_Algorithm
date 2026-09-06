def add_clean_time(time):
    h, m = map(int, time.split(':'))
    total = h * 60 + m 
    
    return total



def solution(book_time):
    answer = 0

    book_time.sort()
    
    s = []
    e = []
    for s_t, e_t in book_time:
        s.append(add_clean_time(s_t))
        e.append(add_clean_time(e_t) + 10)

    s.sort()
    e.sort()   

    n = len(s)
    start = 0
    end = 0
    room = 0

    while start < n:
        if e[end] > s[start]:
            room += 1
            answer = max(answer, room)
            start += 1
        else:
            room -= 1
            end += 1

    return answer

