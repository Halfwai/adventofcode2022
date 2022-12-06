with open("data.txt") as file:
    lines = [line.rstrip() for line in file]

for i in range(3, len(lines[0])):
    check = []
    for j in range(0, 4):
        check.append(lines[0][i - j])
    if len(set(check)) == 4:
        print(i+1)
        break
