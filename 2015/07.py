import re

re_assembly = re.compile(r"(\w+)\s*(\w+)?\s*(\w+)? -> (\w+)")
actions = []
with open("input07.txt") as f:
    for line in f:
        line = line.strip()
        m = re_assembly.match(line)
        assert m is not None
        actions.append(m.groups())


def find_wire(actions):
    found = {}
    while len(actions):
        for action in actions[:]:
            A, B, C, D = action

            if B is None and A.isnumeric():
                found[D] = int(A)
                actions.remove(action)

            elif B is None and A in found:
                found[D] = int(found[A])
                actions.remove(action)

            elif A == "NOT" and B in found:
                found[D] = 65535 - found[B]
                actions.remove(action)

            elif B == "AND" and A.isnumeric() and C in found:
                found[D] = int(A) & found[C]
                actions.remove(action)

            elif B == "AND" and A in found and C in found:
                found[D] = found[A] & found[C]
                actions.remove(action)

            elif B == "OR" and A in found and C in found:
                found[D] = found[A] | found[C]
                actions.remove(action)

            elif B == "LSHIFT" and A in found:
                found[D] = found[A] << int(C)
                actions.remove(action)

            elif B == "RSHIFT" and A in found:
                found[D] = found[A] >> int(C)
                actions.remove(action)

    return found["a"]


answer1 = find_wire(actions[:])
print(answer1)
for A, B, C, D in actions:
    if D == 'b':
        actions.remove((A, B, C, D))
        actions.append((str(answer1), B, C, D))
        break
answer2 = find_wire(actions[:])
print(answer2)
