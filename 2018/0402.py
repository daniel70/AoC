import re
from collections import Counter, defaultdict

with open("input04.txt") as f:
    lines = f.readlines()

re_guard = re.compile("#(\d+)")
lines.sort()
guard, falls = None, None
schedule = defaultdict(list)
slept = Counter()
for line in lines:
    action = line[19:24]
    if action == "Guard":
        guard = int(re_guard.search(line).groups()[0])
    elif action == "falls":
        falls = int(line[15:17])
    elif action == "wakes":
        wakes = int(line[15:17])
        for i in range(falls, wakes):
            schedule[guard].append(i)
        slept[guard] += wakes - falls

sleepy_guard = slept.most_common(1)[0][0]
sleepy_minute = Counter(schedule[sleepy_guard]).most_common(1)[0][0]
print(
    f"most sleepy guard is #{sleepy_guard} in minute {sleepy_minute}, anwser: {sleepy_guard * sleepy_minute}"
)

most_frequent_minute = sorted(
    [(x, Counter(y).most_common(1)[0]) for x, y in schedule.items()],
    key=lambda x: x[1][1],
    reverse=True,
)[0]
print(
    f"guard #{most_frequent_minute[0]} slept most frequent in minute {most_frequent_minute[1][0]}, answer: {most_frequent_minute[0] * most_frequent_minute[1][0]}"
)
