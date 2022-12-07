import re

with open("data.txt") as file:
    lines = [line.rstrip() for line in file]

data = {}

totalSize = 0

sizeDict = {}

def tallySize(key):
    tally = 0
    for datapoint in data[key]:
        if datapoint[0:3] != "dir":
            size = re.findall(r'\d+', datapoint)
            tally += int(size[0])
        else:
            tally += tallySize(f"{key}{datapoint[4:]}/")
    return tally

path = ""
for i in range(0, len(lines)):
    if lines[i][0] == "$":
        if lines[i][2:4] == "cd":
            if lines[i][5:] != "..":
                if lines[i][5] == "/":
                    path = "/"
                else:
                    path = f"{path}{lines[i][5:]}/"
                data[path] = []
            else:
                split = path.rfind("/")
                path = path[:split]
                split = path.rfind("/")
                path = path[:split+1]
        if lines[i][2:4] == "ls":
            startpoint = i + 1
            while startpoint < len(lines) and lines[startpoint][0] != "$":
                data[path].append(lines[startpoint])
                startpoint += 1


for key in data:
    path = key
    total = tallySize(key)
    sizeDict[key] = total

spaceNeeded = 30000000 - (70000000 - sizeDict["/"])

smallestFilesize = 0
for key in sizeDict:
    if sizeDict[key] >= spaceNeeded:
        if smallestFilesize == 0:
            smallestFilesize = sizeDict[key]
        if sizeDict[key] < smallestFilesize:
            smallestFilesize = sizeDict[key]

print(smallestFilesize)
