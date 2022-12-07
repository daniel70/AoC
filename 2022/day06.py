instructions = ""
with open('input06.txt') as f:
    for line in f:
        line = line.strip()
        instructions = line


def find_marker(signal: str, length: int) -> int:
    for idx in range(length, len(signal)):
        if len(set(instructions[idx-length:idx])) == length:
            break

    return idx


print("answer 1:", find_marker(instructions, 4))
print("answer 2:", find_marker(instructions, 14))
