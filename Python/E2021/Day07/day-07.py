print("E2021 - Day 06");

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
            if(minFuel > 0 and fuel > minFuel):
                break
        minFuel = min(minFuel, fuel) if minFuel != -1 else fuel

    return minFuel

print(f" Answer 1st part is {PartX(lambda x: x)}")
print(f" Answer 2st part is {PartX(lambda x: int(((1 + x) * x) / 2))}")
