
reports = []

with open("day2.input", "r") as file:
    for line in file:
        parts = line.strip().split(" ")
        reports.append([int(p) for p in parts])

def processReport(report):
    increasing = []
    for prev, cur in zip(report, report[1:]):
        if not abs(cur - prev) in range(1,4):
            return False
        elif cur == prev:
            return False
        else:
            increasing.append(cur > prev)

    return len(set(increasing)) == 1

print(f"Part1: {sum(1 for report in reports if processReport(report))}")


def dampener(report, i, origReport):
    if processReport(report):
        return True
    elif i > len(report):
        return False
    else:
        newReport = origReport[:i] + origReport[i + 1:]
        return dampener(newReport, i+1, origReport)
        
print(f"Part2: {sum(1 for report in reports if dampener(report, 0, report))}")