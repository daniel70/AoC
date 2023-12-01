nrs = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
chars = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def first_last(line: list, values: list[str]) -> tuple[str, str]:
    first = last = ""
    while not first:
        s = "".join(line)
        for v in values:
            if s.startswith(v):
                first = v
                break
        else:
            line.pop(0)

    while not last:
        s = "".join(line)
        for v in values:
            if s.endswith(v):
                last = v
                break
        else:
            line.pop()

    return first, last


def char_to_int(first: str, last: str) -> int:
    first = nrs.index(first) if first in nrs else chars.index(first)
    last = nrs.index(last) if last in nrs else chars.index(last)
    return (int(first) + 1) * 10 + int(last) + 1


answer1 = []
answer2 = []
with open("input01.txt") as file:
    for line in file:
        line = line.strip()
        line = list(line)

        first, last = first_last(line.copy(), nrs)
        answer1.append([first, last])
        first, last = first_last(line.copy(), nrs + chars)
        answer2.append([first, last])

print("answer 1:", sum(char_to_int(first, last) for first, last in answer1))
print("answer 2:", sum(char_to_int(first, last) for first, last in answer2))
