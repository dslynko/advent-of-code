print("E2021 - Day 02");

class U96Action:
    def __init__(self, line):
        action = line.split(" ")

        self.direction = action[0]
        self.distance = int(action[1])

def Part1():
    forward = 0
    depth = 0

    with open('./input.txt') as input:
        for line in input:
            action = U96Action(line)

            if(action.direction == "forward"):
                forward += action.distance
            else:
                depth += (action.distance if action.direction == "down" else action.distance * -1)

    return forward * depth;

def Part2():
    forward = 0
    depth = 0
    aim = 0

    with open('./input.txt') as input:
        for line in input:
            action = U96Action(line)

            if(action.direction == "forward"):
                forward += action.distance
                depth += action.distance * aim
            else:
                aim += (action.distance if action.direction == "down" else action.distance * -1)

    return forward * depth;

print(f" Answer 1st part is {Part1()}")
print(f" Answer 2st part is {Part2()}")
