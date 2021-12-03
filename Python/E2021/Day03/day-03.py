print("E2021 - Day 03");

def ReadInput():
    with open("./input.txt") as input:
        return input.read().splitlines()

def GetRates(report: list, default = "1"):
    rates = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    reportLength = len(report)

    for i in range(reportLength):
        for j in range(len(report[i])):
            if(report[i][j] == "1"):
                rates[j] += 1

    gammaRate = epsilonRate = ""

    for i in range(len(rates)):
        if(rates[i] == reportLength / 2):
            gammaRate += default
            epsilonRate += default
        if(rates[i] > reportLength / 2):
            gammaRate += "1"
            epsilonRate += "0"
        else:
            gammaRate += "0"
            epsilonRate += "1"

    return (gammaRate, epsilonRate)

def GetLifeSupportRating(report: list, defaultNumber):
    bitPositionInMask = 0

    while(True):
        (gammaRate, epsilonRate) = GetRates(report, defaultNumber)

        mask = gammaRate if defaultNumber == "1" else epsilonRate

        report = list(filter(lambda number: number[bitPositionInMask] == mask[bitPositionInMask], report))

        if(len(report) == 1):
            return report[0]

        bitPositionInMask += 1

def GetOxygenGeneratorRate(report: list):
    return GetLifeSupportRating(report, "1")

def GetCO2ScrubberRate(report: list):
    return GetLifeSupportRating(report, "0")

def Part1(report):
    (gammaRate, epsilonRate) = GetRates(report)

    return int(gammaRate, 2) * int(epsilonRate, 2)

def Part2(report: list):
    oxygenGeneratorRate = GetOxygenGeneratorRate(report)
    co2ScrubberRate = GetCO2ScrubberRate(report)

    return int(oxygenGeneratorRate, 2) * int(co2ScrubberRate, 2)

report = ReadInput()

print(f" Answer 1st part is {Part1(report)}")
print(f" Answer 2st part is {Part2(report)}")
