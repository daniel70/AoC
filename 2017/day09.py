def garbage(stream: str) -> tuple[str, int]:
    cancel = False
    inside = False
    points = []
    ncc: int = 0

    if stream == "":
        return stream

    for idx, char in enumerate(stream):
        if inside and char != "!" and not cancel:
            ncc += 1

        if char == "<" and not inside and not cancel:
            points.append([idx, None])
            inside = True
        if char == ">" and inside and not cancel:
            points[-1][1] = idx
            inside = False
            ncc -= 1
        if char == "!" and inside:
            cancel = not cancel
        else:
            cancel = False

    for first, last in reversed(points):
        stream = stream[:first] + stream[last+1:]

    return stream, ncc


def counter(stream: str) -> int:
    total = 0
    level = 0
    for char in stream:
        if char == "{":
            level += 1
            total += level
        if char == "}":
            level -= 1
    return total


instruction = open("input09.txt").read().strip()
stream, ncc = garbage(instruction)

print("answer 1", counter(stream))
print("answer 2", ncc)
