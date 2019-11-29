import itertools as it
# changes = it.cycle(['+1', '-1'])
# changes = it.cycle(['+3', '+3', '+4', '-2', '-4'])
# changes = it.cycle(['-6', '+3', '+8', '+5', '-6'])
# changes = it.cycle(['7', '7', '-2', '-7', '-4'])
values = []
with open('input01.txt') as f:
    for line in f:
        values.append(int(line))
print(f'add {len(values)} lines')
changes = it.cycle(values)
seen = set()
change = 0
while change not in seen:
    seen.add(change)
    change += int(next(changes))

print(change)
