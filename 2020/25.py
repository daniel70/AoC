
with open("input25.txt") as f:
    card_pk = int(f.readline().strip())
    door_pk = int(f.readline().strip())

# card_pk = 5764801; door_pk = 17807724
subject_number = 7


def transform(pk):
    secret_loop_size = 0
    value = 1
    while value != pk:
        value = value * subject_number
        value = value % 20201227
        secret_loop_size += 1

    return secret_loop_size

card_loop_size = transform(card_pk)
door_loop_size = transform(door_pk)

value = 1
for i in range(door_loop_size):
    value = value * card_pk
    value = value % 20201227

print(value)

value = 1
for i in range(card_loop_size):
    value = value * door_pk
    value = value % 20201227

print(value)
