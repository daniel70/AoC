# code is a bit ugly, bots have values below 1000 and outputs just get added 1000, so they don't interfere with bots.

import re
from collections import defaultdict

two_digits = re.compile(r"(\d+).+?(\d+)")
three_digits = re.compile(r"(\d+).+(bot|output) (\d+).+(bot|output) (\d+)")

answer1 = None
giving = {}
holding = defaultdict(list)
horders = []

with open("input10.txt") as f:
    for line in f:
        line = line.strip()
        if line.startswith("value"):
            m = two_digits.search(line)
            holding[int(m[2])].append(int(m[1]))
        if line.startswith("bot"):
            m = three_digits.search(line)
            giving[int(m[1])] = [
                int(m[3]) + 1000 if m[2] == 'output' else int(m[3]),
                int(m[5]) + 1000 if m[4] == 'output' else int(m[5])
            ]

for bot, chips in holding.items():
    if len(chips) > 1:
        horders.append(bot)

while horders:
    for horder in horders[:]:
        for bot, chip in zip(giving[horder], sorted(holding[horder])):
            holding[bot].append(chip)
            if len(holding[bot]) == 2:
                horders.append(bot)
            if 17 in holding[bot] and 61 in holding[bot]:
                answer1 = bot

        holding[horder].clear()
        horders.remove(horder)

print("answer 1:", answer1)
print("answer 2:", holding[1000][0] * holding[1001][0] * holding[1002][0])
