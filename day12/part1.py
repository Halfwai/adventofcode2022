with open("data.txt") as file:
    lines = [line.rstrip() for line in file]

grid = []

openList = []

closedList = []

class Node():

    def __init__(self, parent=None, position=None, letter=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0
        self.letter = letter

    def __eq__(self, other):
        return self.position == other.position

    def compare(self, other):
        return int(ord(self.letter)) - int(ord(other.letter)) > -2

    def __str__(self):
        return f"Position:{self.position}, Letter:{self.letter}, f:{self.f}"

for i in range(len(lines)):
    row = []
    for j in range(len(lines[i])):
        letter = lines[i][j]
        if letter == "S":
            startNode = Node(None, (j, i), "a")
            row.append("a")
        elif lines[i][j] == "E":
            endNode = Node(None, (j, i), "z")
            row.append("z")
        else:
            row.append(letter)
    grid.append(row)

openList.append(startNode)


while openList:
    currentNode = openList[0]
    current_index = 0
    for index, item in enumerate(openList):
        if item.f < currentNode.f:
            currentNode = item
            current_index = index
    openList.pop(current_index)
    closedList.append(currentNode)
    if currentNode.position == endNode.position:
        path = []
        current = currentNode
        while current is not None:
            path.append(current)
            current = current.parent
        print(len(path) - 1)
    else:
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (currentNode.position[0] + new_position[0], currentNode.position[1] + new_position[1])
            if node_position[0] > (len(grid[0]) - 1) or node_position[0] < 0 or node_position[1] > (len(grid) -1) or node_position[1] < 0:
                continue
            child = Node(currentNode, node_position, grid[node_position[1]][node_position[0]])
            children.append(child)
        for child in children:
            if currentNode.compare(child):
                included = False
                if included == False:
                    child.g = currentNode.g + 1
                    child.h = ((child.position[0] - endNode.position[0]) ** 2) + ((child.position[1] - endNode.position[1]) ** 2)
                    child.f = child.g + child.h
                    for node in closedList:
                        if child == node:
                            included = True
                    for node in openList:
                        if child.position == node.position:
                            if child.g >= node.g:
                                included = True
                    if included == False:
                        # print(child)
                        openList.append(child)
        # for list in openList:
        #     print(list)
        # print()


# for node in closedList:
#     if node.g > 500:
#         print(node)

