from utils import read_input


raw = read_input.read_input_strings('day5')


def calculate_seat_id(seat_string):
    row = seat_string[:7].replace('F', '0').replace('B', '1')
    column = seat_string[-3:].replace('L', '0').replace('R', '1')
    return int(row, 2) * 8 + int(column, 2)


def part_one():
    highest = max([calculate_seat_id(seat) for seat in raw])
    print(f'Highest seat id is {highest}')


def part_two():
    ids = sorted([calculate_seat_id(seat) for seat in raw])
    for index in range(len(ids)):
        if ids[index] - ids[0] != index:
            print(f'Your seat number is {ids[index] - 1}')
            break


if __name__ == '__main__':
    part_one()
    part_two()
