track = { i+1j*j: c for i, line in enumerate(open("input20.txt").read().splitlines())
                    for j, c in enumerate(line)}

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

# build all reachable points from origin
points = {}
for x in range(-20, +21):
    for y in range(abs(x)-20,21-abs(x)):
        points[complex(x, y)] = abs(x) + abs(y)

answer1 = 0
answer2 = 0
set_path = set(path)
for i, pos in enumerate(path):
    new_points = {pos + k: v for k, v in points.items()}
    for end_pos, distance in new_points.items():
        if end_pos in path and path.index(end_pos) - i - distance >= 100:
            answer2 += 1
            if distance == 2:
                answer1 += 1

print("answer 1:", answer1)
print("answer 2:", answer2)
