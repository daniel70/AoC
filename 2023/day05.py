import re

maps: list[dict[range, int]] = []
with open("input05.txt") as file:
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


answer1 = []
for seed in seeds:
    for m in maps:
        for k, v in m.items():
            if seed in k:
                seed += v
                break
    answer1.append(seed)

seeds = [range(left, left + right) for left, right in zip(seeds[::2], seeds[1::2])]
for map in maps:
    new_seeds: list[range] = []
    for seed in sorted(seeds, key=lambda r: r.start):
        for r in sorted(map, key=lambda r: r.start):
            if seed.stop < r.start:
                new_seeds.append(seed)
                seed = range(0, 0)
                break
            if seed.start in r:
                offset = map[r]
                if seed.stop in r:
                    new_seeds.append(range(seed.start + offset, seed.stop + offset))
                    seed = range(seed.stop, seed.stop)
                    break
                else:
                    new_seeds.append(range(seed.start + offset, r.stop + offset))
                    seed = range(r.stop, seed.stop)
            elif seed.stop in r:
                offset = map[r]
                new_seeds.append(range(r.start + offset, seed.stop + offset))
                seed = range(seed.start, r.start)

        if len(seed) > 0:
            new_seeds.append(seed)

    seeds = new_seeds

print("answer 1:", min(answer1))
print("answer 2:", min([s.start for s in seeds]))
