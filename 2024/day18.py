file, first, size = "test18.txt", 12, 6
# file, first, size = "test18.txt", 12, 6

lines = [line.strip() for line in open(file).readlines()]
bytes = set()
for line in lines[:first]:
    i, j = map(int, line.split(","))
    bytes.add(i+j*1j)

pos = (0+0j)
seen = {pos}
steps = 0

def walk(pos, steps):
    print(f"now at: {pos} steps: {steps}")
    steps + 1
    if pos == (size+size*1j):
        print(f"done at: {pos} steps: {steps}")
        return True
    for dir in [1, -1, 1j, -1j]:
        new = pos + dir
        if 0 <= new.real <= size and 0 <= new.imag <= size and new not in seen and new not in bytes:
            seen.add(new)
            walk(new, steps+1)
    return False

print(walk(pos, 0))
