import re
import itertools as it
params = re.compile(r"(position|letter|based|left|right|\b\w(?:\b|$))")


def scramble(line, password):
    match = params.findall(line)
    match line.split()[0]:
        case "swap":
            if match[0] == "position":
                p1, p2 = int(match[1]), int(match[3])
            if match[0] == "letter":
                p1, p2 = password.index(match[1]), password.index(match[3])
            password[p1], password[p2] = password[p2], password[p1]

        case "reverse":
            p1, p2 = int(match[1]), int(match[2])
            password = password[:p1] + list(reversed(password[p1:p2 + 1])) + password[p2 + 1:]

        case "rotate":
            if match[0] == "right":
                p1 = -1 * int(match[1])
            if match[0] == "left":
                p1 = int(match[1])
            if match[0] == "based":
                # this produces the lookup list [-((x + 2 if x >= 4 else x + 1) % 8) for x in range(9)]
                p1 = [-1, -2, -3, -4, -6, -7, 0, -1, -2][password.index(match[3])]

            password = password[p1:] + password[:p1]

        case "move":
            p1, p2 = int(match[1]), int(match[3])
            temp = password.pop(p1)
            password.insert(p2, temp)

    return password


lines = []
with open("input21.txt") as f:
    for line in f:
        line = line.strip()
        lines.append(line)

password = list("abcdefgh")
for line in lines:
    password = scramble(line, password)
print("answer 1:", "".join(password))

for guess in it.permutations("abcdefgh", 8):
    password = list(guess)
    for line in lines:
        password = scramble(line, password)
    if "".join(password) == "fbgdceah":
        break
print("answer 2:", "".join(guess))
