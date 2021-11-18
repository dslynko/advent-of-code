print("Day 03");

dx = 3
dy = 1

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

def ReadInput():
    with open("./input.txt") as input:
        return input.read().splitlines()

def NextPoint(currentPoint: Point):
    nx = currentPoint.x + dx if currentPoint.x + dx < width else currentPoint.x + dx - width

    return Point(nx, currentPoint.y + dy)

area = ReadInput()

height = len(area)
width = len(area[0])

print(f"{width}x{height}")

point = Point(0, 0)

trees = 0

while(point.y < height - 1):
    point = NextPoint(point)

    if(area[point.y][point.x] == "#"):
        trees += 1
        tree = 'X'
    else:
        tree = 'O'

    print(area[point.y][:point.x] + tree + area[point.y][point.x + 1:])

print(f" Answer 1st part is {trees}")
