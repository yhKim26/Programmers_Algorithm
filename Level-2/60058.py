def check_right(p):
    count = 0
    for char in p:
        if char == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return True

def split_uv(p):
    open_count = 0
    close_count = 0
    for i in range(len(p)):
        if p[i] == '(':
            open_count += 1
        else:
            close_count += 1
        if open_count == close_count:
            return p[:i+1], p[i+1:]

def solution(p):
    if not p:
        return ""
    
    u, v = split_uv(p)
    
    if check_right(u):
        return u + solution(v)
    else:
        ans = "("
        ans += solution(v)
        ans += ")"
        
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        ans += "".join(u)
        return ans
