import sys

sys.setrecursionlimit(10000)
file, first, size = "input18.txt", 1024, 70
lines = [line.strip() for line in open(file).readlines()]
bytes = []
for line in lines:
    i, j = map(int, line.split(","))
    bytes.append(i+j*1j)

pos = (0+0j)
seen = {pos: 0}
min_steps = {}


def walk(pos: complex, bytes: list, trail: tuple):
    if len(bytes) in min_steps and len(trail) > len(min_steps[len(bytes)]):
        return

    if pos == (size+size*1j) and (len(bytes) not in min_steps or len(min_steps[len(bytes)]) > len(trail)):
        min_steps[len(bytes)] = trail

    for dir in [1, 1j, -1, -1j]:
        new = pos + dir
        if 0 <= new.real <= size and 0 <= new.imag <= size and new not in bytes and (new not in seen or seen[new] > len(trail)) :
            seen[new] = len(trail)
            walk(new, bytes, trail + (new,))


for i in range(1024, len(bytes)):
    print(f"working on {i}")
    seen = {pos: 0}

    if i - 1 not in min_steps or bytes[i] in min_steps[i-1]:
        walk(pos, bytes[:i], (pos, ))
    else:
        min_steps[i] = min_steps[i-1]

    if i not in min_steps: # unable to find a solution
        break

print("answer 1:", len(min_steps[1024]) - 1)
print("answer 2:", lines[max(min_steps)])
