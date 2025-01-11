import time
from collections import Counter

track = { i+1j*j: c for i, line in enumerate(open("input20.txt").read().splitlines())
                    for j, c in enumerate(line)}

t = time.monotonic()
start = [k for k, v in track.items() if v == 'S'][0]
end = [k for k, v in track.items() if v == 'E'][0]

def distance(pos, track, cheat=None):
    if cheat:
        track[cheat] = "."

    seen = set()
    todo = [(pos, 0)]
    for pos, dist in todo:
        if pos == end:
            return dist

        for new in [pos+1, pos-1, pos+1j, pos-1j]:
            if new in track and track[new] != '#' and new not in seen:
                todo.append((new, dist+1))
                seen.add(new)

def solve(pos, track):
    seen = set()
    todo = [(pos, (pos,))]
    for pos, path in todo:
        if pos == end:
            return path

        for new in [pos+1, pos-1, pos+1j, pos-1j]:
            if new in track and track[new] != '#' and new not in seen:
                todo.append((new, path + (new,)))
                seen.add(new)

path = solve(start, track)

cheats = {}
for i, pos in enumerate(path):
    for p1, p2 in ((pos+1, pos+2), (pos-1, pos-2), (pos+1j, pos+2j), (pos-1j, pos-2j)):
        if p2 in track and track[p1] == "#" and track[p2] in [".", "E", "S"]:
            cheats[(p1, p2)] = i

# cheats = set([c1 for c1, c2 in cheats])
# saves = {cheat: distance(start, track.copy(), cheat) for cheat, cheato in cheats}
saves = {}
for k, path_idx in cheats.items():
    p1, p2 = k
    if p2 not in path:
        print(f"{p2=} not in path")
        continue
    saves[p1] = path_idx - path.index(p2) - 2



c = Counter([len(path) - save for save in saves.values()])
print("answer 1:", len([save for save in saves.values() if save >= 100]))
# print("answer 1:", len([save for save in saves.values() if len(path) - save >= 100]))
print(c)
print("duration:", time.monotonic() - t)
