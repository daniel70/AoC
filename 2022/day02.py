instructions = []
with open('input02.txt') as f:
    for line in f:
        line = line.strip()
        instructions.append(line.split())


def play(he, me, ending=False):
    ix_he = ["A", "B", "C"].index(he)
    ix_me = ["X", "Y", "Z"].index(me)
    if not ending:
        vector = [4, 8, 3, 1, 5, 9, 7, 2, 6]
    else:
        vector = [3, 4, 8, 1, 5, 9, 2, 6, 7]

    return vector[ix_he * 3 + ix_me]


print("answer 1:", sum([play(a, b, ending=False) for a, b in instructions]))
print("answer 2:", sum([play(a, b, ending=True) for a, b in instructions]))
