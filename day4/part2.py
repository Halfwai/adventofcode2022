def pairCheck(pair):
    first = pair[0].split("-")
    second = pair[1].split("-")
    result = False
    if int(first[0]) >= int(second[0]) and int(first[0]) <= int(second[1]):
        result = True
    elif int(first[1]) >= int(second[0]) and int(first[1]) <= int(second[1]):
        result = True
    elif int(second[0]) >= int(first[0]) and int(second[0]) <= int(first[1]):
        result = True
    elif int(second[1]) >= int(first[0]) and int(second[1]) <= int(first[1]):
        result = True
    return result

counter = 0

with open("data.txt") as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    pair = line.split(",")
    if pairCheck(pair):
        counter += 1


print(counter)