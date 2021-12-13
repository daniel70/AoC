from collections import Counter, defaultdict

lines = []
start = []
small_caves = set()
counter = Counter()
cave_map = defaultdict(list)


def is_lower(s):
    if s in ["start", "end"]:
        return False
    return not "A" <= s[0] <= "Z"


def path_finder(cave, small, path = []):
    path.append(cave)
    if cave == "end":
        return path

    for c in [c for c in cave_map[cave] if (not is_lower(c) or c in small)]:
        if c in small:
            small.remove(c)
        path_finder(c, small, path)

    return path

with open('test12.txt') as f:
    for line in f:
        line = line.strip()
        l, r = line.split("-")
        if l == "start":
            start.append(r)
        elif r == "start":
            start.append(l)
        else:
            lines.append((l, r))
        counter[l] += 1
        counter[r] += 1
        if r != "start":
            cave_map[l].append(r)
        if l != "start":
            cave_map[r].append(l)

# remove small caves that occur only once
# in combination with another small cave
# and therefore can't be accessed
for cave, count in counter.items():
    if count == 1:
        for path in lines:
            if all(is_lower(p) for p in path) and cave in path:
                print(f"removing small cave {path}")
                lines.remove(path)

# find all small caves that that are left
for l, r in lines:
    if is_lower(l):
        small_caves.add(l)
    if is_lower(r):
        small_caves.add(r)

for s in cave_map["start"]:
    paths = path_finder(s, small_caves, ["start"])
    print(paths)