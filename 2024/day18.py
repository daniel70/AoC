import sys
from collections import defaultdict

sys.setrecursionlimit(10000)

file, first, size = "input18.txt", 1024, 70

lines = [line.strip() for line in open(file).readlines()]
bytes = []
for line in lines:
    i, j = map(int, line.split(","))
    bytes.append(i+j*1j)

pos = (0+0j)
seen = {pos: 0}
steps = 0
min_steps = defaultdict(tuple)


def walk(pos: complex, steps: int, bytes: list, trail: tuple):
    # print(f"now at: {pos} steps: {steps}")
    if len(bytes) in min_steps and len(trail) > len(min_steps[len(bytes)]):
        return

    if pos == (size+size*1j) and (len(bytes) not in min_steps or len(min_steps[len(bytes)]) > len(trail)):
        # print(f"done at: {pos} steps: {steps}")
        min_steps[len(bytes)] = trail

    for dir in [1, 1j, -1, -1j]:
        new = pos + dir
        if 0 <= new.real <= size and 0 <= new.imag <= size and new not in bytes and (new not in seen or seen[new] > steps) :
            seen[new] = steps
            walk(new, steps+1, bytes, trail + (new,))
    # return False

for i in range(1024, len(bytes)):
    seen = {pos: 0}
    print(f"working on {i}")

    if i - 1 not in min_steps or bytes[i] in min_steps[i-1]:
        walk(pos, 0, bytes[:i], (pos, ))
    else:
        min_steps[i] = min_steps[i-1]

    if i not in min_steps: # unable to find a solution
        break
# 56,27, line 2904


print("answer 1:", len(min_steps[1024]) - 1)
print("answer 2:", lines[max(min_steps)])
#21:42