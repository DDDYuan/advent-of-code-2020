from utils import read_input
import math

raw = read_input.read_input_strings('day13')


def part_one():
    start_time = int(raw[0])
    bus_ids = [int(number) for number in raw[1].split(',') if number != 'x']
    wait_time = 0
    found = False
    while not found:
        for bus_id in bus_ids:
            if (start_time + wait_time) % bus_id == 0:
                print(f'Bus id {bus_id} depart at {start_time + wait_time}, '
                      f'waiting {wait_time}, result is {bus_id * wait_time}.')
                found = True
        wait_time += 1


def part_two():
    raw_ids = raw[1].split(',')
    ids_offsets = [(int(number), int(number) - raw_ids.index(number) % int(number))
                   for number in raw_ids if number != 'x']
    # 孙子定理
    common_multiple = math.prod([number for (number, offset) in ids_offsets])
    base_sum = 0
    for (current_number, current_offset) in ids_offsets:
        others_multiple = common_multiple // current_number
        base = others_multiple
        while base % current_number != 1:
            base += others_multiple
        base_sum += base * current_offset
    print(f'The minimal timestamp is {base_sum % common_multiple}')


if __name__ == '__main__':
    part_one()
    part_two()
