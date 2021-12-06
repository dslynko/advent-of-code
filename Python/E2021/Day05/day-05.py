print("E2021 - Day 05");

class Point:
    def __init__(self, line):
        (self.x, self.y) = list(map(lambda x: int(x), line.split(",")))

class LineOfVents():
    def __init__(self, line):
        (self.startPoint, self.endPoint) = list(map(lambda x: Point(x), line.split(" -> ")))

    def IsHorisontal(self):
        return self.startPoint.y == self.endPoint.y

    def IsVertical(self):
        return self.startPoint.x == self.endPoint.x

    def Is45Degrees(self):
        return abs(self.startPoint.x - self.endPoint.x) == abs(self.startPoint.y - self.endPoint.y)

    def IsValid(self, includeDiagonals = False):
        return self.IsHorisontal() or self.IsVertical() or (includeDiagonals and self.Is45Degrees())

    def DrawLineOnDiagram(self, diagram, includeDiagonals = False):
        if(self.IsHorisontal()):
            for x in range(min(self.startPoint.x, self.endPoint.x), max(self.startPoint.x, self.endPoint.x) + 1):
                diagram[self.startPoint.y][x] += 1
        elif(self.IsVertical()):
            for y in range(min(self.startPoint.y, self.endPoint.y), max(self.startPoint.y, self.endPoint.y) + 1):
                diagram[y][self.startPoint.x] += 1
        elif(includeDiagonals and self.Is45Degrees()):
            dx = 1 if self.startPoint.x < self.endPoint.x else -1
            dy = 1 if self.startPoint.y < self.endPoint.y else -1
            s = 0
            for y in range(min(self.startPoint.x, self.endPoint.x), max(self.startPoint.x, self.endPoint.x) + 1):
                diagram[self.startPoint.y + s * dy][self.startPoint.x + s * dx] += 1
                s+=1

def ReadInput(includeDiagonals = False):
    linesOfVents = []
    maxX = maxY = -1

    with open('./input.txt') as input:
        for line in input:
            line = line.rstrip("\n")

            lineOfVent = LineOfVents(line)

            if(lineOfVent.IsValid(includeDiagonals)):
                linesOfVents.append(lineOfVent)

                maxX = max(lineOfVent.startPoint.x, lineOfVent.endPoint.x) if maxX == -1 else max(maxX, lineOfVent.startPoint.x, lineOfVent.endPoint.x)
                maxY = max(lineOfVent.startPoint.y, lineOfVent.endPoint.y) if maxY == -1 else max(maxY, lineOfVent.startPoint.y, lineOfVent.endPoint.y)

    diagram = [[0 for x in range(maxX + 1)] for y in range(maxY + 1)]

    return (diagram, linesOfVents)

def Part1(includeDiagonals = False):
    (diagram, linesOfVents) = ReadInput(includeDiagonals)

    for i in range(len(linesOfVents)):
        linesOfVents[i].DrawLineOnDiagram(diagram, includeDiagonals)

    overlaps = 0

    for i in range(len(diagram)):
        overlaps += len(list(filter(lambda x: x >= 2, diagram[i])))

    return overlaps

def Part2():
    return Part1(True)

print(f" Answer 1st part is {Part1()}")
print(f" Answer 2st part is {Part2()}")
