from itertools import count

rules = {}
seen = {}
total_prepend = 0

initial_state, _, *instructions = open("input12.txt").readlines()
initial_state = initial_state[15:].strip()
for line in instructions:
    line = line.strip()
    from_, to_ = line.split(" => ")
    rules[from_] = to_


pots = initial_state.strip(".")
for gen in count(1):
    # we lose 2 leading dots per round because LLCRR
    total_prepend -= 2

    # make sure that we have 5 leading and 5 pending dots, keep track of how many leading dots we have added
    prepend = 5 - pots.index("#")
    if prepend > 0:
        total_prepend += prepend
        pots = "." * prepend + pots
    append = 5 - pots[:-6:-1].index("#")
    if append > 0:
        pots += "." * append

    new_state = []
    for i in range(len(pots) - 5):
        if pots[i:i + 5] not in rules:
            new_state.append(".")
        else:
            new_state.append(rules[pots[i:i + 5]])
    pots = "".join(new_state)

    sum_pot = sum([idx - total_prepend for idx, char in enumerate(pots) if char == "#"])

    if gen == 20:
        print("answer 1:", sum_pot)

    # search for a repeat (glider)
    stripped = pots.strip(".")
    if stripped in seen:
        prev_gen, prev_sum_pot = seen[stripped]
        # we start repeating now, for 50_000_000_000 - gen rows
        # each gen - prev_gen we gain sum_pot - prev_sum_pot points
        # we add the current points to that
        print("answer 2:", (50_000_000_000 - gen) // (gen - prev_gen) * (sum_pot - prev_sum_pot) + sum_pot)
        break

    seen[stripped] = (gen, sum_pot)
