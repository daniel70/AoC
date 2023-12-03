import re
from collections import defaultdict

re_numbers = re.compile(r"\d+")
re_symbols = re.compile(r"[^0-9\.]")


def find_matches(regex, line):
    pos = 0
    matches = []
    while match := regex.search(line, pos=pos):
        matches.append(match)
        pos = match.end()
    return matches


def adjacent_cells(numbers):
    cells = defaultdict(list)
    for nr, line in enumerate(numbers):
        for match in line:
            for x in range(match.start() - 1, match.end() + 1):
                cells[((nr - 1, x))].append(int(match.group()))
                cells[((nr, x))].append(int(match.group()))
                cells[((nr + 1, x))].append(int(match.group()))
    return cells


numbers = []
symbols = []
with open("input03.txt") as file:
    for line in file:
        line = line.strip()
        numbers.append(find_matches(re_numbers, line))
        symbols.append(find_matches(re_symbols, line))

cells = adjacent_cells(numbers=numbers)

total = 0
for nr, line in enumerate(symbols):
    for symbol in line:
        total += sum(cells[(nr, symbol.start())])

print(total)