print("E2021 - Day 10");

def ReadInput():
    with open("./input.txt") as input:
        return input.read().splitlines()

openSymbols = ["(", "[", "{", "<"]
closeSymbols = [")", "]", "}", ">"]

def GetCloseSymbol(openSymbol):
    return closeSymbols[openSymbols.index(openSymbol)]

def GetPairs():
    return list(map(lambda x: f"{openSymbols[x]}{closeSymbols[x]}", range(len(openSymbols))))

def GetScore1(corruptedSymbol):
    return 3 if corruptedSymbol == ")" \
        else 57 if corruptedSymbol == "]" \
        else 1197 if corruptedSymbol == "}" \
        else 25137

def GetScore2(closeSymbol):
    return closeSymbols.index(closeSymbol) + 1

def ShrinkChunk(chunk):
    pairs = GetPairs()

    while(True):
        newChunk = chunk

        for pair in pairs:
            newChunk = newChunk.replace(pair, "")

        if(newChunk == chunk):
            return newChunk

        chunk = newChunk

def CorruptedScore(chunk):
    expectedSymbol = GetCloseSymbol(chunk[0])

    for i in range(1, len(chunk)):
        if(chunk[i] in closeSymbols):
            if(chunk[i] != expectedSymbol):
                return GetScore1(chunk[i])
        else:
            expectedSymbol = GetCloseSymbol(chunk[i])

    return 0

def Part1():
    lines = ReadInput()

    score = 0

    for line in lines:
        score += CorruptedScore(ShrinkChunk(line))

    return score

def Part2():
    lines = ReadInput()

    scores = []

    for line in lines:
        chunk = ShrinkChunk(line)

        if(CorruptedScore(chunk) == 0):
            chunk = list(map(GetCloseSymbol, chunk[::-1])) # reverse

            score = 0
            for completeSymbol in chunk:
                score = score * 5 + GetScore2(completeSymbol)

            scores.append(score)

    from statistics import median
    return median(scores)

print(f" Answer 1st part is {Part1()}")
print(f" Answer 2st part is {Part2()}")
