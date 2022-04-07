import math


def get_value(arg: str, registers):
    assert arg
    if arg.strip("-").isdigit():
        return int(arg)
    return registers[arg]


def process(registers, instructions):
    pointer = 0
    steps = 0
    while pointer < len(instructions):
        steps += 1
        args = instructions[pointer].split()
        match args[0]:
            case "nop":
                pointer += 1
            case "mul":
                if get_value(args[1], registers) == 0:
                    pointer += 1
                else:
                    registers[args[-1]] += math.prod([get_value(x, registers) for x in args[1:-1]])
                    for arg in args[1:-1]:
                        registers[arg] = 0
            case "jnz":
                if get_value(args[1], registers) == 0:
                    pointer += 1
                else:
                    pointer += get_value(args[2], registers)
            case "inc":
                registers[args[1]] += 1
                pointer += 1
            case "dec":
                registers[args[1]] -= 1
                pointer += 1
            case "cpy":
                if args[1].strip("-").isdigit() and args[2].strip("-").isdigit():
                    # invalid from tgl, skip
                    pointer += 1
                    continue

                registers[args[2]] = get_value(args[1], registers)
                pointer += 1
            case "tgl":
                tgl_pntr = pointer + registers[args[1]]
                if tgl_pntr >= len(instructions):
                    # nothing happens
                    pointer += 1
                    continue
                tgl = instructions[tgl_pntr].split()
                if len(tgl) == 2:  # one-argument
                    tgl[0] = "dec" if tgl[0] == "inc" else "inc"
                if len(tgl) == 3:  # two-argument
                    tgl[0] = "cpy" if tgl[0] == "jnz" else "jnz"
                instructions[tgl_pntr] = " ".join(tgl)
                pointer += 1

            case _:
                print("oh no, can't handle", [args[0]])
                break

    return registers['a']


# rewrite jnz -> mul; "jnz a b" jumps b instructions if a != 0
instructions = open("input23.txt").read().strip().splitlines()
for idx, instruction in enumerate(instructions.copy()):
    args = instruction.split()
    if args[0] == "jnz" and not args[1].isdigit():
        # collect the parameters of previous lines and replace with nop
        params = []
        for i in range(idx + int(args[2]), idx):
            new_args = instructions[i].split()
            if new_args[0] not in ["inc", "dec", "mul"]:
                continue
            params.extend(new_args[1:])  # collect all params
            instructions[i] = "nop"

        params.remove(args[1])
        instructions[idx] = "mul " + args[1] + " " + " ".join(params)


print(f"answer 1:", process({"a": 7, "b": 0, "c": 0, "d": 0}, instructions.copy()))
print(f"answer 2:", process({"a": 12, "b": 0, "c": 0, "d": 0}, instructions.copy()))
