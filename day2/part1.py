score = 0

with open("data.txt") as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    round = line.split()
    if round[0] == "A":
        if round[1] == "X":
            score += 4
        elif  round[1] == "Y":
            score += 8
        elif  round[1] == "Z":
            score += 3
    elif round[0] == "B":
        if round[1] == "X":
            score += 1
        elif  round[1] == "Y":
            score += 5
        elif  round[1] == "Z":
            score += 9
    elif round[0] == "C":
        if round[1] == "X":
            score += 7
        elif  round[1] == "Y":
            score += 2
        elif  round[1] == "Z":
            score += 6

print(score)

# A - 1 - Rock
# B - 2 - Paper
# C - 3 - Scissors

# X - Rock
# Y - Paper
# Z - Scissors