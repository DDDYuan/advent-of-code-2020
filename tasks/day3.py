from utils import read_input


raw = read_input.read_input_strings('day3')


def calculate_steps(row_inc, column_inc):
    row = 0
    column = 0
    count = 0
    while row < len(raw):
        current = raw[row][column if column < len(raw[row]) else column % len(raw[row])]
        if current == '#':
            count += 1
        row += row_inc
        column += column_inc
    return count


def part_one():
    count = calculate_steps(1, 3)
    print(f'Trees number is {count}')


def part_two():
    count1 = calculate_steps(1, 1)
    count2 = calculate_steps(1, 3)
    count3 = calculate_steps(1, 5)
    count4 = calculate_steps(1, 7)
    count5 = calculate_steps(2, 1)
    print(f'Result number is {count1 * count2 * count3 * count4 * count5}')


if __name__ == '__main__':
    part_one()
    part_two()
