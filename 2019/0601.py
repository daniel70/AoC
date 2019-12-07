"""
Advent of Code 2019, day 6, puzzle 1
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
]
lines = []
with open("input06.txt") as f:
    for line in f:
        lines.append(line.strip())

planet_pairs = set()
for s in lines:
    planet_pairs.add(tuple(s.split(")")))

planet_points = {"COM": 0}
points = 0
while planet_pairs:
    found = set()
    points += 1
    for a, b in planet_pairs:
        if a in planet_points:
            found.add((a, b))

    for _, b in found:
        planet_points[b] = points

    planet_pairs = planet_pairs - found

print(sum(planet_points.values()))
