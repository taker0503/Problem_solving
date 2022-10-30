from sys import stdin

text = list(stdin.readline().strip())
text_2 = []
N = int(stdin.readline())
            
for _ in range(N):
    order = list(stdin.readline().strip())
    orders = order[0]
    if orders == 'P':
        text.append(order[2])
    elif orders == 'L' and text:
        text_2.append(text.pop())
    elif orders == 'D' and text_2:
        text.append(text_2.pop())
    elif orders == 'B' and len(text):
        text.pop()
print(''.join(text+list(reversed(text_2))))