
def test(program, registers=None, both=True):
    global A, B, C, pointer, output
    pointer = 0
    output = []
    if registers is not None:
        A, B, C = registers
    while pointer < len(program):
        pointer = computer(program[pointer], program[pointer + 1])

    if both:
        return output, [A, B, C]
    else:
        return output

def combo(operant: int) -> int:
    return [0, 1, 2, 3, A, B, C][operant]


def computer(opcode: int, operant: int):
    global A, B, C, pointer, output
    match opcode, operant:
        case 0, operant: # adv
            A = A // (2 ** combo(operant))
        case 1, operant: # bxl
            B = B ^ operant
        case 2, operant: # bst
            B = combo(operant) % 8
        case 3, operant: # jnz
            if A != 0:
                return operant

        case 4, _: # bxc
            B = B ^ C
        case 5, operant: # out
            output.append(combo(operant) % 8)
        case 6, operant: # bdv
            B = A // (2 ** combo(operant))
        case 7, operant: # cdv
            C = A // (2 ** combo(operant))

    return pointer + 2


assert test([2, 6], [0, 0, 9]) == ([], [0, 1, 9])
assert test([5,0,5,1,5,4], [10,0,0]) == ([0, 1, 2], [10, 0, 0])
assert test([0,1,5,4,3,0], [2024,0,0]) == ([4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0], [0, 0, 0])
assert test([1,7], [0,29,0]) == ([], [0, 26, 0])
assert test([4,0], [0,2024,43690]) == ([], [0, 44354, 43690])
assert test([0,1,5,4,3,0], [729,0,0]) == ([4, 6, 3, 5, 6, 3, 5, 2, 1, 0], [0, 0, 0])

lines = [line for line in open("input17.txt").read().splitlines() if line]
A = int(lines[0].split(":")[1])
B = int(lines[1].split(":")[1])
C = int(lines[2].split(":")[1])
program = list(map(int, lines[3].split(":")[1].split(",")))
pointer = 0
output = []

answer1 = ",".join([str(c) for c in test(program, [A, B, C], False)])
print(f"answer 1: {answer1}")