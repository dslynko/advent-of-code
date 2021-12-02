print("E2021 - Day 01");

def ReadInput():
    with open("./input.txt") as input:
        return input.read().splitlines()

def CheckDepthHistory(divesHistory, diveToCompareIdx):
    depthIncreases = 0

    i = diveToCompareIdx
    length = len(divesHistory)

    while(i < length):
        currentDepth = int(divesHistory[i])
        previousDepth = int(divesHistory[i - diveToCompareIdx])

        depthIncreases += (1 if currentDepth > previousDepth else 0)

        i += 1

    return depthIncreases

def Part1(divesHistory):
    # a < b when (obwious) a < b, so 1 step back
    return CheckDepthHistory(divesHistory, 1)

def Part2(divesHistory):
    # a + b + c < b + c + d  when a < d, so 3 steps back
    return CheckDepthHistory(divesHistory, 3)

divesHistory = ReadInput()

print(f" Answer 1st part is {Part1(divesHistory)}")
print(f" Answer 2st part is {Part2(divesHistory)}")
