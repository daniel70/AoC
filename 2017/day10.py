def knot_hash(lengths, numbers, rounds=1):
    current_position = skip_size = 0
    for _ in range(rounds):
        for length in lengths:
            numbers = numbers[current_position:] + numbers[:current_position]
            numbers = list(reversed(numbers[:length])) + numbers[length:]
            numbers = numbers[-current_position:] + numbers[:-current_position]
            current_position += (length + skip_size)
            current_position %= len(numbers)
            skip_size += 1
    return numbers


instructions = open("input10.txt").read().strip()
lengths = [int(x) for x in instructions.split(",")]
numbers = knot_hash(lengths, list(range(256)))
print("answer 1:", numbers[0] * numbers[1])

lengths = []
for c in instructions:
    lengths.append(ord(c))
lengths.extend([int(x) for x in "17,31,73,47,23".split(",")])

numbers = knot_hash(lengths, list(range(256)), rounds=64)
dense_hash = []
for i in range(16):
    value = 0
    for j in range(16):
        value = value ^ numbers[i*16+j]
    dense_hash.append(value)

print("answer 2:", "".join([f"{x:02x}" for x in dense_hash]))
