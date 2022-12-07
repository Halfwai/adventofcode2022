import re

with open("data.txt") as file:
    lines = [line.rstrip() for line in file]

data = {}

totalSize = 0

def tallySize(key, tally):
    for datapoint in data[key]:
        if datapoint[0:3] == "dir":
            tally += tallySize(f"{key}/{datapoint[4:]}", tally)
        else:
            size = re.findall(r'\d+', datapoint)
            tally += int(size[0])
    return tally

path = "/"
for i in range(0, len(lines)):
    if lines[i][0] == "$":
        if lines[i][2:4] == "cd":
            if lines[i][5:] != "..":
                if path != "/":
                    path = f"{path}/{lines[i][5:]}"
                data[path] = []
            else:
                split = path.rfind("/")
                path = path[:split]
        if lines[i][2:4] == "ls":
            startPoint = i+1
            try:
                while lines[startPoint][0] != "$":
                    data[path].append(lines[startPoint])
                    startPoint += 1
            except:
                pass

for key in data:
    path = key
    tally = 0
    total = tallySize(key, tally)
    if total <= 100000:
        totalSize += total

print(totalSize)

