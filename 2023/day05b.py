import re

maps: list[dict[range, int]] = []
with open("test05.txt") as file:
    seeds = [int(n) for n in re.findall(r"\d+", file.readline())]
    for line in file:
        line = line.strip()
        if not line:
            continue
        if line.endswith("map:"):
            maps.append(dict())
        else:
            d, s, r = [int(n) for n in re.findall(r"\d+", line)]
            maps[-1][range(s, s + r)] = d - s

# sort the maps
sorted_maps = []
for m in maps:
    sorted_maps.append(sorted(m, key=lambda k: k.start))

answer2 = []
ranges = sorted([range(s, s + r) for s, r in zip(seeds[::2], seeds[1::2])], key=lambda k: k.start)
for r in ranges:
    print(r)
    new_ranges = []
    for m, v in sorted_maps[0].items():
        if m.start <= r.start and m.stop >= r.stop:
            # r is contained
            new_ranges[range(r.start, r.stop)] = v

print(new_ranges)
