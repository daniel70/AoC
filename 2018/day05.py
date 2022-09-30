import string
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
combinations = [lc+uc for lc, uc in zip(lowercase, uppercase)] + [uc+lc for lc, uc in zip(lowercase, uppercase)]
line = 'dabAcCaCBAcCcaDA'
with open("input05.txt") as f:
    line = f.readline()


def react(polymer: str, remove: str | None = None) -> int:
    if remove is not None:
        polymer = polymer.replace(remove, '')
        polymer = polymer.replace(remove.upper(), '')

    match = True
    while match:
        for c in combinations:
            match = False
            if c in polymer:
                match = True
                polymer = polymer.replace(c, '', 1)
                break
    return len(polymer) - 1


answer = react(line, None)
print("answer 1:", answer)

for letter in lowercase:
    answer = min(answer, react(line, letter))

print("answer 2:", answer)
