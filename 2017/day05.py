with open("input05.txt") as f:
    instructions = [int(line.strip()) for line in f]

one = instructions.copy()
two = instructions.copy()
length = len(instructions)

counter = pointer = 0
while 0 <= pointer < length:
    moves = one[pointer]
    one[pointer] += 1
    pointer = pointer + moves
    counter += 1

print("answer 1:", counter)

counter = pointer = 0
while 0 <= pointer < length:
    moves = two[pointer]
    if moves >= 3:
        two[pointer] -= 1
    else:
        two[pointer] += 1
    pointer = pointer + moves
    counter += 1

print("answer 2:", counter)
