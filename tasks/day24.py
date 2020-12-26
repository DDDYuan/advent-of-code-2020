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


def calculate_next(current_points):
    max_x = max([x for (x, y) in current_points])
    min_x = min([x for (x, y) in current_points])
    max_y = max([y for (x, y) in current_points])
    min_y = min([y for (x, y) in current_points])
    result = []
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            adj_blacks = len([1 for (x_diff, y_diff) in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1)]
                              if (x + x_diff, y + y_diff) in current_points])
            if (x, y) in current_points and 0 < adj_blacks <= 2:
                result.append((x, y))
            if (x, y) not in current_points and adj_blacks == 2:
                result.append((x, y))
    return result


def part_two():
    commands = [parse_command(raw_command) for raw_command in raw]
    final = [move_to(command) for command in commands]
    times_dict = calculate_times_dict(final)
    black_tiles = [point for point in times_dict if times_dict[point] % 2 == 1]
    days = 100
    while days > 0:
        black_tiles = calculate_next(black_tiles)
        days -= 1
    print(len(black_tiles))


if __name__ == '__main__':
    part_one()
    part_two()
