lab = {}
for i, line in enumerate(open('input06.txt').readlines()):
    for j, char in enumerate(line.strip()):
        lab[i + j * 1j] = char
        if char == "^":
            start = i + j * 1j


def walk(lab):
    dir, pos, seen = -1, start, set()
    while pos in lab and (pos, dir) not in seen:
        seen |= {(pos, dir)}
        if lab.get(pos+dir) == "#":
            dir *= -1j # rotate 90º
            continue
        pos += dir
    return pos in lab, {pos for pos, dir in seen}

is_loop, path = walk(lab)
answer1 = len(path)
answer2 = sum(walk(lab | {pos: "#"})[0] for pos in path)

print("answer 1:", answer1)
print("answer 2:", answer2)
