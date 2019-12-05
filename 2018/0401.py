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
print(sleepy_guard * sleepy_minute)
