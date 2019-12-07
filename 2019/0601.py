"""
Advent of Code 2019, day 6, puzzle 1
COM is the first center planet to look for, it has 0 points.
Every time we find a planet in orbit to a planet we already found
we add it to the planet_points dict with the number of points.
Each iteration adds one point.
Planets that are added to planet_points are removed from the set of planet pairs.
Finally we sum the number of points.
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
# ]
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
    for center, orbit in planet_pairs:
        if center in planet_points:
            found.add((center, orbit))

    for _, orbit in found:
        planet_points[orbit] = points

    planet_pairs = planet_pairs - found

print(sum(planet_points.values()))
