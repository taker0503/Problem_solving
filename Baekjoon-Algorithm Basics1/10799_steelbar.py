import sys
steel = str(sys.stdin.readline().rstrip())
steel_stack = 0
answer = 0
for i in range(len(steel)):
    if steel[i] == '(':
        steel_stack += 1
    else:
        if steel[i-1] == '(':
            steel_stack -= 1
            answer += steel_stack
        else:
            steel_stack -= 1
            answer += 1
print(answer)