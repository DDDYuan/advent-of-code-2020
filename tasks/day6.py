from utils import read_input


raw = read_input.read_input_strings_groups('day6')


def count_chars(line):
    return len(set(line))


def count_intersection(lines):
    return len(set(lines[0]).intersection(*[set(line) for line in lines]))


def part_one():
    count = sum([count_chars(''.join(group)) for group in raw])
    print(f'The count is {count}')


def part_two():
    count = sum([count_intersection(group) for group in raw])
    print(f'The count is {count}')


if __name__ == '__main__':
    part_one()
    part_two()
