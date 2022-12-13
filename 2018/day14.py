from itertools import count


def ten_after(nr: int) -> str:
    elves = [0, 1]
    recipes = "37"
    while len(recipes) <= nr + 10:
        one, two = int(recipes[elves[0]]), int(recipes[elves[1]])
        total = sum([one, two])
        recipes += str(total)
        idx1 = (elves[0] + one + 1) % len(recipes)
        idx2 = (elves[1] + two + 1) % len(recipes)
        elves = [idx1, idx2]

    return recipes[nr: nr + 10]


def first_occurence(nr: int) -> int:
    nr = str(nr)
    elves = [0, 1]
    recipes = "37"
    while nr not in recipes[-7:]:
        one, two = int(recipes[elves[0]]), int(recipes[elves[1]])
        total = sum([one, two])
        recipes += str(total)
        idx1 = (elves[0] + one + 1) % len(recipes)
        idx2 = (elves[1] + two + 1) % len(recipes)
        elves = [idx1, idx2]

    return recipes.index(nr)


print("answer 1:", ten_after(503761))
print("answer 2:", first_occurence(503761))
