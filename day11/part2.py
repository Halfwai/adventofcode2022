with open("data.txt") as file:
    lines = [line.rstrip() for line in file]

monkeys = []

monkey = {}

itemNumber = 0

itemValues = []

itemsList = {}

for i in range(len(lines)):
    if lines[i][2:7] == "Start":
        items = lines[i][18:]
        itemlist = [word.strip() for word in items.split(",")]
        for j in range(len(itemlist)):
            itemsList[f"item{itemNumber}"] = [int(itemlist[j]),]
            itemlist[j] = f"item{itemNumber}"
            itemNumber += 1
        monkey["items"] = itemlist
    if lines[i][2:7] == "Opera":
        monkey["operation"] = lines[i][23:]
    if lines[i][2:6] == "Test":
        monkey["divide"] = int(lines[i][21:])
        monkey["true"] = int(lines[i+1][29:])
        monkey["false"] = int(lines[i+2][30:])
    if lines[i] == "":
        monkey["counter"] = 0
        monkeys.append(monkey)
        monkey = {}
monkey["counter"] = 0
monkeys.append(monkey)

for item in itemsList:
    initialValue = itemsList[item].pop()
    for monkey in monkeys:
        value = initialValue % int(monkey["divide"])
        if value == 0:
            value = int(monkey["divide"])
        itemsList[item].insert(len(itemsList[item]), value)

def valuesOperations(monkey, item):
    for i in range(len(item)):
        if monkey["operation"][0] == "*":
            try:
                item[i] = item[i] * int(monkey["operation"][1:])
            except:
                item[i] = item[i] * item[i]
        if monkey["operation"][0] == "+":
            item[i] = item[i] + int(monkey["operation"][1:])
    return item

def modItem(monkeys, item):
    for i in range(len(monkeys)):
        mod = item[i] % monkeys[i]["divide"]
        if mod != 0:
            item[i] = mod
    return item

for k in range(10000):
    for i in range(len(monkeys)):
        counter = 0
        for item in monkeys[i]["items"]:
            itemsList[item] = valuesOperations(monkeys[i], itemsList[item])
            if itemsList[item][i] % monkeys[i]["divide"] == 0:
                monkeys[monkeys[i]["true"]]["items"].append(item)
            else:
                monkeys[monkeys[i]["false"]]["items"].append(item)
            itemsList[item] = modItem(monkeys, itemsList[item])
            monkeys[i]["counter"] += 1
            counter += 1
        for j in range(counter):
            monkeys[i]["items"].pop(0)

monkeyBusiness1 = 0
monkeyBusiness2 = 0
for monkey in monkeys:
    if monkey['counter'] >= monkeyBusiness1:
        monkeyBusiness2 = monkeyBusiness1
        monkeyBusiness1 = monkey['counter']
    elif monkey['counter'] >= monkeyBusiness2:
        monkeyBusiness2 = monkey['counter']

print(monkeyBusiness1 * monkeyBusiness2)