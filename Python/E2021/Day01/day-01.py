print("E2021 - Day 01");

def ReadInput():
    with open("./input.txt") as input:
        return input.read().splitlines()

def Part1(divesHistory):
    depthIncreases = 0
    previousDepth = 0

    for i in range(len(divesHistory)):
        currentDepth = int(divesHistory[i])

        if(currentDepth > previousDepth):
            depthIncreases += 1

        previousDepth = currentDepth

    return depthIncreases - 1;

def Part2(divesHistory):
    tripleDivesHistory = []

    i = 2
    length = len(divesHistory)

    while(i < length):
        tripleSum = int(divesHistory[i - 2]) + int(divesHistory[i - 1]) + int(divesHistory[i])
        tripleDivesHistory.append(tripleSum)
        i += 1

    return Part1(tripleDivesHistory)

divesHistory = ReadInput()

print(f" Answer 1st part is {Part1(divesHistory)}")
print(f" Answer 2st part is {Part2(divesHistory)}")
