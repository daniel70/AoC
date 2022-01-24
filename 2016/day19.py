from collections import deque
elfs = 3017957
# elfs = 5

table = []
for elf in range(1, elfs + 1):
    table.append(elf)

q = deque(table)
while len(q) > 1:
    q.append(q.popleft())
    q.popleft()

print(q)
print("done")