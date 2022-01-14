import re
import sys
sys.setrecursionlimit(15000)

password = "hxbxwxba"
password = "abcdefgh"
password = "ghijklmn"
letters = "abcdefghijkmlnopqrstuvwxyz"
valid_letters = "abcdefghjkmnpqrstuvwxyz"

two_consecutive = list((a + b for a, b in zip(valid_letters, valid_letters)))
consecutive = [valid_letters[i - 3:i] for i in range(3, 27)]
print(list(two_consecutive))
print(consecutive)


def new_password(password: str) -> str:
    # if there is an i in password replace with j and the rest with a

    tmp = list(password[::-1])
    for idx, c in enumerate(tmp):
        if c == "z":
            tmp[idx] = "a"
        else:
            tmp[idx] = valid_letters[valid_letters.index(c) + 1]
            return "".join(reversed(tmp))


found = False
while not found:
    password = new_password(password)
    print(f"valid = {password}")

    if "i" in password:
        continue
    if "l" in password:
        continue
    if "o" in password:
        continue

    if not any(con in password for con in consecutive):
        print("no 3-s")
        continue

    once = False
    for two in two_consecutive:
        if two not in password:
            print("no 2-s")
            continue
        elif not once:
            print("found once")
            once = True
            continue
        else:
            found = True

print(password)
