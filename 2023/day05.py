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


def mapping(seeds, maps):
    for map in maps:
        new_seeds: list[range] = []
        for seed in sorted(seeds, key=lambda r: r.start):
            for map_range in sorted(map, key=lambda r: r.start):
                if seed.stop < map_range.start:
                    new_seeds.append(seed)
                    seed = range(0, 0)
                    break
                if seed.start in map_range:
                    offset = map[map_range]
                    if seed.stop in map_range:
                        new_seeds.append(range(seed.start + offset, seed.stop + offset))
                        seed = range(seed.stop, seed.stop)
                        break
                    else:
                        new_seeds.append(
                            range(seed.start + offset, map_range.stop + offset)
                        )
                        seed = range(map_range.stop, seed.stop)
                elif seed.stop in map_range:
                    offset = map[map_range]
                    new_seeds.append(
                        range(map_range.start + offset, seed.stop + offset)
                    )
                    seed = range(seed.start, map_range.start)

            if len(seed) > 0:
                new_seeds.append(seed)

        seeds = new_seeds
    return min([s.start for s in seeds])


print("answer 1:", mapping([range(seed, seed + 1) for seed in seeds], maps))
print(
    "answer 2:",
    mapping(
        [range(left, left + right) for left, right in zip(seeds[::2], seeds[1::2])],
        maps,
    ),
)
