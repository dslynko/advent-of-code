print("E2021 - Day 14");

def ReadInput():
    with open("./input.txt") as input:
        return input.read().splitlines()

def GetLetterCounts(counts: dict):
    letterCounts = {}

    for (_, letter), count in counts.items():
        if(letter not in letterCounts):
            letterCounts[letter] = 0
        letterCounts[letter] += count

    return letterCounts

def PrintAnswer(msg, counts: list):
    letterCounts = GetLetterCounts(counts).values()
    print(f"Answer {msg} part is {max(letterCounts) - min(letterCounts)}")

input = ReadInput()
polymerTemplate = input[0]

rules = {}

for line in input[2:]:
    (pair, insert) = line.split(" -> ")
    rules[pair] = insert

counts = {}

for i in range(1, len(polymerTemplate)):
    (pairL, pairR) = polymerTemplate[i - 1:i + 1]
    counts[f"{pairL}{pairR}"] = 1

for step in range(40):
    newCounts = {}

    for pair in counts:
        if(pair in rules):
            (pairL, pairR) = pair
            insert = rules[pair]
            for newKey in [f"{pairL}{insert}", f"{insert}{pairR}"]:
                if(newKey not in newCounts):
                    newCounts[newKey] = 0
                newCounts[newKey] += counts[pair]

    counts = newCounts

    if(step == 9): # zero-based
        PrintAnswer("1st", counts)

PrintAnswer("2nd", counts)
