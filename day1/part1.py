topnum = 0
secondnum = 0
thirdnum = 0
dataset = 0

with open("data.txt") as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    if line != "":
        dataset += int(line)
    else:
        if dataset > thirdnum:
            if dataset > secondnum:
                if dataset > topnum:
                    thirdnum = secondnum
                    secondnum = topnum
                    topnum = dataset
                else:
                    thirdnum = secondnum
                    secondnum = dataset
            else:
                thirdnum = dataset
        dataset = 0

print(topnum + secondnum + thirdnum)