
def solution(p):
    if p == '':
        answer = ''
        return answer
    idx = split_uv(p)
    u = p[:idx+1]
    v = p[idx+1:]
    blank = '('
    if check_vaiid(u):
        blank = u
        v_valid = solution(v)
        answer = blank + v_valid
    else:
        v_valid = solution(v)
        blank += v_valid
        blank += ')'
        for i in u[1:-1]:
            if i == '(':
                blank += ')'
            elif i == ')':
                blank += '('
        answer = blank
    return answer



def check_vaiid(p):
    left = 0
    right = 0
    for i in p:
        if i == '(':
            left += 1
        elif i == ')':
            right += 1
        if left < right:
            return False
    return True





def split_uv(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count +=1
        else:
            count -= 1
        if count == 0:
            return i
