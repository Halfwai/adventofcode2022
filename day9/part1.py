with open("data.txt") as file:
    lines = [line.rstrip() for line in file]

head = {
    "y": 4,
    "x": 0,
}

tail = {
    "y": 4,
    "x": 0,
}

visited = {}

def diagonalCheck(head, tail):
    if abs(head["x"] - tail["x"]) == 1 and abs(head["y"] - tail["y"]) == 1:
        return True
    return False

def distCheck(head, tail):
    if head["x"] - tail["x"] > 1:
        tail["x"] += 1
        check = diagonalCheck(head, tail)
        if check == True:
            tail["y"] = head["y"]
    elif tail["x"] - head["x"] > 1:
        tail["x"] -= 1
        check = diagonalCheck(head, tail)
        if check == True:
            tail["y"] = head["y"]
    elif head["y"] - tail["y"] > 1:
        tail["y"] += 1
        check = diagonalCheck(head, tail)
        if check == True:
            tail["x"] = head["x"]
    elif tail["y"] - head["y"] > 1:
        tail["y"] -= 1
        check = diagonalCheck(head, tail)
        if check == True:
            tail["x"] = head["x"]
    else:
        return

for line in lines:
    movement = int(line[2:])
    for step in range(movement):
        if line[0] == "R":
            head["x"] += 1
            distCheck(head, tail)
        if line[0] == "L":
            head["x"] -= 1
            distCheck(head, tail)
        if line[0] == "U":
            head["y"] -= 1
            distCheck(head, tail)
        if line[0] == "D":
            head["y"] += 1
            distCheck(head, tail)
        visited[f"{tail['x']},{tail['y']}"] = True

print(len(visited))