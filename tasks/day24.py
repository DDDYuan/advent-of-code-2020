from utils import read_input

raw = read_input.read_input_strings('day24')


def parse_command(raw_command):
    i = 0
    result = []
    while i < len(raw_command):
        current = raw_command[i]
        if current == 's' or current == 'n':
            result.append(raw_command[i:i+2])
            i += 2
        else:
            result.append(raw_command[i])
            i += 1
    return result


def move_to(commands):
    x = 0
    y = 0
    for command in commands:
        if command == 'nw':
            y += 1
        if command == 'se':
            y -= 1
        if command == 'w':
            x -= 1
        if command == 'e':
            x += 1
        if command == 'ne':
            y += 1
            x += 1
        if command == 'sw':
            y -= 1
            x -= 1
    return x, y


def calculate_times_dict(points):
    result = dict()
    for point in points:
        if result.get(point) is not None:
            result[point] = result[point] + 1
        else:
            result[point] = 1
    return result


def part_one():
    commands = [parse_command(raw_command) for raw_command in raw]
    final = [move_to(command) for command in commands]
    times_dict = calculate_times_dict(final)
    print(len([point for point in times_dict if times_dict[point] % 2 == 1]))


def part_two():
    pass


if __name__ == '__main__':
    part_one()
    part_two()
