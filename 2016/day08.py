import re


def rect(screen, x, y):
    for r in range(y):
        for c in range(x):
            screen[r][c] = 1


def rotate_row(screen, x, y):
    row = screen[x].copy()
    for c in range(C):
        screen[x][c] = row[(c+C-y) % C]


def rotate_column(screen, x, y):
    column = [row[x] for row in screen]
    for r in range(R):
        screen[r][x] = column[(r+R-y) % R]


with open("input08.txt") as f:
    xy = re.compile(r"(\d+).*?(\d+)")
    C = 50
    R = 6
    screen = [[0] * C for r in range(R)]

    for line in f:
        line = line.strip()
        x, y = xy.findall(line)[0]
        x, y = int(x), int(y)
        if line.startswith("rect"):
            rect(screen, x, y)
        elif line.startswith("rotate row"):
            rotate_row(screen, x, y)
        elif line.startswith("rotate column"):
            rotate_column(screen, x, y)

    lit = sum(map(sum, screen))
    print("answer 1:", lit)

    print("answer 2:")
    for row in screen:
        for col in row:
            print(f"{[' ', '#'][col]}", end="")
        print()
