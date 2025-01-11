import time
from collections import Counter

track = { i+1j*j: c for i, line in enumerate(open("input20.txt").read().splitlines())
                    for j, c in enumerate(line)}

t = time.monotonic()
start = [k for k, v in track.items() if v == 'S'][0]
end = [k for k, v in track.items() if v == 'E'][0]


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
walls = set()
for i, pos in enumerate(path):
    for p1, p2 in ((pos+1, pos+2), (pos-1, pos-2), (pos+1j, pos+2j), (pos-1j, pos-2j)):
        if p2 in track and track[p1] == "#" and track[p2] in [".", "E", "S"]:
            if p1 not in walls:
                walls.add(p1)
                cheats[(pos, p2)] = i

saves = {}
for k, path_idx in cheats.items():
    p1, p2 = k
    saves[k] = path.index(p2) - path_idx - 2

# op ieder punt in path wordt bepaald welke punten ná het huidige punt in path bereikbaar zijn binnen 20 stappen
# cheats =
# for i, pos in enumerate(path):


c = Counter(saves.values())
print("answer 1:", len([save for save in saves.values() if save >= 100]))
# print("answer 1:", len([save for save in saves.values() if len(path) - save >= 100]))
print(c)
print("duration:", time.monotonic() - t)
