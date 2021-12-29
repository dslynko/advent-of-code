print("E2021 - Day 13")

class Dot:
    def __init__(self, line):
        (self.x, self.y) = list(map(int, line.rstrip().split(',')))
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))

class Fold:
    def __init__(self, line):
        (self.type, line) =  line.rstrip()[11:].split("=")
        self.line = int(line)

def ReadInput():
    with open("./input.txt") as input:
        allDotsWereRead = False

        dots = []
        folds = []

        for line in input:
            if(line == "\n"):
                allDotsWereRead = True
                continue

            if(not allDotsWereRead):
                dots.append(Dot(line))
            else:
                folds.append(Fold(line))

    return (dots, folds)

def PerformFold(dots, fold):
    for i in range(len(dots)):
        if(fold.type == "y"):
            if(dots[i].y >= fold.line):
                dots[i].y = dots[i].y - 2 * (dots[i].y - fold.line)
        else:
            if(dots[i].x > fold.line):
                dots[i].x = dots[i].x - 2 * (dots[i].x - fold.line)
    return dots

def GetScreenWidth(dots):
    width = height = 0

    for dot in dots:
        if(dot.x > width):
            width = dot.x
        if(dot.y > height):
            height = dot.y

    return (width, height)

def GetScreen(dots):
    dots = set(dots)

    (width, height) = GetScreenWidth(dots)

    screen = []
    for y in range(height + 1):
        line = []
        for x in range(width + 1):
            line.append(".")
        screen.append(line)

    for dot in dots:
        screen[dot.y][dot.x] = "#"

    message = ""
    for line in screen:
        message += "".join(line)+"\n"

    return message

def Part1():
    (dots, folds) = ReadInput()

    return len(set(PerformFold(dots, folds[0])))

def Part2():
    (dots, folds) = ReadInput()

    for fold in folds:
        dots = PerformFold(dots, fold)

    return "\n" + GetScreen(dots)

print(f" Answer 1st part is {Part1()}")
print(f" Answer 2nd part is {Part2()}")
