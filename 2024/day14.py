import math
import re
nrs = re.compile(r"[\d-]+")

grid = []
for line in open("input14.txt").readlines():
    px, py, vx, vy = nrs.findall(line)
    grid.append((int(px)+int(py)*1j,int(vx)+int(vy)*1j))

w, h = 101, 103
round = 0
two = False
while True:
    round += 1
    temp = []
    for p, v in grid:
        p += v
        q = p.real % w + p.imag % h * 1j
        temp.append((q, v))
    grid = temp
    positions = [p for p, _ in grid]

    if round == 100:
        quadrants = [[], [], [], []]
        for p in positions:
            x, y = p.real, p.imag
            if x < w // 2 and y < h // 2:
                quadrants[0].append(p)
            elif x > w // 2 and y < h // 2:
                quadrants[1].append(p)
            elif x < w // 2 and y > h // 2:
                quadrants[2].append(p)
            elif x > w // 2 and y > h // 2:
                quadrants[3].append(p)
        print("answer 1:", math.prod(len(q) for q in quadrants))

    for p in positions:
        if all([p+i in positions for i in range(1, 8)]):
            print("answer 2:", round)
            two = True
            break

    if two: break
