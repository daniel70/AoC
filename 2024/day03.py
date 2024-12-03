import re
mul = re.compile(r"mul\((\d+),(\d+)\)")
total = 0
data = open(r".\2024\input03.txt").read().strip().split("\n")
for line in data:
    matches = mul.findall(line)
    if matches is None:
        print("nothing here")
        continue
    for left, right in matches:
        total += int(left) * int(right)


print(total)