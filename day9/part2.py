with open("data.txt") as file:
    lines = [line.rstrip() for line in file]

grid = []
for i in range(0, 6):
    row = []
    for j in range(0, 6):
        row.append(".")
    grid.append(row)

rope = []

for i in range(10):
    rope.append([0, 0])

def markGrid(rope, grid):
    for i in range(len(rope)-1, -1, -1):
        grid[rope[i][1]][rope[i][0]] = i



visited = {}

def moveUp(knot):
    knot[1] -= 1

def moveDown(knot):
    knot[1] += 1

def moveLeft(knot):
    knot[0] -= 1

def moveRight(knot):
    knot[0] += 1

def diagonalCheck(head, tail):
    if abs(head[0] - tail[0]) >= 1 and abs(head[1] - tail[1]) >= 1:
        return True
    return False

def move(head, tail):
    if head[0] - tail[0] > 1 and head[1] - tail[1] > 1:
        tail[0] += 1
        tail[1] += 1
    if head[0] - tail[0] > 1 and tail[1] - head[1] > 1:
        tail[0] += 1
        tail[1] -= 1
    if tail[0] - head[0] > 1 and head[1] - tail[1] > 1:
        tail[0] -= 1
        tail[1] += 1
    if tail[0] - head[0] > 1 and tail[1] - head[1] > 1:
        tail[0] -= 1
        tail[1] -= 1
    if head[0] - tail[0] > 1:
        tail[0] += 1
        tail[1] = head[1]
    if tail[0] - head[0] > 1:
        tail[0] -= 1
        tail[1] = head[1]
    if head[1] - tail[1] > 1:
        tail[1] += 1
        tail[0] = head[0]
    if tail[1] - head[1] > 1:
        tail[1] -= 1
        tail[0] = head[0]

def moveRope(rope):
    for i in range(1, len(rope)):
        move(rope[i-1], rope[i])


for line in lines:
    movement = int(line[2:])
    for step in range(movement):
        if line[0] == "R":
            moveRight(rope[0])
        if line[0] == "L":
            moveLeft(rope[0])
        if line[0] == "U":
            moveUp(rope[0])
        if line[0] == "D":
            moveDown(rope[0])
        moveRope(rope)
        visited[f"{rope[9][0]},{rope[9][1]}"] = True

print(len(visited))