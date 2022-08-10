N = int(input())
house_index = list(map(int,input().split()))

distance = [(0,0)]
for i in range(1, max(house_index)+1):
    difference = 0
    for j in house_index:
        difference += abs(i-j)
    if i == 1:
        distance[0] = (difference,i)
    if distance[0][0] > difference:
        distance[0] = (difference,i)
print(distance[0][1])