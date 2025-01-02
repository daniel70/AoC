
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
assert test([0,3,5,4,3,0], [117440,0,0], both=False) == [0, 3, 5, 4, 3, 0]
print(test([0,3,5,4,3,0], [117440,0,0], both=False))

lines = [line for line in open("test17.txt").read().splitlines() if line]
A = int(lines[0].split(":")[1])
B = int(lines[1].split(":")[1])
C = int(lines[2].split(":")[1])
program = list(map(int, lines[3].split(":")[1].split(",")))
pointer = 0
output = []

answer1 = ",".join([str(c) for c in test(program, [A, B, C], False)])
print(f"answer 1: {answer1}")

a = 0
while output != [0,3,5,4,3,0]:
    a += 1
    output = test([0,3,5,4,3,0], [a, 0, 0], False)

print(f"answer 2: {a}")

a = 8 * 23798078187393
n = 16
output = []
find = [2,4,1,2,7,5,4,5,0,3,1,7,5,5,3,0]
# find = [0,3,5,4,3,0]
while output != find:
    a += 1
    # if a % 100000 == 0:
    #     print(a)
    output = test(find, [a, 0, 0], False)
    if output == find[len(find)-n:]:
        print(f"{a} -> {output}")
print(f"answer 2: {a}")

"""
190384625499151

23798078187393 -> [4, 1, 2, 7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]

2974759613685 -> [1, 2, 7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]
2974759773424 -> [1, 2, 7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]
2974759773429 -> [1, 2, 7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]

1420280 -> [3, 1, 7, 5, 5, 3, 0]
1420281 -> [3, 1, 7, 5, 5, 3, 0]
1420283 -> [3, 1, 7, 5, 5, 3, 0]
1549547 -> [3, 1, 7, 5, 5, 3, 0]

12396383 -> [0, 3, 1, 7, 5, 5, 3, 0]

99171066 -> [5, 0, 3, 1, 7, 5, 5, 3, 0]
99171069 -> [5, 0, 3, 1, 7, 5, 5, 3, 0]
99171071 -> [5, 0, 3, 1, 7, 5, 5, 3, 0]

793368535 -> [4, 5, 0, 3, 1, 7, 5, 5, 3, 0]
793368574 -> [4, 5, 0, 3, 1, 7, 5, 5, 3, 0]

6346948282 -> [5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]
6346948285 -> [5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]
6346948594 -> [5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]
6346948599 -> [5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]

50775586259 -> [7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]
50775586280 -> [7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]
50775588755 -> [7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]
50775588756 -> [7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]
50775588757 -> [7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]
50775588796 -> [7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]
50775588797 -> [7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]
50775588799 -> [7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]

406204690078 -> [2, 7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]
406204710046 -> [2, 7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]

3249637520629 -> [1, 2, 7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]
3249637680368 -> [1, 2, 7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]
3249637680373 -> [1, 2, 7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]

25997101442945 -> [4, 1, 2, 7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]
207976811543567 is too high
207976801319951
"""