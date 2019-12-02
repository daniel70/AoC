test1 = '1,9,10,3,2,3,11,0,99,30,40,50'
test2 = '2,3,0,3,99'
test3 = '1,0,0,0,99'
test4 = '2,4,4,5,99,0'
test5 = '1,1,1,4,99,5,6,0,99'
with open('input02.txt') as f:
    test = f.read()

codes = [int(s) for s in test.split(',')]
codes[1] = 12
codes[2] = 2
counter = 0
while True:
    opcode = codes[counter]
    if opcode == 99:
        break
    elif opcode == 1:
        codes[codes[counter+3]] = codes[codes[counter+1]] + codes[codes[counter+2]]
    elif opcode == 2:
        codes[codes[counter+3]] = codes[codes[counter+1]] * codes[codes[counter+2]]
    else:
        print(f'invalid opcode {opcode} at {counter}')
    counter += 4

print(codes[0])