"""
Advent of Code 2019, day 6, puzzle 2
"""
lines = [
    "COM)B",
    "B)C",
    "C)D",
    "D)E",
    "E)F",
    "B)G",
    "G)H",
    "D)I",
    "E)J",
    "J)K",
    "K)L",
    "K)YOU",
    "I)SAN"
]

lines = []
with open("input06.txt") as f:
    for line in f:
        lines.append(line.strip())

planet_pairs = set()
for s in lines:
    planet_pairs.add(tuple(s.split(")")))

# from YOU to COM
YOU = []
a, b = None, "YOU"
while a != "COM":
    for i, j in planet_pairs:
        if j == b:
            YOU.append(i)
            a = i
            b = i
            break

# from SAN to COM
SAN = []
a, b = None, "SAN"
while a != "COM":
    for i, j in planet_pairs:
        if j == b:
            SAN.append(i)
            a = i
            b = i
            break

for a in SAN:
    if a in YOU:
        break

print(f"Found {a} in SAN at {SAN.index(a)} and in YOU at {YOU.index(a)}, SUM = {SAN.index(a) + YOU.index(a)}")