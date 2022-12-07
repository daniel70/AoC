from collections import defaultdict
import pathlib

total_disk_space = 70_000_000
needed_disk_space = 30_000_000
used_disk_space = 0

instructions = []
with open('input07.txt') as f:
    for line in f:
        line = line.strip()
        instructions.append(line)

pwd = pathlib.Path()
fs = {}
for instruction in instructions:
    command = instruction.split()
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] == "/":
                pwd = pathlib.Path(pwd.root)
            elif command[2] == "..":
                pwd = pathlib.Path(pwd.parent)
            else:
                pwd = pwd / command[2]

    else:  # dir mode
        dir_or_size, file_name = instruction.split()
        size = 0 if dir_or_size == "dir" else int(dir_or_size)
        used_disk_space += size
        fs[pwd / file_name] = size

dirs = defaultdict(int)
root = pathlib.Path()
for file_name, size in fs.items():
    if size > 0:
        while file_name.parent != root:
            file_name = pathlib.Path(file_name.parent)
            dirs[file_name] += size

total = sum(size for size in dirs.values() if size <= 100_000)
print("answer 1:", total)

min_size_to_delete = needed_disk_space - (total_disk_space - used_disk_space)
size_to_delete = [d for d in sorted(dirs.values()) if d >= min_size_to_delete][0]
print("answer 2:", size_to_delete)
