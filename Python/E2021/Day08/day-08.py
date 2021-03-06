print("E2021 - Day 08");

def ReadInput():
    with open("./input.txt") as input:
        return input.read().splitlines()

def GetDigits(digits, justUnique = True):
    uniques = {
        2, # 1
        4, # 4
        3, # 7
        7, # 8
    }

    digitPatterns = [{}]*10

    # Identify easy digits (unique length)
    for i in range(len(digits)):
        if(len(digits[i]) in uniques):
            segmentsCount = len(digits[i])
            idx = 1 if segmentsCount == 2 \
                else 4 if segmentsCount == 4 \
                else 7 if segmentsCount == 3 \
                else 8
            digitPatterns[idx] = set(digits[i])

    if(justUnique):
        return digitPatterns

    # Identify other digits based on known ones
    for j in range(len(digits)):
        digitPattern = set(digits[j])

        if(digitPattern in digitPatterns):
            # Known already
            continue

        if(len(digitPatterns[8] - digitPattern) == 1):
            # 6, 9, 0
            digit = 6 if digitPattern | digitPatterns[1] == digitPatterns[8] \
                else 9 if len(digitPattern - digitPatterns[4]) == 2 \
                else 0
        else:
            # 2, 3, 5
            digit =  3 if len(digitPattern - digitPatterns[1]) == 3 \
                else 2 if (digitPattern | digitPatterns[4]) == digitPatterns[8] \
                else 5

        digitPatterns[digit] = digitPattern

    return digitPatterns

def Part1():
    digits = list(map(lambda x: x.split(" | ")[1].split(), ReadInput()))

    uniqueSegments = 0

    for i in range(len(digits)):
        d1478 = GetDigits(digits[i])

        for j in range(len(digits[i])):
            uniqueSegments += 1 if set(digits[i][j]) in d1478 else 0

    return uniqueSegments

def Part2():
    input = ReadInput()

    outputSum = []
    
    for i in range(len(input)):
        entry = input[i].split(" | ")
        patterns = entry[0].split()
        output = entry[1].split()

        digits = GetDigits(patterns, justUnique = False)

        number = ""

        for j in range(len(output)):
            number += f"{digits.index(set(output[j]))}"

        outputSum.append(int(number))

    return sum(outputSum)

print(f" Answer 1st part is {Part1()}")
print(f" Answer 2st part is {Part2()}")
