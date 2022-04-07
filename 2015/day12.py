import json

with open('input12.txt') as f:
    instructions = json.load(f)


def summer(obj, skip_red=False):
    match obj:
        case int(obj):
            return obj

        case dict(obj):
            if skip_red and "red" in obj.values():
                return 0
            else:
                return sum([summer(val, skip_red) for val in obj.values()])

        case list(obj):
            return sum([summer(val, skip_red) for val in obj])

    return 0


print("answer 1:", summer(instructions))
print("answer 2:", summer(instructions, skip_red=True))
