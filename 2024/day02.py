reports = []
lines = open(r".\2024\test02bad.txt").read().strip().split("\n")
for line in lines:
    reports.append([int(level) for level in line.split()])

answer1 = 0
answer2 = 0

def save_report(report) -> int:
    """
    If the report is save -> return 0
    else return the number of the offending level
    """
    up = report[0] < report[1]
    index = 0
    for left, right in zip(report, report[1:]):
        index += 1
        if up and not (left < right <= left + 3):
            return index
        elif not up and not (left > right >= left - 3):
            return index
    
    return 0

# def safe2(report):
#     return any(save_report(reports[:i] + reports[i + 1:]) for i in range(len(reports)))

# print(sum(safe2(reports) for reports in lines))

for i, report in enumerate(reports):
    print(i, report, end=" ")
    result = save_report(report)
    if result == 0:
        answer1 += 1
        answer2 += 1
        print("Safe without removing any level")
        continue
    result_without_first_element = save_report(report[1:])
    if result_without_first_element == 0:
        answer2 += 1
        print("Safe by removal of first element")
        continue
    popped = report.pop(result)
    popped_index = result
    # print(f"Removing {popped}")
    result = save_report(report)
    if result == 0:
        answer2 += 1
        print(f"Safe after removal of {popped} (idx={popped_index})")
        continue

    print(f"Bad idx1:{popped_index} idx2:{result}")

print(answer1)
print(answer2)
# 323 too low, because error in 0
# 611 too high
# 340 too low