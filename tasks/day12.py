from utils import read_input

raw = read_input.read_input_strings('day12')


def parse_command(command):
    return command[0], int(command[1:])


def move(instruction, value, facing):
    if instruction == 'L':
        return 0, 0, value
    if instruction == 'R':
        return 0, 0, -value
    if instruction == 'N':
        return 0, value, 0
    if instruction == 'S':
        return 0, -value, 0
    if instruction == 'E':
        return value, 0, 0
    if instruction == 'W':
        return -value, 0, 0
    if instruction == 'F':
        direction = facing % 360
        if direction == 0:
            return value, 0, 0
        if direction == 90:
            return 0, value, 0
        if direction == 180:
            return -value, 0, 0
        if direction == 270:
            return 0, -value, 0


def part_one():
    x = 0
    y = 0
    facing = 0
    for command in raw:
        instruction, value = parse_command(command)
        x_diff, y_diff, facing_diff = move(instruction, value, facing)
        x += x_diff
        y += y_diff
        facing += facing_diff
    print(f'The final position is {x}, {y} facing {facing}, manhattan distance is {abs(x) + abs(y)}')


def move_waypoint(instruction, value, w_x, w_y):
    if instruction == 'N':
        return w_x, w_y + value
    if instruction == 'S':
        return w_x, w_y - value
    if instruction == 'E':
        return w_x + value, w_y
    if instruction == 'W':
        return w_x - value, w_y
    if instruction == 'L':
        direction = value % 360
        if direction == 90:
            return -w_y, w_x
        if direction == 180:
            return -w_x, -w_y
        if direction == 270:
            return w_y, -w_x
    if instruction == 'R':
        direction = value % 360
        if direction == 90:
            return w_y, -w_x
        if direction == 180:
            return -w_x, -w_y
        if direction == 270:
            return -w_y, w_x


def part_two():
    x = 0
    y = 0
    w_x = 10
    w_y = 1
    for command in raw:
        instruction, value = parse_command(command)
        if instruction == 'F':
            x += w_x * value
            y += w_y * value
        else:
            w_x, w_y = move_waypoint(instruction, value, w_x, w_y)
    print(f'The final position is {x}, {y}, manhattan distance is {abs(x) + abs(y)}')


if __name__ == '__main__':
    part_one()
    part_two()
