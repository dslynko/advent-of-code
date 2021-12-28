from collections import defaultdict

print("E2021 - Day 12")

def ReadInput():
    caves = defaultdict(set)
    with open("./input.txt") as input:
        for line in input:
            (caveFrom, caveTo) = line.strip().split("-")
            caves[caveFrom].add(caveTo)
            caves[caveTo].add(caveFrom)

    return caves

def PathsCount(caves, currentCave, seen, visitTwice):
    if(currentCave == "end"):
        return 1

    if(currentCave.islower() and currentCave in seen):
        if(currentCave == "start" or not visitTwice):
            return 0

        visitTwice = False

    nextCaves = caves[currentCave]
    newSeen = seen | {currentCave}

    return sum(PathsCount(caves, nextCave, newSeen, visitTwice) for nextCave in nextCaves)

def PartX(visitTwice):
    caves = ReadInput()
    return PathsCount(caves, "start", set(), visitTwice)

print(f" Answer 1st part is {PartX(False)}")
print(f" Answer 2nd part is {PartX(True)}")
