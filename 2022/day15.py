import re
goal = 2_000_000
nearby = 4_000_000
md = lambda s, b: int(abs(s.real - b.real) + abs(s.imag - b.imag))
positions = set()
beacons = {}
scanners = {}
with open("input15.txt") as f:
    for line in f:
        x1, y1, x2, y2 = [int(p) for p in re.findall(r"-?\d+", line.strip())]
        beacons[complex(int(x1), int(y1))] = complex(int(x2), int(y2))
        scanners[(x1, y1)] = abs(x1 - x2) + abs(y1 - y2)


def signals_in_line(sensor: complex, man_dist: int, line: int) -> set:
    dist_from_line = man_dist - int(abs(sensor.imag - line))
    start = int(sensor.real - dist_from_line)
    end = int(sensor.real + dist_from_line)
    return set(range(start, end + 1))


def signals_in_range(sensor: complex, man_dist: int, line: int) -> set:
    dist_from_line = man_dist - int(abs(sensor.imag - line))
    start = int(sensor.real - dist_from_line)
    end = int(sensor.real + dist_from_line)
    return set(range(start, end + 1))


for sensor, beacon in beacons.items():
    distance = md(sensor, beacon)
    positions |= signals_in_line(sensor, distance, goal)

beacons_in_line = set(int(p.real) for p in beacons.values() if p.imag == goal)
print("answer 1:", len(positions - beacons_in_line))

# only one point in the grid is not found by the scanner
# this means the scanners *just* can't reach it, otherwise there would be more points
# the shape of the scanned area is rectangular where the sides have a slope of +1 and -1
# now, find two lines that, if they move one up or one down, overlap
# take the intersection point and check that none of the scanners can reach it
# that is the answer:

pos, neg = list(), list()
for point, dist in scanners.items():
    x, y = point
    pos.append(y - x + dist + 1)
    pos.append(y - x - dist - 1)
    neg.append(y + x + dist + 1)
    neg.append(y + x - dist - 1)

# only take overlapping lines into consideration
pos = set(p for p in pos if pos.count(p) > 1)
neg = set(p for p in neg if neg.count(p) > 1)

for up in pos:
    for down in neg:
        x, y = (down - up) // 2, (down + up) // 2  # the intersection of both lines
        if all(0 <= i <= nearby for i in [x, y]):  # make sure the point is in the grid
            # and that none of the scanners can reach it
            if all(abs(x - scanner[0]) + abs(y - scanner[1]) > dist for scanner, dist in scanners.items()):
                print("answer 2:", (x * 4_000_000) + y)
