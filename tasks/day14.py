from utils import read_input
import copy

raw = read_input.read_input_strings('day14')


def parse_mask(line):
    raw_mask = list(reversed(line.split(' = ')[1]))
    mask = []
    for i in range(len(raw_mask)):
        if raw_mask[i] != 'X':
            mask.append((i, raw_mask[i]))
    return mask


def parse_mem(line):
    mem_address, value = line.split(' = ')
    address = mem_address.split('[')[1][:-1]
    return int(address), int(value)


def make_36bit_binary(decimal):
    return format(int(bin(decimal)[2:]), '036d')


def apply_mask(mask, value):
    value_list = list(reversed(make_36bit_binary(value)))
    for (bit, binary) in mask:
        value_list[bit] = binary
    return int(''.join(reversed(value_list)), 2)


def apply_address_mask(mask, address):
    addresses = [[]]
    value_list = list(make_36bit_binary(address))
    for i in range(len(mask)):
        if mask[i] == '1':
            for a in addresses:
                a.append('1')
        elif mask[i] == '0':
            for a in addresses:
                a.append(value_list[i])
        else:
            addresses = copy.deepcopy(addresses) + copy.deepcopy(addresses)
            for a in addresses[:(len(addresses)//2)]:
                a.append('0')
            for a in addresses[(len(addresses)//2):]:
                a.append('1')
    return [int(''.join(a), 2) for a in addresses]


def part_one():
    memory = dict()
    mask = []
    for line in raw:
        if line.startswith('mask'):
            mask = parse_mask(line)
        else:
            address, raw_value = parse_mem(line)
            value = apply_mask(mask, raw_value)
            memory[address] = value
    print(f'The sum of memory is {sum(memory.values())}')


def part_two():
    memory = dict()
    mask = ''
    for line in raw:
        if line.startswith('mask'):
            mask = line[7:]
        else:
            address, raw_value = parse_mem(line)
            addresses = apply_address_mask(mask, address)
            for a in addresses:
                memory[a] = raw_value
    print(f'The sum of memory is {sum(memory.values())}')


if __name__ == '__main__':
    part_one()
    part_two()
