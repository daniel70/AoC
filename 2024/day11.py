from collections import deque, Counter


totals = Counter(map(int, open(r"2024\input11.txt").read().split()))
stones = deque(totals.keys())
previous = totals.copy()
for r in range(75):
    new = Counter()
    while stones:
        stone = stones.popleft()
        if stone == 0:
            new[1] += previous[stone]
        elif len(str(stone)) % 2 == 0:
            left, right = int(str(stone)[:len(str(stone))//2]), int(str(stone)[len(str(stone))//2:])
            new[left] += previous[stone]
            new[right] += previous[stone]
        else:
            new[stone * 2024] += previous[stone]
    totals.update(new)
    previous = new.copy()
    stones = deque(new.keys())
    print(f"round {r+1}:", sum(new.values()))
print(sum(totals.values()))
