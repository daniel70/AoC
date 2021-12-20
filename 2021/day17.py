import re
from itertools import count

with open("input17.txt") as f:
    line = f.readline().strip()
x1, x2, y1, y2 = map(int, re.findall(r"[-]?\d+", line))
# x1, x2, y1, y2 = 20, 30, -10, -5

hor = []
t = 0
for i in count():
    t += i
    if x1 <= t <= x2:
        hor.append(i)
    if t > x2:
        break

# na 6 of 7 stappen op -5 .. -10
ver = []
y = 162
t = 0
for i in range(1, 400):
    ver.append(t + y)
    t = t + y
    y -= 1
