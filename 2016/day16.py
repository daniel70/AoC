def checksum(code, length):
    while len(code) < length:
        code += "0" + "".join([str(int(not(int(c)))) for c in reversed(code)])

    code = code[:length]
    while True:
        code = "".join(["1" if code[i:i + 2] in ["00", "11"] else "0" for i in range(0, len(code), 2)])
        if len(code) % 2 == 1:
            break

    return code


def main():
    code = "10011111011011001"
    length = 272
    print("answer 1:", checksum(code, length))
    length = 35651584
    print("answer 2:", checksum(code, length))


if __name__ == "__main__":
    main()
