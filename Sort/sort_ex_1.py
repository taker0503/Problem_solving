N = int(input())
a_list = []
for _ in range(N):
    name, korean, english, math = input().split()
    a_list.append((name, int(korean), int(english), int(math)))
a_list.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

b= []
for i in a_list:
    b.append(i[0])
print(b)