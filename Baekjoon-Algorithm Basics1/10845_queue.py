from sys import stdin
N = int(stdin.readline())
queue = []
answer =[]
for _ in range(N):
    order = list(map(str, input().split()))
    orders = order[0]
    if orders == 'push':
        queue.append(order[1])
    elif orders == 'pop':
        if queue: 
            answer.append(queue[0])
            del queue[0]
        else: 
            answer.append(-1)
    elif orders == 'size':
        answer.append(len(queue))
    elif orders == 'empty':
        if queue: 
            answer.append(0)
        else: 
            answer.append(1)
    elif orders == 'front':
        if queue: 
            answer.append(queue[0])
        else: 
            answer.append(-1)
    elif orders == 'back':
        if queue: 
            answer.append(queue[-1])
        else: 
            answer.append(-1)           
for i in answer:
    print(i)