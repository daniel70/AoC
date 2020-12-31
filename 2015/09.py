from itertools import permutations

routes = {}
costs = {}
locations = set()

with open("input09.txt") as f:
    for line in f:
        line = line.strip()
        cities, distance = line.split(" = ")
        from_, to = cities.split(" to ")
        locations.add(from_)
        locations.add(to)
        routes[(from_, to)] = int(distance)
        routes[(to, from_)] = int(distance)

all_routes = permutations(locations, len(locations))

for route in all_routes:
    distance = 0
    for dep, arr in zip(route, route[1:]):
        distance += routes[(dep, arr)]

    costs[route] = distance

short = [v for v in sorted(costs, key=costs.get)][0]
long = [v for v in sorted(costs, key=costs.get, reverse=True)][0]
print(costs[short])
print(costs[long])