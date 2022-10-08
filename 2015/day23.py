instructions = []
with open("input23.txt") as f:
    for line in f:
        line = line.strip()
        instruction, other = line.split(" ", maxsplit=1)
        args = other.split(", ")
        instructions.append((instruction, args))


def execute(reg, instructions):
    index = 0
    while True:
        jump = +1
        if index > len(instructions) - 1:
            break

        instruction, args = instructions[index]
        if instruction == "hlf":
            reg[args[0]] //= 2
        if instruction == "tpl":
            reg[args[0]] *= 3
        if instruction == "inc":
            reg[args[0]] += 1
        if instruction == "jmp":
            jump = int(args[0])
        if instruction == "jie" and reg[args[0]] % 2 == 0:
            jump = int(args[1])
        if instruction == "jio" and reg[args[0]] == 1:
            jump = int(args[1])

        index += jump

    return reg['b']


print("answer 1:" ,execute({"a": 0, "b": 0}, instructions))
print("answer 2:", execute({"a": 1, "b": 0}, instructions))
