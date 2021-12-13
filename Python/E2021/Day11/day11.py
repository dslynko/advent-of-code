print("E2021 - Day 11");

gridSize = -1
octopuses = []

def ReadInput():
    with open("/Users/dimitry/Work/Study/AdventOfCode/2020/Python/E2021/Day11/input.test.txt") as input:
        return input.read().splitlines()

class Octopus:
    def __init__(self, row, col, energy):
        self.row = row
        self.col = col
        self.energy = energy
        self.isFlashed = False

    def FirstStep(self):
        self.energy += 1

    def Flash(self):
        if(self.energy > 9 and not self.isFlashed):
            self.isFlashed = True
            self.KickNeibhours()

    def KickNeibhours(self):
        for (dRow, dCol) in [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]:
            nRow = self.row + dRow
            nCol = self.col + dCol
            if(nRow >= 0 and nRow < gridSize and nCol >= 0 and nCol < gridSize):
                neighbour = GetOctopusAt(nRow, nCol)
                neighbour.FirstStep()
                neighbour.Flash()

    def FinalStep(self):
        flashes = 0

        if(self.isFlashed):
            flashes += 1
            self.isFlashed = False
            self.energy = 0

        return flashes

    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return f"{self.energy}@[{self.row}:{self.col}]"

def GetOctopusAt(row, col) -> Octopus:
    for octopus in octopuses:
        if(octopus.row == row and octopus.col == col):
            return octopus

def PrintOctopuses(octopuses: list[Octopus]):
    print("---")
    currLine = 0
    line = ""
    for octopus in octopuses:
        if (currLine != octopus.row):
            print(line)
            line = ""
            currLine += 1
        line += f"{octopus.energy}"
    print(line)

def Part1(octopuses: list[Octopus]):
    flashes = 0

    for step in range(100):
        for octopus in octopuses:
            octopus.FirstStep()

        for octopus in octopuses:
            octopus.Flash()

        for octopus in octopuses:
            flashes += octopus.FinalStep()

    return flashes

def Part2(octopuses: list[Octopus]):
    step = 0

    while(True):
        step += 1
        #print(step)

        for octopus in octopuses:
            octopus.FirstStep()

        for octopus in octopuses:
            octopus.Flash()

        flashes = 0

        for octopus in octopuses:
            flashes += octopus.FinalStep()
        #PrintOctopuses(octopuses)

        if(flashes == gridSize ** 2):
            return step

input = ReadInput()
gridSize = len(input)

for row in range(len(input)):
    for col in range(len(input[row])):
        octopuses.append(Octopus(row, col, int(input[row][col])))

print(f" Answer 1st part is {Part1(octopuses)}")
print(f" Answer 2st part is {Part2(octopuses)}")
