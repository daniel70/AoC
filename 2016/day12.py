
instructions = []
with open("input12.txt") as f:
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
        else:
            done = True

    return registers["a"]


print("answer 1:", solve({"a": 0, "b": 0, "c": 0, "d": 0}))
print("answer 2:", solve({"a": 0, "b": 0, "c": 1, "d": 0}))
