reports = []
answer1 = answer2 = 0

lines = open(r".\2024\input02.txt").read().strip().split("\n")
for line in lines:
    reports.append([int(level) for level in line.split()])

def save_report(report) -> bool:
    """
    If the report is save -> return 0
    else return the number of the offending level
    """
    up = report[0] < report[1]
    for left, right in zip(report, report[1:]):
        if up and not (left < right <= left + 3):
            return False
        elif not up and not (left > right >= left - 3):
            return False
    
    return True


for report in reports:
    if save_report(report):
        answer1 += 1
        answer2 += 1
    else:
        for dampener in [report[:i] + report[i+1:] for i in range(len(report))]:
            if save_report(dampener):
                answer2 += 1
                break

print(answer1)
print(answer2)
