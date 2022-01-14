from collections import defaultdict
import itertools as it


def is_valid(plan: dict) -> bool:
    # if a microchip is on a floor without its generator but with another generator then return False.
    for item, floor in plan.items():
        if item == "E":
            continue
        if item[1] == "M":
            if (item[0] + "G", floor) in plan.items():
                continue
            if any([k[1] == "G" for k, v in plan.items() if v == floor and k != "E"]):
                return False
    return True


def solve(plan):
    floors = 3
    seen = {frozenset(plan.items())}
    steps = defaultdict(list)
    steps[0].append(plan.copy())
    found = False

    for step in it.count(1):
        if found:
            return step - 1

        for plan in steps[step - 1]:
            floor = plan["E"]
            items_on_floor = [k for k, v in plan.items() if v == floor and k != "E"]
            moves = list(it.chain(it.combinations(items_on_floor, 2), it.combinations(items_on_floor, 1)))

            if floor < floors:
                for items in moves:
                    mmap = plan.copy()
                    mmap["E"] = floor + 1
                    for item in items:
                        mmap[item] = floor + 1
                    fmap = frozenset(mmap.items())
                    if is_valid(mmap) and fmap not in seen:
                        if all([floor == 3 for floor in mmap.values()]):
                            found = True
                            break
                        seen.add(fmap)
                        steps[step].append(mmap)

                        # optimization: if we were able to take two items up than that is always a good thing
                        if len(items) == 2:
                            break

            # optimization: don't take two items down
            items = [items[0] for items in moves if len(items) == 1]

            # optimization: don't go down to put items on already empty floors
            if floor > min(plan.values()):
                for item in items:
                    mmap = plan.copy()
                    mmap["E"] = floor - 1
                    mmap[item] = floor - 1
                    fmap = frozenset(mmap.items())
                    if is_valid(mmap) and fmap not in seen:
                        seen.add(fmap)
                        steps[step].append(mmap)


question1 = {"E": 0, "SG": 0, "SM": 0, "PG": 0, "PM": 0, "TG": 1, "RG": 1, "RM": 1, "CG": 1, "CM": 1, "TM": 2}
answer1 = solve(question1)
print("answer 1:", answer1)
question2 = dict(question1, **{"EG": 0, "EM": 0, "DG": 0, "DM": 0})
answer2 = solve(question2)
print("answer 2:", answer2)
