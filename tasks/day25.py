from utils import read_input

raw = read_input.read_input_strings('day25')


def calculate_next(current, subject):
    return current * subject % 20201227


def calculate_loops(subject, loops):
    current = 1
    while loops != 0:
        current = calculate_next(current, subject)
        loops -= 1
    return current


def get_loop_size(target):
    current = 1
    loop_size = 0
    while current != target:
        loop_size += 1
        current = calculate_next(current, 7)
    return loop_size


def part_one():
    card = int(raw[0])
    door = int(raw[1])
    card_loop = get_loop_size(card)
    print(calculate_loops(door, card_loop))


def part_two():
    pass


if __name__ == '__main__':
    part_one()
    part_two()
