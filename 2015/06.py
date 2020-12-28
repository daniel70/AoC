import re
from collections import defaultdict

re_coordinates = re.compile(r"(.*?)(\d+),(\d+) through (\d+),(\d+)")
lines = []
grid1 = defaultdict(int)
grid2 = defaultdict(int)

with open("input06.txt") as f:
    for line in f:
        line = line.strip()
        m = re_coordinates.match(line)
        assert m is not None
        action, x1, y1, x2, y2 = m.groups()
        action: str = action.strip()
        x1: int = int(x1)
        x2: int = int(x2)
        y1: int = int(y1)
        y2: int = int(y2)

        for dx in range(x1, x2+1):
            for dy in range(y1, y2+1):
                idx = dx * 1_000 + dy
                if action == "turn on":
                    grid1[idx] = 1
                    grid2[idx] += 1
                elif action == "turn off":
                    grid1[idx] = 0
                    if grid2[idx] > 0:
                        grid2[idx] -= 1
                elif action == "toggle":
                    grid1[idx] = abs(grid1[idx] - 1)
                    grid2[idx] += 2
                else:
                    print("Invalid action")

print(sum(grid1.values()))
print(sum(grid2.values()))
