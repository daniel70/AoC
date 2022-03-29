with open("input15.txt") as f:
    a_start = int(f.readline().strip().split()[-1])
    b_start = int(f.readline().strip().split()[-1])


def generator(start, factor, multiple_of=1):
    current = start
    while True:
        current = (current * factor) % 2147483647
        if current % multiple_of == 0:
            yield current


gen_a = generator(a_start, 16807)
gen_b = generator(b_start, 48271)
answer1 = 0
for _ in range(40_000_000):
    a = next(gen_a) & 65535
    b = next(gen_b) & 65535
    # print(f"{a:016b}")
    # print(f"{b:016b}")
    # print()
    if a == b:
        answer1 += 1

print("answer 1:", answer1)
gen_a = generator(a_start, 16807, multiple_of=4)
gen_b = generator(b_start, 48271, multiple_of=8)
answer2 = 0
for _ in range(5_000_000):
    a = next(gen_a) & 65535
    b = next(gen_b) & 65535
    # print(f"{a:016b}")
    # print(f"{b:016b}")
    # print()
    if a == b:
        answer2 += 1

print("answer 2:", answer2)
