grid = { (i+j*1j):c for i, r in enumerate(open("test16.txt").readlines())
                    for j, c in enumerate(r.strip()) }
S, = [k for k, v in grid.items() if v == "S"]
E, = [k for k, v in grid.items() if v == "E"]

dir = 1j # facing east
seen = {(S, dir): 0} # (position, direction) : cost
paths = {(S, dir): 0} # tuples with position, direction, cost

"""
op ieder punt proberen we 3 dingen:
    1. rechtdoor
    2. linksaf
    3. rechtsaf
als die nieuwe locatie + richting al bestaat en de kosten doorvoor zijn lager dan de huidige kosten dan doen we niets.
anders updaten we seen en voegen een nieuw pad toe
"""
while paths:
    new_paths = {}
    for k, cost in paths.items():
        pos, dir = k
        for pos, dir, cost in ((pos + dir, dir, cost + 1), (pos + dir * 1j, dir * 1j, cost + 1001), (pos + dir * -1j, dir * -1j, cost + 1001)):
            if grid[pos] == "E" and (not (pos, dir) in seen or seen[pos, dir] >= cost):
                print(f"made it to E for {cost}")
                seen[(pos, dir)] = cost

            # if grid[pos] == "." and ((pos, dir) in seen and seen[pos, dir] == cost):
            #     print(f"we meet at {pos} for {cost}")

            if grid[pos] == "." and (not (pos, dir) in seen or seen[pos, dir] >= cost):
                seen[(pos, dir)] = cost
                new_paths[(pos, dir)] = cost

    paths = new_paths
