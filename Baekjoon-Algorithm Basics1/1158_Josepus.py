N, M = map(int, input().split())
cursor = 0
answer_list = []
circle = list(range(1,N+1))
for i in range(N):
    cursor = (cursor + M - 1) % len(circle)
    pop = circle.pop(cursor)
    answer_list.append(str(pop))

    
    
print(f"<{', '.join(answer_list)}>")