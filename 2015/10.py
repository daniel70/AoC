nr = "1113222113"
for i in range(50):
    prev = nr[0]
    new_nr = ""
    count = 0
    for j, c in enumerate(nr):
        if c != prev:
            new_nr += str(count) + prev
            count = 1
        else:
            count += 1
        prev = c

    nr = new_nr + str(count) + c
    if i == 39:
        print(len(nr))

print(len(nr))