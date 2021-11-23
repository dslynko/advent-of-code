import re

VERBOSE = False

def v_print(str):
    if(VERBOSE):
        print(str)

print("Day 04");

mandatoryFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def ValidNumber(number, min, max, title):
    intNumber = int(number)

    if((intNumber < min) or (intNumber > max)):
        v_print(f" X Value {intNumber} is INVALID ('{title}' should be in range=[{min}..{max}])")
        return False
    return True

def ValidString(string, regexp, title):
    if(not re.match(regexp, string)):
        v_print(f" X Value '{string}' is INVALID ('{title}' should match the pattern {regexp}")
        return False
    return True

def ValidHeight(string, title):
    hgtUnit = string[-2:]

    if(not(hgtUnit == "cm" or hgtUnit == "in")):
        v_print(f" X Value '{string}' is INVALID ('{title}' does not contain 'cm' or 'in'")
        return False

    min = 150 if hgtUnit == "cm" else 59
    max = 193 if hgtUnit == "cm" else 76

    hgt = string[:-2]

    return ValidNumber(hgt, min, max, "hgt")

class Passport:
    def __init__(self, inputStr):
        # input str: ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm

        bySpaces = inputStr.lstrip(" ").split(" ")

        for i in range(len(bySpaces)):
            keyValue = bySpaces[i].split(":")

            setattr(self, keyValue[0], keyValue[1])

    def IsValid1(self):
        return (len(vars(self)) == 8) or (self.AllMandatoryFieldsPresent())

    def AllMandatoryFieldsPresent(self):
        for i in range(len(mandatoryFields)):
            if(not hasattr(self, mandatoryFields[i])):
                return False

        return True

    def IsValid2(self):
        return (self.IsValid1() and (self.AllFieldsValuesAreOK()))
    
    def AllFieldsValuesAreOK(self):
        if(not ValidNumber(self.byr, 1920, 2002, "byr")):
            return False

        if(not ValidNumber(self.iyr, 2010, 2020, "iyr")):
            return False

        if(not ValidNumber(self.eyr, 2020, 2030, "eyr")):
            return False

        if(not ValidString(self.hcl, r"^\#[0-9a-f]{6}$", "hcl")):
            return False

        if(not ValidString(self.ecl, r"^amb|blu|brn|gry|grn|hzl|oth$", "ecl")):
            return False

        if(not ValidString(self.pid, r"^\d{9}$", "pid")):
            return False

        if(not ValidHeight(self.hgt, "hgt")):
            return False

        v_print(f"VALID {self.Output()}")

        return True

    def Output(self):
        props = []

        for att in sorted(self.__dict__):
            props.append(f"{att}:{getattr(self,att)};")

        return props

def ReadPassports():
    passports = []
    passportLine = ""

    with open('./input.txt') as input:
        for line in input:
            line = line.rstrip("\n")

            if(line != ""):
                passportLine = passportLine + " " + line
            else:
                passports.append(Passport(passportLine))
                passportLine = ""

        # last passport
        passports.append(Passport(passportLine))

    return passports

def Part1():
    return len(list(filter(lambda passport: passport.IsValid1(), ReadPassports())))

def Part2():
    return len(list(filter(lambda passport: passport.IsValid2(), ReadPassports())))

print(f" Answer 1st part is {Part1()}")
print(f" Answer 2nd part is {Part2()}")
