disk_map = open("input09.txt").read().strip()

def checksum(fs: str) -> int:
    return sum([i*(ord(c)-100) for i, c in enumerate(fs) if c != '.'])


blocks = ""
id = 0
for i, c in enumerate(disk_map):
    if not i % 2:
        blocks += str(chr(id+100)) * int(c)
        id += 1
    else:
        blocks += "." * int(c)

answer1 = answer2 = blocks
for i in range(blocks.count('.')):
    answer1, c = answer1[:-1], answer1[-1]
    if c != ".":
        answer1 = answer1.replace('.', c, 1)

for id in range(id - 1, 0, -1):
    at = answer2.find(chr(id+100))
    cnt = answer2.count(chr(id+100))
    # find first cnt dots
    idx = answer2.find('.' * cnt, 0, at)
    if idx == -1:
        continue
    answer2 = answer2.replace(chr(id+100), '.')
    answer2 = answer2[:idx] + chr(id+100) * cnt + answer2[idx+cnt:]

print("answer 1:", checksum(answer1))
print("answer 2:", checksum(answer2))
