from pprint import pprint


def rotate_square(square: list[list]) -> list[list]:
    """
    This function takes a square and returns the same square rotated by 90 degrees.
    """
    return [
        [square[i][j] for i in reversed(range(len(square)))]
        for j in range(len(square))
    ]


def flip_square(square: list[list]) -> list[list]:
    """
    This function takes a square and returns the same square flipped horizontally.
    """
    return [
        [square[j][i] for i in reversed(range(len(square)))]
        for j in range(len(square))
    ]


def square_to_string(square: list[list]) -> str:
    return "/".join(["".join(["." if c == 0 else "#" for c in row]) for row in square])


def string_to_square(s: str) -> list[list]:
    return [[0 if c == '.' else 1 for c in row] for row in s.split("/")]


pattern = r".#./..#/###"
rules = {}
with open("test21.txt") as f:
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
        rules[(
            square_to_string(square_0),
            square_to_string(flip_0),
            square_to_string(square_1),
            square_to_string(flip_1),
            square_to_string(square_2),
            square_to_string(flip_2),
            square_to_string(square_3),
            square_to_string(flip_3),
        )] = r


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
    squares = []
    length = len(square)
    if length % 2 == 0:
        step = 2
    elif length % 3 == 0:
        step = 3
    else:
        raise ArithmeticError(f"{length=} is not divisable by 2 or 3.")

    for y in range(0, length, step):
        for x in range(0, length, step):
            squares.append(
                [[square[dx + x][dy + y] for dx in range(step)] for dy in range(step)]
            )
    return squares
