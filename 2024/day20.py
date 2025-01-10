from collections import Counter

track = { i+1j*j: c for i, line in enumerate(open("input20.txt").read().splitlines())
                    for j, c in enumerate(line)}

start = [k for k, v in track.items() if v == 'S'][0]
end = [k for k, v in track.items() if v == 'E'][0]

def distance(pos, track, cheat=None):
    print("let's go")
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
    todo = [(pos, ())]
    for pos, path in todo:
        if pos == end:
            return path

        for new in [pos+1, pos-1, pos+1j, pos-1j]:
            if new in track and track[new] != '#' and new not in seen:
                todo.append((new, path + (new,)))
                seen.add(new)

# track[end+1j] = '.'
# track[(1+8j)] = '.'
path = solve(start, track)

# voor iedere stap, probeer een cheat te vinden en los de puzzel opnieuw op
cheats = set()
for pos in path:
    for p1, p2 in ((pos+1, pos+2), (pos-1, pos-2), (pos+1j, pos+2j), (pos-1j, pos-2j)):
        if p2 in track and track[p1] == "#" and track[p2] in [".", "E", "S"]:
            cheats.add((p1, p2))

cheats = set([c1 for c1, c2 in cheats])
saves = {cheat: distance(start, track.copy(), cheat) for cheat in cheats}
c = Counter([len(path) - len(save) for save in saves.values()])
print("answer 1:", len([save for save in saves.values() if len(path) - save >= 100]))