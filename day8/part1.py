with open("data.txt") as file:
    lines = [line.rstrip() for line in file]

counter = (len(lines) * 2) + (len(lines[0]) * 2) - 4

for i in range(1, len(lines)-1):
    for j in range(1, len(lines[0])-1):
        xCheck = j
        yCheck = i
        tree = lines[i][j]
        visible = False
        while xCheck > 0:
            xCheck -= 1
            if lines[yCheck][xCheck] >= tree:
                break
            if xCheck == 0:
                visible = True
        xCheck = j
        while xCheck < len(lines[0])-1:
            xCheck += 1
            if lines[yCheck][xCheck] >= tree:
                break
            if xCheck + 1 == len(lines[0]):
                visible = True
        xCheck = j
        while yCheck > 0:
            yCheck -= 1
            if lines[yCheck][xCheck] >= tree:
                break
            if yCheck == 0:
                visible = True
        yCheck = i
        while yCheck < len(lines)-1:
            yCheck += 1
            if lines[yCheck][xCheck] >= tree:
                break
            if yCheck + 1 == len(lines):
                visible = True
        if visible == True:
            counter += 1

print(counter)





