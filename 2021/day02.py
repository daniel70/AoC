import re

course = []
recom = re.compile(r"(\w+)\s+(\d+)")

with open('input02.txt') as f:
    for line in f:
        m = recom.match(line)
        if m:
            course.append(m.groups())

x = y = 0
for direction, length in course:
    length = int(length)
    match direction:
        case 'forward':
            x += length
        case 'up':
            y -= length
        case 'down':
            y += length

print('puzzle 1:', x * y)

x = y = aim = 0
for direction, length in course:
    length = int(length)
    match direction:
        case 'forward':
            x += length
            y += aim * length
        case 'up':
            aim -= length
        case 'down':
            aim += length

print('puzzle 2:', x * y)
