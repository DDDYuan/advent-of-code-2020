from utils import read_input

raw = read_input.read_input_strings('day15')


def append_dict(current_dict, number, turn):
    if number in current_dict:
        turns = current_dict[number]
        if len(turns) == 1:
            current_dict[number] = (turns[0], turn)
        else:
            current_dict[number] = (turns[1], turn)
    else:
        current_dict[number] = (turn,)


def calculate_current_value(number_dict, previous):
    if previous in number_dict and len(number_dict[previous]) > 1:
        return number_dict[previous][1] - number_dict[previous][0]
    else:
        return 0


def calculate_specific_turn(turn):
    numbers_dict = dict()
    numbers = [int(number) for number in raw[0].split(',')]
    for i in range(len(numbers)):
        append_dict(numbers_dict, numbers[i], i + 1)
    previous_value = numbers[-1]
    current_turn = len(numbers) + 1
    while current_turn <= turn:
        current = calculate_current_value(numbers_dict, previous_value)
        append_dict(numbers_dict, current, current_turn)
        previous_value = current
        current_turn += 1
    print(f'Turn {turn} speak {previous_value}.')


def part_one():
    calculate_specific_turn(2020)


def part_two():
    calculate_specific_turn(30000000)


if __name__ == '__main__':
    part_one()
    part_two()
