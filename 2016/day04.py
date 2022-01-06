from string import ascii_lowercase as az
import collections as co

lines = []
north_pols_objects_id = 0

with open("input04.txt") as f:
    for line in f:
        line = line.strip()
        lines.append(line)


def decrypt(char, nr):
    if char == "-":
        return " "
    return az[(az.index(char) + nr) % 26]


def real_room(dashed_string, _id, checksum):
    global north_pols_objects_id
    c = co.Counter(dashed_string)
    del c["-"]
    alpha = sorted(c.most_common())
    final = sorted(alpha, key=lambda x: x[1], reverse=True)
    check = "".join([item[0] for item in final[:5]])
    if check != checksum:
        return 0
    name = "".join([decrypt(c, _id) for c in dashed_string])
    if name == "northpole object storage":
        north_pols_objects_id = _id
    return _id


total = 0
for line in lines:
    dashed_string, _id, checksum = line[:-11], int(line[-10:-7]), line[-6:-1]
    total += real_room(dashed_string, _id, checksum)

print("answer 1:", total)
print("answer 2:", north_pols_objects_id)
