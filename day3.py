import re

lines = []
with open("day3.input", "r") as file:
    for line in file:
        lines.append(line.strip())

def partOne():
    mulPattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
    numPattern = r"[0-9]+"

    sum = 0
    for line in lines:
        matches = re.findall(mulPattern, line)
        for match in matches:
            numbers = re.findall(numPattern, match)
            sum += int(numbers[0]) * int(numbers[1])
    return sum

print(f"Part one: {partOne()}")

def partTwo():
    mulPattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)"
    numPattern = r"[0-9]+"

    sum = 0
    skip = False
    for line in lines:
        matches = re.findall(mulPattern, line)
        for match in matches:
            if match == "don't()":
                skip = True
            elif match == "do()":
                skip = False
            elif not skip:
                numbers = re.findall(numPattern, match)
                sum += int(numbers[0]) * int(numbers[1])
    return sum

print(f"Part two: {partTwo()}")