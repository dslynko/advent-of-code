print("E2021 - Day 09");

def ReadInput():
    with open("./input.txt") as input:
        return input.read().splitlines()

def AddFenceToMap(heightmap):
    heightmap = list(map(lambda x: f"x{x}x", heightmap))
    xxxRow = "".join(["x"] * len(heightmap[0]))
    heightmap.insert(0, xxxRow)
    heightmap.append(xxxRow)

    return heightmap

def CheckAdjacentLocations(heightmap: list, y, x):
    smallMap = list(filter(lambda x: x != "x", [
        heightmap[y - 1][x],
        heightmap[y + 1][x],
        heightmap[y][x],
        heightmap[y][x - 1],
        heightmap[y][x + 1]
    ]))

    smallMap = list(map(int, smallMap))
    minPoint = min(smallMap)

    return (minPoint == int(heightmap[y][x])) and (len(list(filter(lambda x: x == minPoint, smallMap))) == 1)

def ExploreBasin(heightmap: list, y, x):
    points = [f"{y}:{x}"]

    current = int(heightmap[y][x])

    for shift in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        (dy, dx) = shift

        if((heightmap[y + dy][x + dx] not in {"x", "9"}) and (int(heightmap[y + dy][x + dx]) > current)):
            points += ExploreBasin(heightmap, y + dy, x + dx)

    return points

def GetLowPoints(heightmap):
    lowPoints = []

    for y in range(1, len(heightmap) - 1):
        for x in range(1, len(heightmap[y]) - 1):
            if CheckAdjacentLocations(heightmap, y, x):
                lowPoints.append(f"{y}:{x}")

    return lowPoints

def Part1():
    heightmap = AddFenceToMap(ReadInput())
    lowPoints = GetLowPoints(heightmap)

    lowPointsSum = 0

    for i in range(len(lowPoints)):
        (y, x) = list(map(int, lowPoints[i].split(":")))
        lowPointsSum += int(heightmap[y][x]) + 1

    return lowPointsSum

def Part2():
    heightmap = AddFenceToMap(ReadInput())
    lowPoints = GetLowPoints(heightmap)

    basins = []

    for i in range(len(lowPoints)):
        (y, x) = list(map(int, lowPoints[i].split(":")))
        basin = list(set(ExploreBasin(heightmap, y, x)))

        if(len(basin) > 1):
            basins.append(basin)

    basinSizes = list(map(lambda x: len(x), (basins)))
    basinSizes.sort(reverse = True)

    return basinSizes[0] * basinSizes[1] * basinSizes[2]

print(f" Answer 1st part is {Part1()}")
print(f" Answer 2st part is {Part2()}")
