from collections import defaultdict
from pprint import pprint

mfscam = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

sues = defaultdict(dict)
with open('input16.txt') as f:
    for line in f:
        if not line:
            continue
        sue, props = line.strip().split(":", 1)
        for prop in props.split(","):
            key, val = prop.split(":", 1)
            sues[int(sue[4:])][key.strip()] = int(val)

for sue, props in sues.items():
    for key, val in props.items():
        if mfscam[key] != val:
            break
    else:
        print('answer 1:', sue)

for sue, props in sues.items():
    for key, val in props.items():
        if key in ["cats", "trees"]:
            if mfscam[key] >= val:
                break

        elif key in ["pomeranians", "goldfish"]:
            if mfscam[key] <= val:
                break

        elif mfscam[key] != val:
            break
    else:
        print('answer 2:', sue)
