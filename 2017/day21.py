from math import sqrt


def stitch_squares(squares):
    """ Return one square from a square number of squares"""
    # step size is square root of squares
    length = len(squares)
    step = int(sqrt(length))
    size = len(squares[0])

    cells = []
    worm = []
    for steps in range(0, length, step):
        for y in range(size):
            for x in range(step):
                cells.append((steps + x, y))
                worm.extend(squares[steps + x][y])

    length = int(sqrt(len(worm)))
    square = []
    for x in range(length):
        row = []
        for y in range(length):
            row.append(worm[length * x + y])
        square.append(row.copy())

    return square, sum(worm)


def divide_square(square: list[list]):
    """
    We receive a square, can be any size, and return a list of squares
    #..#
    ....
    ....
    #..#

    #.|.#
    ..|..
    --+--
    ..|..
    #.|.#
    """
    length = len(square)
    if length % 2 == 0:
        step = 2
    elif length % 3 == 0:
        step = 3
    else:
        raise ValueError(f"{length=} is not divisable by 2 or 3.")

    squares = []
    for y_sq in range(length // step):
        for x_sq in range(length // step):
            table = []
            for y in range(step):
                row = []
                for x in range(step):
                    row.append(square[y_sq * step + y][x_sq * step + x])
                table.append(row.copy())
            squares.append(table.copy())

    return squares


def rotate_square(square: list[list]) -> list[list]:
    """
    This function takes a square and returns the same square rotated by 90 degrees.
    """
    return [[square[i][j] for i in reversed(range(len(square)))] for j in range(len(square))]


def flip_square(square: list[list]) -> list[list]:
    """
    This function takes a square and returns the same square flipped horizontally.
    """
    return [[square[j][i] for i in reversed(range(len(square)))] for j in range(len(square))]


def square_to_string(square: list[list]) -> str:
    return "/".join(["".join(["." if c == 0 else "#" for c in row]) for row in square])


def string_to_square(s: str) -> list[list]:
    return [[0 if c == '.' else 1 for c in row] for row in s.split("/")]


def tupleize(ll):
    return tuple(tuple(l) for l in ll)


def main():
    pattern = r".#./..#/###"
    rules = {}
    with open("input21.txt") as f:
        for line in f:
            line = line.strip()
            l, r = line.split(" => ")
            square_0 = string_to_square(l)
            flip_0 = flip_square(square_0)
            square_1 = rotate_square(square_0)
            flip_1 = flip_square(square_1)
            square_2 = rotate_square(square_1)
            flip_2 = flip_square(square_2)
            square_3 = rotate_square(square_2)
            flip_3 = flip_square(square_3)
            possible_squares = tuple(
                set([tupleize(square_0), tupleize(flip_0), tupleize(square_1), tupleize(flip_1), tupleize(square_2),
                    tupleize(flip_2), tupleize(square_3), tupleize(flip_3), ]))
            enhanced_grid = string_to_square(r)
            for ps in possible_squares:
                rules[ps] = enhanced_grid

    enhanced_grid = string_to_square(pattern)
    for turn in range(5):
        squares = divide_square(enhanced_grid)
        enhances_squares = [rules[tupleize(square)] for square in squares]
        enhanced_grid, on = stitch_squares(enhances_squares)

    print("answer 1:", on)

    enhanced_grid = string_to_square(pattern)
    for turn in range(18):
        squares = divide_square(enhanced_grid)
        enhances_squares = [rules[tupleize(square)] for square in squares]
        enhanced_grid, on = stitch_squares(enhances_squares)

    print("answer 2:", on)


if __name__ == "__main__":
    exit(main())
