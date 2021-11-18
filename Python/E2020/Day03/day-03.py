print("Day 03");

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

def ReadInput():
    with open("./input.txt") as input:
        return input.read().splitlines()

def NextPoint(currentPoint: Point, dx, dy):
    nx = currentPoint.x + dx if currentPoint.x + dx < width else currentPoint.x + dx - width

    return Point(nx, currentPoint.y + dy)

area = ReadInput()

height = len(area)
width = len(area[0])

def GoDownTheSlope(dx, dy):
    point = Point(0, 0)

    trees = 0

    while(point.y < height - 1):
        point = NextPoint(point, dx, dy)

        if(area[point.y][point.x] == "#"):
            trees += 1
            tree = "X"
        else:
            tree = "O"

        print(area[point.y][:point.x] + tree + area[point.y][point.x + 1:])

    return trees

def Part1():
    return GoDownTheSlope(3, 1)

def Part2():
    slope11 = GoDownTheSlope(1, 1)
    slope31 = GoDownTheSlope(3, 1)
    slope51 = GoDownTheSlope(5, 1)
    slope71 = GoDownTheSlope(7, 1)
    slope12 = GoDownTheSlope(1, 2)

    return slope11 * slope31 * slope51 * slope71 * slope12

print(f" Answer 1st part is {Part1()}")
print(f" Answer 1st part is {Part2()}")
