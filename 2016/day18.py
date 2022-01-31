def count_safe_tiles(rows):
    traps = ["^^.", ".^^", "^..", "..^"]
    row = open("input18.txt").readline().strip()
    safe_tally = 0
    for i in range(rows):
        safe_tally += row.count(".")
        row = "." + row + "."
        new_traps = []
        for j in range(len(row) - 2):
            # print(row[j:j + 3], end=" | ")
            new_traps.append("^" if row[j:j+3] in traps else ".")
        row = "".join(new_traps)
    return safe_tally


print("answer 1:", count_safe_tiles(40))
print("answer 2:", count_safe_tiles(400_000))
