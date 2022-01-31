instructions = open("input23mul.txt").read().strip().splitlines()
registers = {"a": 7, "b": 0, "c": 0, "d": 0}
pointer = 0


def get_value(arg: str):
    assert arg
    if arg.strip("-").isdigit():
        return int(arg)
    return registers[arg]


while pointer < len(instructions):
    print(registers, pointer)
    args = instructions[pointer].split()
    match args[0]:
        case "mul":
            if get_value(args[1]) == 0:
                pointer += 1
            else:
                registers[args[2]] += get_value(args[1])
                registers[args[1]] = 0
        case "jnz":
            if get_value(args[1]) == 0:
                pointer += 1
            else:
                pointer += get_value(args[2])
        case "inc":
            registers[args[1]] += 1
            # registers[args[1]] = get_value(args[1]) * get_value(args[1])
            pointer += 1
        case "dec":
            registers[args[1]] -= 1
            pointer += 1
        case "cpy":
            if args[1].strip("-").isdigit() and args[2].strip("-").isdigit():
                # invalid from tgl, skip
                pointer += 1
                continue

            registers[args[2]] = get_value(args[1])
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

print(registers)
