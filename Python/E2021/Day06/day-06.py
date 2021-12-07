print("E2021 - Day 06");

def ReadInput():
    with open("./input.txt") as input:
        return list(map(int, input.readline().split(",")))

def PartX(days):
    lanternfishes = ReadInput()

    lanternfishesCounter = [0] * 9

    for i in range(len(lanternfishes)):
        lanternfishesCounter[lanternfishes[i]] += 1

    for i in range(days):
        lanternfishesCounter[(i + 7) % 9] += lanternfishesCounter[i % 9]

    return sum(lanternfishesCounter)

print(f" Answer 1st part is {PartX(80)}")
print(f" Answer 2st part is {PartX(256)}")
