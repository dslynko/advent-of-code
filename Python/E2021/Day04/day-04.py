print("E2021 - Day 04");

class Bingo:
    def __init__(self, numbers):
        self.numbers = numbers

    def IsBingo(self, number):
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[i])):
                if(self.numbers[i][j] == number):
                    self.numbers[i][j] = 0
                    return self.CheckRow(i) or self.CheckColumn(j)

    def CheckRow(self, rowIdx):
        return sum(self.numbers[rowIdx]) == 0

    def CheckColumn(self, colIdx):
        for i in range(len(self.numbers)):
            if(self.numbers[i][colIdx] > 0):
                return False
        return True

    def Sum(self):
        return sum(item for sublist in self.numbers for item in sublist)

    def Print(self):
        print(self.numbers)

def ReadInput():
    with open('./input.txt') as input:
        cards = []

        firstLine = True
        numbers = []

        for line in input:
            line = line.rstrip("\n")

            if(firstLine):
                randomSet = list(map(int, line.split(",")))
                firstLine = False
                continue

            if(line == ""):
                if(len(numbers) > 0):
                    cards.append(Bingo(numbers))
                    numbers = []
                continue

            numbers.append(list(map(int, line.split())))

    return (randomSet, cards)

def Part1(randomSet: list, cards: list[Bingo]):
    for i in range(len(randomSet)):
        for j in range(len(cards)):
            if(cards[j].IsBingo(randomSet[i])):
                print(f"BINGO! number is {randomSet[i]}")
                return cards[j].Sum() * randomSet[i]

    # Should never get here
    return -1

def Part2(randomSet: list, cards: list[Bingo]):
    for i in range(len(randomSet)):
        cardsWon = 0

        for j in range(len(cards)):
            cardIdx = j - cardsWon

            if(cards[cardIdx].IsBingo(randomSet[i])):
                if(len(cards) == 1):
                    print(f"BINGO! number is {randomSet[i]}")
                    return cards[cardIdx].Sum() * randomSet[i]
                else:
                    del cards[cardIdx]
                    cardsWon += 1

    # Should never get here
    return -1

(randomSet, cards) = ReadInput()

print(f" Answer 1st part is {Part1(randomSet, cards)}")
print(f" Answer 2st part is {Part2(randomSet, cards)}")
