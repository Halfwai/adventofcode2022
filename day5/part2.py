import re

with open("data.txt") as file:
    lines = [line.rstrip() for line in file]

boxes = [[] for _ in range (9)]

for line in lines:
    for i in range(1, 37, 4):
        if line[i] != " ":
            boxes[i // 4].append(line[i])

with open("data2.txt") as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    move = re.findall(r'\d+', line)
    for i in range(int(move[0])):
        boxes[int(move[2])-1].insert(0, boxes[int(move[1])-1].pop(int(move[0])-1-i))

for box in boxes:
    print(box[0], end ="")