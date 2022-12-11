with open("data.txt") as file:
    lines = [line.rstrip() for line in file]

cycle = 0

X = 1

message = []

def lineCheck(line, X, cycle):
    if abs(X - cycle) <= 1:
        line = f"{line}#"
    else:
        line = f"{line}."
    return line

def checkCycle(cycle, line, message):
    if cycle == 40:
        message.append(line)
        line = ""
    if cycle == 80:
        message.append(line)
        line = ""
    if cycle == 120:
        message.append(line)
        line = ""
    if cycle == 160:
        message.append(line)
        line = ""
    if cycle == 200:
        message.append(line)
        line = ""
    if cycle == 240:
        message.append(line)
        line = ""
    return message

def pixelCheck(X, cycle):
    if abs(X - cycle) <= 1:
        return True
    else:
        return False


line = ""

for i in range(0, len(lines)):
    if pixelCheck(X, cycle):
        line = f"{line}#"
    else:
        line = f"{line}."
    print(cycle, X)
    print(line)
    print()
    if lines[i][:4] != "noop":
        cycle += 1
        if cycle % 40 == 0:
            message.append(line)
            line = ""
            cycle = 0
        if pixelCheck(X, cycle):
            line = f"{line}#"
        else:
            line = f"{line}."
        print(cycle, X)
        print(line)
        print()
        X += int(lines[i][5:])
    cycle += 1
    if cycle % 40 == 0:
        message.append(line)
        line = ""
        cycle = 0

for line in message:
    print(line)
