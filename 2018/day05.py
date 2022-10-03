with open("input05.txt") as f:
    line = f.readline().strip()


def destroy(a, b):
    return (
        a.lower() == b.lower()
        and
        (a.isupper() and b.islower() or a.islower() and b.isupper())
    )


def react(polymer: str) -> int:
    buffer = ['-']
    for c in polymer:
        if destroy(c, buffer[-1]):
            buffer.pop()
        else:
            buffer.append(c)
    return len(buffer) - 1


print("answer 1:", react(line))
print("answer 2:", min([react(line.replace(c, '').replace(c.upper(), '')) for c in set(c.lower() for c in line)]))
