def find_digits(signals):
    digits = {}
    for d in signals:
        match len(d):
            case 2:
                digits[1] = d
            case 3:
                digits[7] = d
            case 4:
                digits[4] = d
            case 7:
                digits[8] = d

    # wire a = 7 - 1
    wires = {"a": (set(digits[7]) - set(digits[1])).pop()}
    # digit 6 is the only len 6 missing either c of f (from 1)
    for s in signals:
        if len(s) == 6:
            c = set(digits[1]) - set(s)
            if c:
                wires["c"] = c.pop()
                digits[6] = s
    # now that we know wire c we can find wire f, it is the other wire in digit 1
    wires["f"] = (set(digits[1]) - set(wires["c"])).pop()
    # digit 5 is the only len 5 that is missing wire c
    for s in signals:
        if len(s) == 5 and wires["c"] not in s:
            digits[5] = s
    # wire e is diff between digit 6 and 5
    wires["e"] = (set(digits[6]) - set(digits[5])).pop()
    # digit 9 is len 6, missing wire e
    for s in signals:
        if len(s) == 6 and wires["e"] not in s:
            digits[9] = s
    # digit 0 is len 6 and not in digits yet
    for s in signals:
        if len(s) == 6 and s not in digits.values():
            digits[0] = s
    # two and three are still missing
    missing = set(signals) - set(digits.values())
    # digit 3 is missing wire f, digit 2 is not missing wire f
    for s in missing:
        if wires["f"] in s:
            digits[3] = s
        else:
            digits[2] = s

    return digits


signals =[]
values = []
with open('input08.txt') as f:
    for line in f:
        line = line.strip()
        entry = line.split(" | ")
        signals.append(entry[0].split())
        values.append(entry[1].split())

total = 0
for value in values:
    for v in value:
        if len(v) in [2, 3, 4, 7]:
            total += 1

print('answer 1', total)

total = 0
for idx, signal in enumerate(signals):
    nr = ""
    digits = find_digits(signal)
    sorted_signal = [set(digits[key]) for key in sorted(digits.keys())]
    # nr = [sorted_signal.index(s) for s in values[idx]]
    for s in values[idx]:
        for idx, ss in enumerate(sorted_signal):
            if set(s) == ss:
                nr += str(idx)

    total += int(nr)

print('answer 2', total)
