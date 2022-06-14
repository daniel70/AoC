from collections import defaultdict

transformations = {}
initials = []
with open("input19.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            molecule = f.readline().strip()
            break
        l, r = line.split(" => ")
        if l == "e":
            initials.append(r)
        else:
            transformations[r] = l


# check overlap
# transvals = transformations.keys()
# for k in transformations.keys():
#     for val in transvals:
#         if k in val and not k == val:
#             print(f"overlap {k}, {val}")

temp = molecule
for i in range(10):
    count = 0
    for key, val in transformations.items():
        if key in temp:
            count += 1
        temp = temp.replace(key, val, 1)
    print(i, count)
print(temp)
