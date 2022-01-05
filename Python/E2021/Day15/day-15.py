print("E2021 - Day 15")

def GetMapSize(riskMap):
    return (len(riskMap), len(riskMap[0]))

class Point:
    def __init__(self, row, col, riskLevel):
        self.row = row
        self.col = col
        self.riskLevel = riskLevel
        self.riskLevelSum = float('inf')
        self.isVisited = False

    def __lt__(self, other):
        return self.riskLevelSum < other.riskLevelSum

    def Neibhours(self, riskMap):
        (height, width) = GetMapSize(riskMap)

        neighbours = []

        for (dRow, dCol) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nRow = self.row + dRow
            nCol = self.col + dCol

            if(nRow >= 0 and nRow < height and nCol >= 0 and nCol < width and not riskMap[nRow][nCol].isVisited):
                neighbours.append(riskMap[nRow][nCol])

        neighbours.sort()

        return neighbours

def GetRiskLevelForMultiplier(riskLevel, multiplier):
    return (riskLevel + multiplier) % 9 + 1

def MultiplyCols(row, riskLine, multiply):
    width = len(riskLine)

    for multiplier in range(multiply - 1):
        for c in range(width):
            riskLine.append(Point(row, len(riskLine), GetRiskLevelForMultiplier(riskLine[c].riskLevel, multiplier)))

    return riskLine

def MultiplyRows(riskMap, multiply):
    (height, width) = GetMapSize(riskMap)

    for multiplier in range(multiply - 1):
        for r in range(height):
            newLine = []
            row = len(riskMap)

            for c in range(width):
                newLine.append(Point(row, len(newLine), GetRiskLevelForMultiplier(riskMap[r][c].riskLevel, multiplier)))

            riskMap.append(newLine)

    return riskMap

def ReadInput(multiply = 1):
    riskMap = []

    with open("./input.txt") as input:
        for line in input:
            riskLine = []
            row = len(riskMap)

            for number in line.rstrip():
                riskLine.append(Point(row, len(riskLine), int(number)))

            riskLine = MultiplyCols(row, riskLine, multiply)

            riskMap.append(riskLine)

    return MultiplyRows(riskMap, multiply)

def CalculatePaths(currentPoint, riskMap):
    toQueue = []

    if(currentPoint.isVisited):
        return toQueue

    for neibhour in currentPoint.Neibhours(riskMap):
        if(currentPoint.riskLevelSum + neibhour.riskLevel < neibhour.riskLevelSum):
            neibhour.riskLevelSum = currentPoint.riskLevelSum + neibhour.riskLevel
        toQueue.append(riskMap[neibhour.row][neibhour.col])

    currentPoint.isVisited = True

    return toQueue

def GetLowestRiskPath(riskMap):
    queue = [riskMap[0][0]]
    riskMap[0][0].riskLevelSum = 0

    while(len(queue) > 0):
        toQueue = CalculatePaths(queue.pop(0), riskMap)

        if(len(toQueue) > 0):
            queue += toQueue
            queue.sort()

    return riskMap[len(riskMap) - 1][len(riskMap[0]) - 1].riskLevelSum

def PartX(multiply = 1):
    riskMap = ReadInput(multiply)

    return GetLowestRiskPath(riskMap)

print(f" Answer 1st part is {PartX()}")
print(f" Answer 2nd part is {PartX(multiply = 5)}")