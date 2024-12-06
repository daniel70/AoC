reports = []
answer1 = answer2 = 0

lines = open(r"input02.txt").read().strip().split("\n")
for line in lines:
    reports.append([int(level) for level in line.split()])

def is_safe(report) -> bool:
    up = report[0] < report[1]
    for left, right in zip(report, report[1:]):
        if up and not (left < right <= left + 3):
            return False
        elif not up and not (left > right >= left - 3):
            return False
    return True


for report in reports:
    if is_safe(report):
        answer1 += 1
    for dampener in [report[:i] + report[i+1:] for i in range(len(report))]:
        if is_safe(dampener):
            answer2 += 1
            break

print("answer 1:", answer1)
print("answer 2:", answer2)
