import statistics

numbers = list(map(int, open("input07.txt").read().strip().split(",")))
median = statistics.median(numbers)
distance = 0
for nr in numbers:
    distance += int(abs(nr - median))

print('answer 1:', distance)

# build a dict with triangular numbers
triangular = {}
current = 0
for i in range(max(numbers) + 1):
    current += i
    triangular[i] = current

distances = {}
for i in range(max(numbers)):
    fuel = sum([triangular[abs(i - pos)] for pos in numbers])
    distances[i] = fuel

print('answer 2:', min(distances.values()))
