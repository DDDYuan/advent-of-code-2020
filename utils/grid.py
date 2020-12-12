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
