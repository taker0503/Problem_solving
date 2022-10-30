import sys
N = int(sys.stdin.readline())
deque = []
for _ in range(N):
    order = list(map(str, sys.stdin.readline().split()))
    first = order[0]
    if first == 'push_front':
        deque.insert(0,order[1])
    elif first == 'push_back':
        deque.append(order[1])
    elif first == 'pop_front':
        if deque:
            print(deque[0])
            del deque[0]
        else:
            print(-1)
    elif first == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif first == 'size':
        print(len(deque))
    elif first == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif first == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif first == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)
    
        