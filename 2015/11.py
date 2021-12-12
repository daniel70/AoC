import re
from string import ascii_lowercase as az
pw = "hxbxwxba"

repairs = re.compile(r"([a-z])\1")
triplets = ["".join(l) for l in zip(az, az[1:], az[2:])]
for triplet in triplets[:]:
    if any(c in ["i", "o", "l"] for c in triplet):
        triplets.remove(triplet)


def passwords(pw) -> str:
    pw_len = len(pw)
    pw = list(pw)
    while True:
        for i in range(pw_len - 1, -1, -1):
            next_char = az[(az.index(pw[i]) + 1) % 26]
            pw[i] = next_char
            if next_char != "a":
                yield "".join(pw)
                break

        else:
            # we reached the end
            break


def valid(password) -> bool:
    # check for confusing characters
    if any([c in ["i", "o", "l"] for c in password]):
        return False

    # check for increasing straight
    if not any(triplet in password for triplet in triplets):
        return False

    # check for two different, non-overlapping pairs
    if len(set(repairs.findall(password))) < 2:
        return False

    return True


for x in [1, 2]:
    for password in passwords(pw):
        if not valid(password):
            continue

        print(f"answer {x}:", password)
        pw = password
        break
