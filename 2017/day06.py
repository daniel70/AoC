cycles = 0
banks = [int(x) for x in open("input06.txt").read().split()]
seen = {}
while tuple(banks) not in seen.keys():
    seen[(tuple(banks))] = cycles
    cycles += 1
    start = banks.index(max(banks))
    for idx in range(banks[start] + 1):
        if idx == 0:
            banks[start] = 0
            continue
        banks[(start + idx) % len(banks)] += 1

print("answer 1:", len(seen))
print("answer 2:", len(seen) - seen[tuple(banks)])
