import itertools as it
import hashlib

input = "reyedfim"
answer1 = ""
answer2 = [None] * 8
counter = it.count(0)
while True:
    i = next(counter)
    if hashlib.md5(f"{input}{i}".encode('utf-8')).hexdigest().startswith("00000"):
        hash = hashlib.md5(f"{input}{i}".encode('utf-8')).hexdigest()
        answer1 += hash[5]
        if hash[5].isdigit() and int(hash[5]) <= 7 and answer2[int(hash[5])] is None:
            answer2[int(hash[5])] = hash[6]
            if all([item is not None for item in answer2]) and len(answer1) >= 8:
                break

print("answer 1:", answer1[:8])
print("answer 2:", "".join(answer2))
