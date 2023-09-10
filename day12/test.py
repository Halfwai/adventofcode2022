with open("data.txt") as file:
    lines = [line.rstrip() for line in file]

class Node():

    def __init__(self, parent=None, position=None, letter=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.letter = letter

    def __eq__(self, other):
        return self.position == other.position

    def __add__(self, other):
        return int(ord(self.letter)) - int(ord(other.letter)) > -2

    def __str__(self):
        return f"Position:{self.position}, Letter:{self.letter}, f:{self.g}"

grid = []

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


routeMap = []

routeMap.append(startNode)

while routeMap:
    for currentNode in routeMap:
        if currentNode.position == endNode.position:
            path = []
            current = currentNode
            while current is not None:
                path.append(current)
                current = current.parent
            # for node in path:
            #     print(node)
            print(len(path) - 1)
            routeMap = []
            break
        else:
            children = []
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                node_position = (currentNode.position[0] + new_position[0], currentNode.position[1] + new_position[1])
                if node_position[0] > (len(grid[0]) - 1) or node_position[0] < 0 or node_position[1] > (len(grid) -1) or node_position[1] < 0:
                    continue
                child = Node(currentNode, node_position, grid[node_position[1]][node_position[0]])
                children.append(child)
            for child in children:
                if currentNode + child:
                    child.g = currentNode.g + 1
                    included = False
                    for node in routeMap:
                        if child.position == node.position and child.g > node.g:
                            included = True
                    if not included:
                        routeMap.append(child)

    # lowG = 100000000
    # position = 0
    # for i in range(len(openList)):
    #     if openList[i].g < lowG and openList[i].g != 0:
    #         lowG = openList[i].g
    #         position = i
    # currentNode = openList.pop(position)
    # closedList.append(currentNode)
    # if currentNode.position == endNode.position:
    #     path = []
    #     current = currentNode
    #     while current is not None:
    #         path.append(current)
    #         current = current.parent
    #     # for node in path:
    #     #     print(node)
    #     print(len(path) - 1)
    # else:
    #     children = []
    #     for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
    #         node_position = (currentNode.position[0] + new_position[0], currentNode.position[1] + new_position[1])
    #         if node_position[0] > (len(grid[0]) - 1) or node_position[0] < 0 or node_position[1] > (len(grid) -1) or node_position[1] < 0:
    #             continue
    #         child = Node(currentNode, node_position, grid[node_position[1]][node_position[0]])
    #         children.append(child)
    #     # if currentNode.position[0] != 0:
    #     #     leftLetter = Node(currentNode, (currentNode.position[0]-1,currentNode.position[1]), grid[currentNode.position[1]][currentNode.position[0]-1])
    #     #     children.append(leftLetter)
    #     # if currentNode.position[0] != len(grid[0])-1:
    #     #     rightLetter = Node(currentNode, (currentNode.position[0]+1,currentNode.position[1]), grid[currentNode.position[1]][currentNode.position[0]+1])
    #     #     children.append(rightLetter)
    #     # if currentNode.position[1] != 0:
    #     #     upLetter = Node(currentNode, (currentNode.position[0],currentNode.position[1]-1), grid[currentNode.position[1]-1][currentNode.position[0]])
    #     #     children.append(upLetter)
    #     # if currentNode.position[1] != len(grid)-1:
    #     #     downLetter = Node(currentNode, (currentNode.position[0],currentNode.position[1]+1), grid[currentNode.position[1]+1][currentNode.position[0]])
    #     #     children.append(downLetter)
    #     for child in children:
    #         if currentNode + child:
    #             included = False
    #             for node in closedList:
    #                 if child.position == node.position:
    #                     included = True
    #             if not included:
    #                 child.g = currentNode.g + 1
    #                 included = False
    #                 for node in openList:
    #                     if child.position == node.position:
    #                         if child.g > node.g:
    #                             included = True
    #                 if not included:
    #                     openList.append(child)
        # for list in openList:
        #     print(list)
        # print()

# print()
# for list in closedList:
#     print(list)

