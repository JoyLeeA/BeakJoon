# 1: 동 2: 서 3:남 4:북
K = int(input())
directions = []
lengths = []
for _ in range(6):
    direction, length = map(int,input().split())
    directions.append(direction)
    lengths.append(length)

max_lengths = []
box_lengths = []
for i in range(1, 5):
    if directions.count(i) == 1:
        max_lengths.append(lengths[directions.index(i)])

        temp = directions.index(i) + 3 
        if temp >= 6:
            temp -= 6
        box_lengths.append(lengths[temp]) 

print(K * ((max_lengths[0] * max_lengths[1]) - (box_lengths[0] * box_lengths[1])))
