from collections import defaultdict
from string import ascii_lowercase


def get_value(param: str, duet) -> int:
    if param in ascii_lowercase:
        return duet[param]
    return int(param)


def program(instructions, program_id: int = 0):
    global high
    duet = defaultdict(int)
    duet["p"] = program_id

    line = 0
    while True:
        instruction = instructions[line]
        line += 1
        match instruction[0]:
            case "snd":
                yield get_value(instruction[1], duet)
            case "rcv":
                duet[instruction[1]] = yield
            case "set":
                duet[instruction[1]] = get_value(instruction[2], duet)
            case "add":
                duet[instruction[1]] += get_value(instruction[2], duet)
            case "mul":
                duet[instruction[1]] *= get_value(instruction[2], duet)
            case "mod":
                duet[instruction[1]] %= get_value(instruction[2], duet)
            case "jgz":
                if get_value(instruction[1], duet) > 0:
                    line += get_value(instruction[2], duet) - 1

        if not 0 <= line < high:
            return


instructions = []
with open("input18.txt") as f:
    for ln in f:
        ln = ln.strip()
        instructions.append(ln.split())
high = len(instructions)


p = program(instructions)
ret = next(p)
frequency = 0
while p is not None:
    try:
        # keep receiving from p0 until no value is given
        while ret is not None:
            frequency = ret
            ret = next(p)

        if ret is None:
            print("answer 1:", frequency)
            break

    except StopIteration:
        p = None


q0 = []
q1 = []
p0 = program(instructions, 0)
p1 = program(instructions, 1)

ret0 = next(p0)
ret1 = next(p1)
total = 0
while not (p0 is None and p1 is None):
    if p0 is not None:
        try:
            while ret0 is not None:
                q1.append(ret0)
                ret0 = next(p0)

            while ret0 is None and len(q0) > 0:
                ret0 = p0.send(q0.pop(0))

        except StopIteration:
            p0 = None

    if p1 is not None:
        try:
            while ret1 is not None:
                total += 1
                q0.append(ret1)
                ret1 = next(p1)

            while ret1 is None and len(q1) > 0:
                ret1 = p1.send(q1.pop(0))

        except StopIteration:
            p1 = None

    if len(q0) == 0 and len(q1) == 0:
        break

print("answer 2:", total)
