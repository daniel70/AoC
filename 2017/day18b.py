from collections import defaultdict
from string import ascii_lowercase


def get_value(param: str, duet) -> int:
    if param in ascii_lowercase:
        return duet[param]
    return int(param)


def program(instructions, program_id: int):
    duet = defaultdict(int)
    duet["p"] = program_id

    line = 0
    high = len(instructions)
    while True:
        instruction = instructions[line]
        line += 1
        match instruction[0]:
            case "snd":
                frequency = get_value(instruction[1], duet)
                # print(f"{program_id=} sending {frequency}")
                yield frequency
            case "rcv":
                received = yield
                # print(f"{program_id=} received {received}")
                if instruction[1] != 0:
                    duet[instruction[1]] = received
            case "set":
                duet[instruction[1]] = get_value(instruction[2], duet)
            case "add":
                duet[instruction[1]] += get_value(instruction[2], duet)
            case "mul":
                duet[instruction[1]] *= get_value(instruction[2], duet)
            case "mod":
                duet[instruction[1]] %= get_value(instruction[2], duet)
            case "jgz":
                if get_value(instruction[1], duet) != 0:
                    line += get_value(instruction[2], duet) - 1

        if not 0 <= line < high:
            return


instructions = []
frequency = 0
with open("input18.txt") as f:
    for ln in f:
        ln = ln.strip()
        instructions.append(ln.split())

# instructions = [
#     ["snd", "1"],
#     ["snd", "2"],
#     ["snd", "p"],
#     ["rcv", "a"],
#     ["rcv", "b"],
#     ["mul", "b", "4"],
#     ["snd", "17"],
#     ["rcv", "c"],
#     ["rcv", "d"],
# ]

q0 = []
q1 = []
p0 = program(instructions, 0)
p1 = program(instructions, 1)

total = 0
ret0 = next(p0)
ret1 = next(p1)
while not (p0 is None and p1 is None):
    if p0 is not None:
        try:
            # keep receiving from p0 until no value is given
            while ret0 is not None:
                total += 1
                q1.append(ret0)
                ret0 = next(p0)

            while ret0 is None and len(q0) > 0:
                print(f"len q0: {len(q0)}")
                ret0 = p0.send(q0.pop(0))

        except StopIteration:
            p0 = None

    if p1 is not None:
        try:
            # keep receiving from p1 until no value is given
            while ret1 is not None:
                q0.append(ret1)
                ret1 = next(p1)

            while ret1 is None and len(q1) > 0:
                print(f"len q1: {len(q1)}")
                ret1 = p1.send(q1.pop(0))

        except StopIteration:
            p1 = None

    if len(q0) == 0 and len(q1) == 0:
        break

print("answer 2:", total)
