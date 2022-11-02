import sys
_ = int(sys.stdin.readline())
stack = []

for _ in range(_):
    string = list(map(str,sys.stdin.readline().split()))
    if string[0] == 'push':
        stack.append(string[1])
    elif string[0] == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif string[0] == 'size':
        print(len(stack))
    elif string[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif string[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

