from collections import defaultdict
from string import ascii_lowercase


def get_value(param: str) -> int:
    if param in ascii_lowercase:
        return duet[param]
    return int(param)


duet = defaultdict(int)
instructions = []
frequency = 0
with open("input18.txt") as f:
    for line in f:
        line = line.strip()
        instructions.append(line.split())

line = 0
high = len(instructions)
while True:
    instruction = instructions[line]
    line += 1
    match instruction[0]:
        case "set":
            duet[instruction[1]] = get_value(instruction[2])
        case "snd":
            frequency = get_value(instruction[1])
            # print("playing with frequency", frequency)
        case "add":
            duet[instruction[1]] += get_value(instruction[2])
        case "mul":
            duet[instruction[1]] *= get_value(instruction[2])
        case "mod":
            duet[instruction[1]] %= get_value(instruction[2])
        case "rcv":
            if instruction[1] != 0:
                duet[instruction[1]] = frequency
                print("answer 1:", frequency)
                break
        case "jgz":
            if get_value(instruction[1]) != 0:
                line += get_value(instruction[2]) - 1

    if not 0 <= line < high:
        break


program_0 = defaultdict(int)
program_1 = defaultdict(int)
program_1["p"] = 1
