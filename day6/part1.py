with open("data.txt") as file:
    line = file.read()

for i in range(3, len(line)):
    check = line[i-4:i]
    if len(set(check)) == 4:
        print(i)
        break
