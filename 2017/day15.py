with open("input15.txt") as f:
    a_start = int(f.readline().strip().split()[-1])
    b_start = int(f.readline().strip().split()[-1])


def generator(start, factor, mod=1):
    current = start
    while True:
        current = (current * factor) % 2147483647
        if current % mod == 0:
            yield current


def matches(gen_a, gen_b, rounds):
    total = 0
    for _ in range(rounds):
        a = next(gen_a) & 65535
        b = next(gen_b) & 65535
        if a == b:
            total += 1

    return total


print("answer 1:", matches(generator(a_start, 16807), generator(b_start, 48271), 40_000_000))
print("answer 2:", matches(generator(a_start, 16807, mod=4), generator(b_start, 48271, mod=8), 5_000_000))
