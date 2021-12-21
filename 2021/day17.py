import re
with open("input17.txt") as f:
    line = f.readline().strip()

x1, x2, y1, y2 = map(int, re.findall(r"[-]?\d+", line))
heighest = 0
hit = set()
for x in range(x2 + 1):
    for y in range(y1, abs(y1)):
        x_distance = y_distance = 0
        x_velocity = x
        y_velocity = y
        while x_distance <= x2:
            x_distance += x_velocity
            if x_velocity > 0:  # no negative speed
                x_velocity -= 1
            y_distance += y_velocity
            heighest = max(y_distance, heighest)
            y_velocity -= 1
            if x1 <= x_distance <= x2 and y1 <= y_distance <= y2:
                hit.add((x, y))

            if y_distance < y1:
                break

print("answer 1:", heighest)
print("answer 2:", len(hit))
