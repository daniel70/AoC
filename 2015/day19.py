*lines, _, molecule = open("input19.txt").readlines()
replacements = [line.strip().split(" => ") for line in lines]
molecule = molecule.strip()
min_steps = None
molecules = set()
for before, after in replacements:
    for position in range(len(molecule)):
        left, right = molecule[:position], molecule[position:]
        if right.startswith(before):
            molecules.add(left + right.replace(before, after, 1))

print("Answer 1:", len(molecules))

sorted_replacements = {}  # we'll try to replace the longest strings first
for before, after in sorted(replacements, key=lambda values: len(values[1]), reverse=True):
    sorted_replacements[after] = before


def find_e(s: str, step: int):
    global min_steps
    found = None
    if min_steps is not None:
        return

    if s == "e":
        min_steps = step
        return min_steps

    for left in range(len(s)):
        if found is not None:
            break
        if left > 14:  # optimized for my input, this is a magic number to me
            return
        for key, value in sorted_replacements.items():
            if s[left:].startswith(key):
                found = find_e(s.replace(key, value, 1), step=step+1)

    return min_steps


print("Answer 2:", find_e(s=molecule, step=0))
