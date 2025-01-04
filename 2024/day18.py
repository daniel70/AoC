from collections import defaultdict
import sys
sys.setrecursionlimit(10000)

# file, first, size = "test18.txt", 12, 6
file, first, size = "input18.txt", 1024, 70

lines = [line.strip() for line in open(file).readlines()]
bytes = set()
for line in lines[:first]:
    i, j = map(int, line.split(","))
    bytes.add(i+j*1j)

pos = (0+0j)
seen = {pos: 0}
steps = 0
best = 1_000_000

def walk(pos, steps):
    global best
    # print(f"now at: {pos} steps: {steps}")
    steps + 1
    if pos == (size+size*1j):
        print(f"done at: {pos} steps: {steps}")
        best = min(best, steps)

    for dir in [1, -1, 1j, -1j]:
        new = pos + dir
        if 0 <= new.real <= size and 0 <= new.imag <= size and new not in bytes and (new not in seen or seen[new] > steps) :
            seen[new] = steps
            walk(new, steps+1)
    # return False

walk(pos, 0)
print("answer 1:", best)
