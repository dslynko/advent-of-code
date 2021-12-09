print("E2021 - Day 07");

def ReadInput():
    with open("./input.txt") as input:
        return list(map(int, input.readline().split(",")))

def PartX(calculateFuel):
    positions = ReadInput()

    minFuel = -1

    for i in range(min(positions), max(positions) + 1):
        fuel = 0
        for j in range(len(positions)):
            fuel += calculateFuel(abs(positions[j] - i))
            if(fuel > minFuel and minFuel > 0):
                break
        minFuel = min(minFuel, fuel) if minFuel != -1 else fuel

    return minFuel

print(f" Answer 1st part is {PartX(lambda n: n)}")
print(f" Answer 2st part is {PartX(lambda n: int((1 + n) * n / 2))}")
