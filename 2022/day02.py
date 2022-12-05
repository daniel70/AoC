instructions = []
with open('input02.txt') as f:
    for line in f:
        line = line.strip()
        instructions.append(line.split())


def play(he, me, ending=False):
    """
    Rock Paper Scissors
    Answer 1, ending = False, has 9 solutions starting with 4
    He has rock, I have rock, it's a draw (3), I used rock (1) == 4 points etc.
    Answer 2, ending = True, also has 9 solutions starting with 3
    He has rock, I have to lose (0), I chose scissors (3) == 3 points etc.
    For both answer we use the index of his card (0) * 3 + my card (0) == 0
    """

    ix_he = ["A", "B", "C"].index(he)
    ix_me = ["X", "Y", "Z"].index(me)
    if not ending:
        vector = [4, 8, 3, 1, 5, 9, 7, 2, 6]
    else:
        vector = [3, 4, 8, 1, 5, 9, 2, 6, 7]

    return vector[ix_he * 3 + ix_me]


print("answer 1:", sum(play(a, b, ending=False) for a, b in instructions))
print("answer 2:", sum(play(a, b, ending=True) for a, b in instructions))
