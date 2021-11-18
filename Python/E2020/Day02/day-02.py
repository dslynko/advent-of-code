print("Day 02");

class Policy:
    def __init__(self, inputStr):
        # InputStr: "5-16 j: jjjjkjjzjjjjjfjzjjj"
        bySpaces = inputStr.split(" ")

        minmax = bySpaces[0].split("-")

        self.min = int(minmax[0])
        self.max = int(minmax[1])

        self.letter = bySpaces[1][0]

        self.password = bySpaces[2]

def Part1():
    validPasswords = 0

    with open('./input.txt') as input:
        for line in input:
            policy = Policy(line);

            letterOccurences = policy.password.count(policy.letter)

            if(letterOccurences >= policy.min and letterOccurences <= policy.max):
                validPasswords += 1

    return validPasswords;

def Part2():
    from operator import xor

    validPasswords = 0

    with open('./input.txt') as input:
        for line in input:
            policy = Policy(line);

            if(xor(policy.password[policy.min - 1] == policy.letter, policy.password[policy.max - 1] == policy.letter)):
                validPasswords += 1

    return validPasswords

print(f" Answer 1st part is {Part1()}")
print(f" Answer 2st part is {Part2()}")
