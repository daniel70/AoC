aria = {(i + j * 1j): int(c) for i, line in enumerate(open("input10.txt").readlines())
                             for j, c in enumerate(line.strip())}
seen = {step: [] for step in range(10)}
seen[0] = ([[pos,] for pos, height in aria.items() if height == 0])

for round in range(10):
    for path in seen[round]:
        for dir in [-1, 1j, 1, -1j]:
            if aria.get(path[-1] + dir) == round + 1:
                seen[round+1].append(path + [path[-1] + dir])

print("answer 1:", len({(path[0], path[-1]) for path in seen[9]}))
print("answer 2:", len(seen[9]))
