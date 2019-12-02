found = False
with open('input02.txt') as f:
    test = f.read()

memory = [int(s) for s in test.split(',')]
for noun in range(100):
    for verb in range(100):
        print(f'testing {noun=} {verb=}')
        codes = memory[:]
        codes[1] = noun
        codes[2] = verb
        counter = 0
        while found == False:
            opcode = codes[counter]
            if opcode == 99:
                if codes[0] == 19690720:
                    print(f'{noun=} {verb=} answer is {100 * noun + verb}')
                    found = True
                break
            elif opcode == 1:
                codes[codes[counter+3]] = codes[codes[counter+1]] + codes[codes[counter+2]]
            elif opcode == 2:
                codes[codes[counter+3]] = codes[codes[counter+1]] * codes[codes[counter+2]]
            else:
                print(f'invalid opcode {opcode} at {counter}')
                continue
            counter += 4

        if found:
            break

    if found:
        break



