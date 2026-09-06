def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True




def solution(s):
    # 1. ( 는 무조건 스택에 집어 넣는다.
    # 2. ) 이면 스택에서 (를 빼줘라.
    # 3. 다 끝났는데 스택에 (가 남았으면 모자른거니까 잘못된거다.
    stk = []
    for word in s:
        if word == "(": 
            stk.append(word)
        else:
            # )
            if not stk:
                return False
            else:
                stk.pop()
    if stk:
        return False
    return True