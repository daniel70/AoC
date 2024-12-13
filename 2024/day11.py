from collections import deque, Counter

old = Counter(map(int, open("input11.txt").read().split()))
stones = deque(old.keys())
for round in range(75):
    new = Counter()
    while stones:
        stone = stones.popleft()
        if stone == 0:
            new[1] += old[stone]
        elif len(str(stone)) % 2 == 0:
            left, right = int(str(stone)[:len(str(stone))//2]), int(str(stone)[len(str(stone))//2:])
            new[left] += old[stone]
            new[right] += old[stone]
        else:
            new[stone * 2024] += old[stone]
    old = new.copy()
    stones = deque(new.keys())

    if round == 24:
        print("answer 1:", sum(new.values()))

print(f"answer 2:", sum(new.values()))
