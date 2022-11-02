import sys
N = int(sys.stdin.readline())
idx_cnt = 1
stack = []
sign_list = []
answer = True
for i in range(N):
    input_value= int(sys.stdin.readline())
    while idx_cnt <= input_value:
        stack.append(idx_cnt)
        sign_list.append('+')
        idx_cnt +=1
    if stack[-1] == input_value:
        stack.pop()
        sign_list.append('-')
    else:
        answer = False  
if answer:
    for i in sign_list:
        print(i)
else:
    print('NO')