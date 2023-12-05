import re

seeds = (79, 14)

maps = [
    {
        range(98, 100): -48,
        range(50, 98): 2,
    },
    {
        range(15, 15 + 37): -15,
        range(52, 52 + 2): -15,
        range(0, 15): 39,
    },
]


maps = []
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
    # print(f"{seed} -> ", end="")
    for m in maps:
        for k, v in m.items():
            if seed in k:
                seed += v
                break
        # print(f"{seed} -> ", end="")

    # print(seed)
    answer1.append(seed)

answer2 = []
for r in [range(s, s + r) for s, r in zip(seeds[::2], seeds[1::2])]:
    for seed in r:
        # print(f"{seed} -> ", end="")
        for m in maps:
            for k, v in m.items():
                if seed in k:
                    seed += v
                    break
            # print(f"{seed} -> ", end="")

        # print(seed)
        answer2.append(seed)

print("answer 1:", min(answer1))
print("answer 2:", min(answer2))
