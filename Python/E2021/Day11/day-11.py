print("E2021 - Day 11");

gridSize = -1
octopuses = []

def ReadInput():
    with open("./input.txt") as input:
        return input.read().splitlines()

class Octopus:
    def __init__(self, row, col, energy):
        self.row = row
        self.col = col
        self.energy = energy
        self.isFlashed = False
        self.neighbours = []

    def FillNeibhours(self, octopuses):
        gridSize = int(len(octopuses) ** 0.5) # sqrt
        for (dRow, dCol) in [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]:
            nRow = self.row + dRow
            nCol = self.col + dCol

            if(nRow >= 0 and nRow < gridSize and nCol >= 0 and nCol < gridSize):
                self.neighbours.append(octopuses[nRow * gridSize + nCol])

    def FirstStep(self):
        self.energy += 1

    def Flash(self):
        if(self.energy > 9 and not self.isFlashed):
            self.isFlashed = True
            self.KickNeibhours()

    def KickNeibhours(self):
        for neighbour in self.neighbours:
            neighbour.FirstStep()
            neighbour.Flash()

    def FinalStep(self):
        flashes = 0

        if(self.isFlashed):
            flashes += 1
            self.isFlashed = False
            self.energy = 0

        return flashes

input = ReadInput()

for row in range(len(input)):
    for col in range(len(input[row])):
        octopuses.append(Octopus(row, col, int(input[row][col])))

for octopus in octopuses:
    octopus.FillNeibhours(octopuses)

step = 0
flashes = 0

while(True):
    step += 1

    for octopus in octopuses:
        octopus.FirstStep()

    for octopus in octopuses:
        octopus.Flash()

    stepFlashes = 0

    for octopus in octopuses:
        stepFlashes += octopus.FinalStep()

    flashes += stepFlashes

    if(step == 100):
        print(f" Answer 1st part is {flashes}")

    if(stepFlashes == len(octopuses)):
        print(f" Answer 2nd part is {step}")
        break
