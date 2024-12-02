
reports = []

with open("day2.input", "r") as file:
    for line in file:
        parts = line.strip().split(" ")
        reports.append(parts)

def processReport(report):
    isSafe = []
    increasing = []
    lastLevel = int(report[0])
    for level in report[1:]:
        level = int(level)

        diff = abs(level - lastLevel)
        isSafe.append(1 <= diff and diff <= 3)

        
        if level < lastLevel:
            increasing.append(False)
        elif level > lastLevel:
            increasing.append(True)
        else:
            increasing.append(None)
        
        lastLevel = level

    setSafe = set(isSafe)
    setInc = set(increasing)
    return (len(setSafe) == 1 and setSafe.pop()) and len(setInc) == 1


safeCount = 0
for report in reports:
    if processReport(report):
        safeCount += 1
print(f"Part1: {safeCount}")


def dampener(report, i, origReport):
    if processReport(report):
        return True
    elif i > len(report):
        return False
    else:
        newReport = origReport[:i] + origReport[i + 1:]
        return dampener(newReport, i+1, origReport)
        
safeCount = 0
for report in reports:
    if dampener(report, 0, report):
        safeCount += 1
        
print(f"Part2: {safeCount}")





