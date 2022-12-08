with open("data.txt") as file:
    lines = [line.rstrip() for line in file]

total = 0

def viewCheck(j, i, total):
    xCheck = j
    yCheck = i
    tree = lines[i][j]
    counter = 0
    while xCheck > 0:
        xCheck -= 1
        if lines[yCheck][xCheck] >= tree:
            counter = j - xCheck
            break
        if xCheck == 0:
            counter = j
    xCheck = j
    while xCheck < len(lines[0])-1:
        xCheck += 1
        if lines[yCheck][xCheck] >= tree:
            counter *= (xCheck - j)
            break
        if xCheck + 1 == len(lines[0]):
            counter *= ((xCheck) - j)
    xCheck = j
    while yCheck > 0:
        yCheck -= 1
        if lines[yCheck][xCheck] >= tree:
            counter *= i - yCheck
            break
        if yCheck == 0:
            counter *= i
    yCheck = i
    while yCheck < len(lines)-1:
        yCheck += 1
        if lines[yCheck][xCheck] >= tree:
            counter *= (yCheck - i)
            break
        if yCheck + 1 == len(lines):
            counter *= ((yCheck) - i)
    if counter > total:
        total = counter
    return total

for i in range(1, len(lines)-1):
    for j in range(1, len(lines[0])-1):
        total = viewCheck(j, i, total)

# total = viewCheck(2, 3, total)
        

print(total)