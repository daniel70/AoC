from collections import defaultdict

lines = []
small_caves = set()
cave_map = defaultdict(list)


def is_lower(s):
    if s in ["start", "end"]:
        return False
    return not "A" <= s[0] <= "Z"


def path_finder(cave, small, path, twice=True):
    paths = []
    if cave == "end":
        # print(f"{path=} {small=}")
        return [path]
    else:
        for c in [c for c in cave_map[cave] if (not is_lower(c) or c in small)]:
            if c in small:
                if twice:
                    paths += path_finder(c, small, path + [c], False)
                paths += path_finder(c, small - {c}, path + [c], twice)
            else:
                paths += path_finder(c, small, path + [c], twice)

    return paths


with open('input12.txt') as f:
    for line in f:
        line = line.strip()
        l, r = line.split("-")
        if r != "start":
            cave_map[l].append(r)
        if l != "start":
            cave_map[r].append(l)
        if is_lower(l):
            small_caves.add(l)
        if is_lower(r):
            small_caves.add(r)

for a in range(1, 3):
    paths = path_finder("start", small_caves, ["start"], [False, True][a-1])
    uq_paths = []
    for path in paths:
        if path not in uq_paths:
            uq_paths.append(path)

    print(f"answer {a}:", len(uq_paths))
