import hashlib
from itertools import count
key = "bgvyzdsv"


def find_hash(start_with):
    for i in count():
        if hashlib.md5(f"{key}{i}".encode('utf-8')).hexdigest().startswith(start_with):
            break
    return i

print(find_hash("00000"))
print(find_hash("000000"))