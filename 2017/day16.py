from string import ascii_lowercase


def dance(programs, instructions):
    for instruction in instructions:
        match instruction[0]:
            case "s":  # spin
                x = int(instruction[1:])
                programs = programs[-x:] + programs[:-x]
            case "x":  # swap
                x, y = sorted([int(x) for x in instruction[1:].split("/")])
                programs = programs[:x] + programs[y] + programs[x + 1:y] + programs[x] + programs[y + 1:]
            case "p":  # partner
                x, y = sorted([programs.index(x) for x in instruction[1:].split("/")])
                programs = programs[:x] + programs[y] + programs[x + 1:y] + programs[x] + programs[y + 1:]
    return programs


nr_of_programs = 16
programs = ascii_lowercase[:nr_of_programs]
instructions = open("input16.txt").read().strip().split(",")
seen = [programs]
programs = dance(programs, instructions)
seen.append(programs)

print("answer 1:", programs)

while True:
    programs = dance(programs, instructions)
    if programs in seen:
        break
    seen.append(programs)

skip = len(seen) - seen.index(programs)
for _ in range((1_000_000_000 - len(seen)) % skip):
    programs = dance(programs, instructions)

print("answer 2:", programs)
