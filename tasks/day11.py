from utils import read_input, grid as grid_util
from copy import deepcopy

raw = read_input.read_input_grid('day11')


def calculate_adjacent_occupied(grid, x, y):
    possible_positions = [
        (px, py) for (px, py) in
        [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)]
        if 0 <= py < len(grid) and 0 <= px < len(grid[0])
    ]
    result = 0
    for (px, py) in possible_positions:
        if grid[py][px] == '#':
            result += 1
    return result


def calculate_seen_occupied(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    result = 0
    for (dx, dy) in directions:
        distance = 1
        while True:
            px = distance * dx + x
            py = distance * dy + y
            if 0 <= py < len(grid) and 0 <= px < len(grid[0]):
                node = grid[py][px]
                if node == '#':
                    result += 1
                    break
                elif node == 'L':
                    break
                else:
                    distance += 1
            else:
                break
    return result


def calculate_next_state(pre_grid, is_part_one):
    result = deepcopy(pre_grid)
    for y in range(len(pre_grid)):
        for x in range(len((pre_grid[y]))):
            if is_part_one:
                if pre_grid[y][x] == 'L' and calculate_adjacent_occupied(pre_grid, x, y) == 0:
                    result[y][x] = '#'
                if pre_grid[y][x] == '#' and calculate_adjacent_occupied(pre_grid, x, y) >= 4:
                    result[y][x] = 'L'
            else:
                if pre_grid[y][x] == 'L' and calculate_seen_occupied(pre_grid, x, y) == 0:
                    result[y][x] = '#'
                if pre_grid[y][x] == '#' and calculate_seen_occupied(pre_grid, x, y) >= 5:
                    result[y][x] = 'L'
    return result


def calculate_final_state(is_part_one):
    current = deepcopy(raw)
    previous = []
    while current != previous:
        previous = deepcopy(current)
        current = calculate_next_state(current, is_part_one)
    return current


def part_one():
    final_state = calculate_final_state(True)
    print(f'The final occupied seats are {grid_util.calculate_total(final_state, "#")}. - 1')


def part_two():
    final_state = calculate_final_state(False)
    print(f'The final occupied seats are {grid_util.calculate_total(final_state, "#")}. - 2')


if __name__ == '__main__':
    part_one()
    part_two()
