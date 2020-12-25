import copy


def print_grid(grid):
    for row in grid:
        [print(e, end='') for e in row]
        print('')


def calculate_total(grid, target):
    result = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == target:
                result += 1
    return result


def find_first(grid, target):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == target:
                return x, y
    return None, None


def expand_grid(grid, element=''):
    new_grid = copy.deepcopy(grid)
    new_row = [element] * (len(new_grid[0]) + 2)
    result = [new_row.copy()]
    for row in new_grid:
        result.append([element] + row + [element])
    result.append(new_row.copy())
    return result


def create_grid(w, h, element=''):
    return [[element for _ in range(w)] for _ in range(h)]


def parse_grid(lines):
    return [[element for element in line] for line in lines]
