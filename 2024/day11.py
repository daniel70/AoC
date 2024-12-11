from collections import deque

stones = deque(map(int, open(r"2024\input11.txt").read().split()))
stones = deque([0])
for r in range(12):
    new = deque()
    while stones:
        stone = stones.popleft()
        if stone == 0:
            new.append(1)
        elif len(str(stone)) % 2 == 0:
            left, right = int(str(stone)[:len(str(stone))//2]), int(str(stone)[len(str(stone))//2:])
            new.extend([left, right])
        else:
            new.append(stone * 2024)
    stones = new
    print(f"round {r}:", len(stones), stones)
print(len(stones))