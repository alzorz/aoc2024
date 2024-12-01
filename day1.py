
listA = []
listB = []

with open("day1.input", "r") as file:
    for line in file:
        parts = line.strip().split()
        listA.append(int(parts[0]))
        listB.append(int(parts[1]))

listA.sort()
listB.sort()

distances = []
score = 0
for i in range(len(listA)):
    distance = abs(listA[i] - listB[i])
    distances.append(distance)

    matches = 0
    listAValue = listA[i]
    for y in range(len(listB)):
        if listAValue == listB[y]:
            matches += 1
    score += matches * listAValue


print(f"Part1: {sum(distances)}")
print(f"Part2: {score}")
