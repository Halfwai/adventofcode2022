with open("data.txt") as file:
    lines = [line.rstrip() for line in file]

for i in range(13, len(lines[0])):
    check = []
    for j in range(0, 14):
        check.append(lines[0][i - j])
    if len(set(check)) == 14:
        print(i+1)
        break