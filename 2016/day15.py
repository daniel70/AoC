import itertools as it
import re
nrs = re.compile(r"\d+")
lines = []
with open("input15.txt") as f:
    for line in f:
        line = line.strip()
        lines.append(list(map(int, re.findall(nrs, line))))


def time(discs):
    for c in it.count(0):
        if all(disc[2] == 0 for disc in discs):
            return c
        for disc in discs:
            disc[2] = (disc[2] + 1) % disc[1]


def main():
    # set the starting position to zero for each disk
    discs = [[idx, arms, (pos + idx) % arms] for idx, arms, _, pos in lines]
    t = time(discs)
    print("answer 1:", t)
    lines.append([7, 11, 0, 0])  # a new disc for question 2
    discs = [[idx, arms, (pos + idx) % arms] for idx, arms, _, pos in lines]
    t = time(discs)
    print("answer 2:", t)


if __name__ == "__main__":
    main()
