import re
from itertools import count
from collections import defaultdict

with open("input17.txt") as f:
    line = f.readline().strip()
# x1, x2, y1, y2 = map(int, re.findall(r"[-]?\d+", line))
x1, x2, y1, y2 = 85, 145, -163, -108
# x1, x2, y1, y2 = 20, 30, -10, -5

x_steps = defaultdict(list)
x_stops = []
x_steps_set = set()

for x in range(1, x2 + 1):
    distance = 0
    velocity = x
    for step in count(1):
        if velocity < 0:
            break
        distance += velocity
        if x1 <= distance <= x2:
            x_steps[x].append(step)
            if velocity == 0:
                x_stops.append(x)
        velocity -= 1


# make a set of all possible steps that are not in stops
x_steps_set = set(item for x, sublist in x_steps.items() for item in sublist if x not in x_stops)

y_steps = defaultdict(list)
for y in count(y1):
    distance = 0
    velocity = y
    found = False
    for step in x_steps_set:
        distance += velocity
        if y1 <= distance <= y2:
            found = True
            y_steps[y].append(step)
        velocity -= 1

    if not found:
        break

# find all normal cases of the initial_velocities
normal_velocities = set()
for x, xs in x_steps.items():
    for x_step in xs:
        for y, ys in y_steps.items():
            if x_step in ys:
                normal_velocities.add((x, y))

# find all special cases where the x-velocity stops in the target area (x_stops)
max_height = 0
special_velocities = set()
for x in x_stops:
# for x in range(10, 30):
    for i, y in enumerate(range(abs(y1))):
        distance = 0
        velocity = y
        for z in count(1):
            distance += velocity
            max_height = max(distance, max_height)
            if y1 <= distance <= y2:  # and z >= min(x_steps[x]):
                special_velocities.add((x, y))
            velocity -= 1

            if velocity < y1:
                break

initial_velocities = normal_velocities.union(special_velocities)
print("answer 2:", len(initial_velocities))
print(f"{max_height=}")
# 3964 is too low
