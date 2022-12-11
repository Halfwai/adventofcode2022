with open("testdata.txt") as file:
    lines = [line.rstrip() for line in file]

monkeys = []

monkey = {}

for i in range(len(lines)):
    if lines[i][2:7] == "Start":
        items = lines[i][18:]
        itemlist = [word.strip() for word in items.split(",")]
        for j in range(len(itemlist)):
            itemlist[j] = int(itemlist[j])
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

for i in range(6):
    for monkey in monkeys:
        while monkey["items"]:
            if monkey["operation"][0] == "*":
                try:
                    monkey["items"][0] = int(monkey["items"][0]) * int(monkey["operation"][1:])
                except:
                    monkey["items"][0] = int(monkey["items"][0]) * int(monkey["items"][0])
            if monkey["operation"][0] == "+":
                monkey["items"][0] = int(monkey["items"][0]) + int(monkey["operation"][1:])
            if monkey["items"][0] % monkey["divide"] == 0:
                monkeys[monkey["true"]]["items"].append(monkey["items"][0])
                monkey["items"].pop(0)
            else:
                monkeys[monkey["false"]]["items"].append(monkey["items"][0])
                monkey["items"].pop(0)
            monkey["counter"] += 1

monkeyBusiness1 = 0
monkeyBusiness2 = 0
for monkey in monkeys:
    if monkey['counter'] >= monkeyBusiness1:
        monkeyBusiness2 = monkeyBusiness1
        monkeyBusiness1 = monkey['counter']
    elif monkey['counter'] >= monkeyBusiness2:
        monkeyBusiness2 = monkey['counter']

print(monkeyBusiness1 * monkeyBusiness2)