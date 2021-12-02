print("E2021 - Day 02");

class Maneuver:
    def __init__(self, command):
        action = command.split(" ")

        self.direction = action[0]
        self.distance = int(action[1])

class IDasBoot:
    def ExecuteManeuver(self, action: Maneuver):
        pass
    def GetPosition(self) -> int:
        pass

class U96(IDasBoot):
    def __init__(self):
        self.forward = 0
        self.depth = 0

    def ExecuteManeuver(self, action: Maneuver):
        if(action.direction == "forward"):
            self.forward += action.distance
        else:
            self.depth += (action.distance if action.direction == "down" else action.distance * -1)

    def GetPosition(self):
        return self.forward * self.depth

class U96Aimed(U96):
    def __init__(self):
        U96.__init__(self)

        self.aim = 0

    def ExecuteManeuver(self, action: Maneuver):
        if(action.direction == "forward"):
            self.forward += action.distance
            self.depth += action.distance * self.aim
        else:
            self.aim += (action.distance if action.direction == "down" else action.distance * -1)

def PartX(dasBoot: IDasBoot):
    with open('./input.txt') as input:
        for line in input:
            dasBoot.ExecuteManeuver(Maneuver(line))

    return dasBoot.GetPosition()

print(f" Answer 1st part is {PartX(U96())}")
print(f" Answer 2st part is {PartX(U96Aimed())}")
