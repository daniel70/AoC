"""
Advent of Code 2019, day 6, puzzle 2
From YOU to COM => ['YOU', 'K', 'J', 'E', 'D', 'C', 'B', 'COM']
From SAN to COM => ['SAN', 'I', 'D', 'C', 'B', 'COM']
The answer is the number of planets between YOU and the common ancestor (D), which is 3
Plus the number of planets between SAN and the common ancestor (D), which is 1.
The test answer is therefore 4 (3 + 1)
"""
# lines = [
#     "COM)B",
#     "B)C",
#     "C)D",
#     "D)E",
#     "E)F",
#     "B)G",
#     "G)H",
#     "D)I",
#     "E)J",
#     "J)K",
#     "K)L",
#     "K)YOU",
#     "I)SAN"
# ]

lines = []
with open("input06.txt") as f:
    for line in f:
        lines.append(line.strip())

planet_pairs = set()
for s in lines:
    planet_pairs.add(tuple(s.split(")")))

# from YOU to COM
YOU = ["YOU",]
while "COM" not in YOU:
    for a, b in planet_pairs:
        if b in YOU and a not in YOU:
            YOU.append(a)
            break

# from SAN to COM
SAN = ["SAN",]
while "COM" not in SAN:
    for a, b in planet_pairs:
        if b in SAN and a not in SAN:
            SAN.append(a)
            break

# Find first common ancestor planet
for planet in SAN:
    if planet in YOU:
        break

san, you = SAN.index(planet) - 1, YOU.index(planet) - 1
print(f"Found {planet} in SAN at {san} and in YOU at {you}, SUM = {san + you}")