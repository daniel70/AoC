from collections import defaultdict

grid = { (i+j*1j):c for i, r in enumerate(open("input16.txt").readlines())
                    for j, c in enumerate(r.strip()) }
S, = [k for k, v in grid.items() if v == "S"]
E, = [k for k, v in grid.items() if v == "E"]

dir = 1j # facing east
seen = {(S, dir): 0} # (position, direction) : cost
paths = {(S, dir): 0} # tuples with position, direction, cost

while paths:
    new_paths = {}
    for k, cost in paths.items():
        pos, dir = k
        for pos, dir, cost in ((pos + dir, dir, cost + 1), (pos + dir * 1j, dir * 1j, cost + 1001), (pos + dir * -1j, dir * -1j, cost + 1001)):
            if grid[pos] == "E" and (not (pos, dir) in seen or seen[pos, dir] >= cost):
                seen[(pos, dir)] = cost

            if grid[pos] == "." and (not (pos, dir) in seen or seen[pos, dir] >= cost):
                seen[(pos, dir)] = cost
                new_paths[(pos, dir)] = cost

    paths = new_paths

answer1 = min([v for k, v in seen.items() if k[0] == E])
print("answer 1:", answer1)

def calc_cost(path):
    cost = 0
    for p1, p2 in zip(path, path[1:]):
        if p1[1] == p2[1]:
            cost += 1
        else:
            cost += 1001
    return cost


dir = 1j # facing east
seen = {} # (position, direction) : cost
paths = [[(S, dir)]] # tuples with position, direction, cost
finished = []
while paths:
    new_paths = []
    for path in paths:
        pos, dir = path[-1]
        for pos, dir in ((pos + dir, dir), (pos + dir * 1j, dir * 1j), (pos + dir * -1j, dir * -1j)):
            if grid[pos] == "E":
                path.append((pos, dir))
                seen[(pos, dir)] = calc_cost(path)
                finished.append(path)
            if grid[pos] == ".": # and path + [(pos, dir)] not in paths
                if any([p for p, _ in path if p == pos]):
                    continue

                elif calc_cost(path + [(pos, dir)]) > answer1:
                    continue

                elif (pos, dir) in seen and seen[(pos, dir)] < (calc_cost(path) - 1001):
                    continue

                else:
                    new_paths.append(path + [(pos, dir)])
                    seen[(pos, dir)] = calc_cost(path)

    paths = new_paths

costs = defaultdict(set)

for path in finished:
    costs[calc_cost(path)] |= set([p[0] for p in path])

print("answer 2: ", len(costs[min(costs)]))