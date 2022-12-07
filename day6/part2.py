with open("data.txt") as file:
    line = file.read()

for i in range(13, len(line)):
    check = line[i-14:i]
    if len(set(check)) == 14:
        print(i)
        break