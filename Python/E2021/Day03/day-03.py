print("E2021 - Day 03 #########################s");

def ReadInput():
    with open("./input.txt") as input:
        return input.read().splitlines()

def PrettyBin(n):
    b = bin(n)[2:]
    return b.zfill(12)

def GetRates(report: list, default = "1"):
    rates = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    reportLength = len(report)

    for i in range(reportLength):
        for j in range(len(report[i])):
            if(report[i][j] == "1"):
                rates[j] += 1

    gammaRate = ""

    for i in range(len(rates)):
        gammaRate += (default if rates[i] == reportLength / 2 else "1" if rates[i] > reportLength / 2 else "0")

    print(f"gammaRate: {gammaRate}")
    gammaRate = int(gammaRate, 2)
    epsilonRate = ~gammaRate & 0xFFF
    print(f"epslnRate: {PrettyBin(epsilonRate)}")

    return (gammaRate, epsilonRate)

def GetLifeSupportRating(report: list, defaultNumber):
    bitPositionInMask = 0

    while(True):
        (gammaRate, epsilonRate) = GetRates(report, defaultNumber)

        mask = PrettyBin(gammaRate if defaultNumber == "1" else epsilonRate)
        print(f"mask: {mask}")

        maskBit = mask[bitPositionInMask]

        report = list(filter(lambda number: number[bitPositionInMask] == mask[bitPositionInMask], report))
        print(f"CUT (len: {len(report)} pos: {bitPositionInMask}): {report}")

        if(len(report) == 1):
            print(report)
            print(f"  {mask}")
            return int(report[0], 2)

        bitPositionInMask += 1

        if bitPositionInMask > 12: return -1

def Part1(report):
    (gammaRate, epsilonRate) = GetRates(report)

    return gammaRate * epsilonRate

def Part2(report: list):
    oxygenGeneratorRate = GetLifeSupportRating(report, "1")
    co2ScrubberRate = GetLifeSupportRating(report, "0")

    return oxygenGeneratorRate * co2ScrubberRate

report = ReadInput()

print(f" Answer 1st part is {Part1(report)}")
#print(f" Answer 2st part is {Part2(report)}")
