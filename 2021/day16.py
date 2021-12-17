from math import prod


def calculate_version(packet, total, values):
    if all([c == "0" for c in packet]):
        return "", total, values

    version, type_id, packet = int(packet[:3], 2), int(packet[3:6], 2), packet[6:]

    match type_id:
        case 4:  # literal value
            more, value, packet = int(packet[:1], 2), packet[1:5], packet[5:]
            while more:
                more, t, packet = int(packet[:1], 2), packet[1:5], packet[5:]
                value += t
            values.append(int(value, 2))

        case _:  # operator
            length_type_id, packet = int(packet[:1], 2), packet[1:]
            if length_type_id == 0:  # 15 bits subpackage, length
                sub_packets_length, packet = int(packet[:15], 2), packet[15:]
                sub_packets, packet = packet[:sub_packets_length], packet[sub_packets_length:]
                temp, packet = packet, sub_packets
                ops = []
                while packet:
                    packet, version, ops = calculate_version(packet, version, ops)
                packet = temp

            if length_type_id == 1:  # 11 bits subpackage, loop
                nr_of_sub_packets, packet = int(packet[:11], 2), packet[11:]
                ops = []
                for i in range(nr_of_sub_packets):
                    # sub_packet, packet = packet[:11 * nr_of_sub_packets], packet[11 * nr_of_sub_packets:]
                    packet, version, ops = calculate_version(packet, version, ops)

            if type_id == 0:
                values.append(sum(ops))
            elif type_id == 1:
                values.append(prod(ops))
            elif type_id == 2:
                values.append(min(ops))
            elif type_id == 3:
                values.append(max(ops))
            elif type_id == 5:
                values.append(int(ops[0] > ops[1]))
            elif type_id == 6:
                values.append(int(ops[0] < ops[1]))
            elif type_id == 7:
                values.append(int(ops[0] == ops[1]))

    return packet, total + version, values


with open("input16.txt") as f:
    bits = f.readline().strip()

bits = "1" + bits
packet = f"{int(bits, 16):>b}"
packet = packet[1:]
_, total, values = calculate_version(packet, 0, [])
print('answer 1:', total)
print('answer 2:', values[0])
