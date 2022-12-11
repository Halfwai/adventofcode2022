with open("data.txt") as file:
    lines = [line.rstrip() for line in file]

cycle = 1

X = 1

total = 0

def checkCycle(cycle, total):
    if cycle == 20:
        total += 20 * X
    if cycle == 60:
        total += 60 * X
    if cycle == 100:
        total += 100 * X
    if cycle == 140:
        total += 140 * X
    if cycle == 180:
        total += 180 * X
    if cycle == 220:
        total += 220 * X
    return total


for i in range(0, len(lines)):
    if lines[i][:4] != "noop":
        cycle += 1
        total = checkCycle(cycle, total)
        X += int(lines[i][5:])
        cycle += 1
    else:
        cycle += 1
    print(cycle, X)

    total = checkCycle(cycle, total)

print(total)
