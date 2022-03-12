import itertools

instructions = []
with open("input25.txt") as f:
    for line in f:
        line = line.strip()
        instructions.append(line.split())


def solve(registers):
    jmp = 0
    done = False
    while not done:
        if jmp >= len(instructions):
            done = True
        for idx, instruction in enumerate(instructions[jmp:]):
            if instruction[0] == "inc":
                registers[instruction[1]] += 1
            if instruction[0] == "dec":
                registers[instruction[1]] -= 1
            if instruction[0] == "cpy":
                if instruction[1].isnumeric():
                    x = int(instruction[1])
                else:
                    x = registers[instruction[1]]
                registers[instruction[2]] = x
            if instruction[0] == "jnz":
                if instruction[1].isnumeric():
                    x = int(instruction[1])
                else:
                    x = registers[instruction[1]]
                if x:
                    jmp += idx + int(instruction[2])
                    break
            if instruction[0] == "out":
                yield registers[instruction[1]]
        else:
            done = True

    return registers["a"]


for a in itertools.count(0):
    r = {"a": a, "b": 0, "c": 0, "d": 0}
    solver = solve(r)
    # print(f"{a=}:", end=" ")
    valid = [0, 1]
    is_valid = True
    for _ in range(12):
        signal = next(solver)
        if signal in valid:
            valid = [abs(signal - 1)]
        else:
            is_valid = False
            break

    if is_valid:
        print("answer 1:", a)
        break
