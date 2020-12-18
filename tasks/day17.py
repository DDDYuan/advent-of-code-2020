from utils import read_input
from utils import grid
from copy import deepcopy

raw = read_input.read_input_grid('day17')


def calculate_active(flats):
    result = 0
    for flat in flats:
        result += grid.calculate_total(flat, '#')
    return result


def calculate_neighbor_active(flats, f_i, r_i, c_i):
    result = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                if i != 0 or j != 0 or k != 0:
                    f = f_i + i
                    r = r_i + j
                    c = c_i + k
                    if f >= 0 and r >= 0 and c >= 0:
                        if f < len(flats) and r < len(flats[i]) and c < len(flats[i][j]):
                            if flats[f][r][c] == '#':
                                result += 1
    return result


def calculate_hyper_neighbor_active(dimensions, d_i, f_i, r_i, c_i):
    result = 0
    for v in [-1, 0, 1]:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    if v != 0 or i != 0 or j != 0 or k != 0:
                        d = d_i + v
                        f = f_i + i
                        r = r_i + j
                        c = c_i + k
                        if d >= 0 and f >= 0 and r >= 0 and c >= 0:
                            if d < len(dimensions) and f < len(dimensions[d])\
                                    and r < len(dimensions[d][i]) and c < len(dimensions[d][i][j]):
                                if dimensions[d][f][r][c] == '#':
                                    result += 1
    return result


def calculate_next(flats):
    original = deepcopy(flats)
    for f_i in range(len(flats)):
        for r_i in range(len(flats[f_i])):
            for c_i in range(len(flats[f_i][r_i])):
                neighbor_active = calculate_neighbor_active(original, f_i, r_i, c_i)
                if flats[f_i][r_i][c_i] == '#':
                    if 2 <= neighbor_active <= 3:
                        flats[f_i][r_i][c_i] = '#'
                    else:
                        flats[f_i][r_i][c_i] = '.'
                else:
                    if neighbor_active == 3:
                        flats[f_i][r_i][c_i] = '#'
                    else:
                        flats[f_i][r_i][c_i] = '.'


def calculate_hyper_next(dimensions):
    original = deepcopy(dimensions)
    for d_i in range(len(dimensions)):
        for f_i in range(len(dimensions[d_i])):
            for r_i in range(len(dimensions[d_i][f_i])):
                for c_i in range(len(dimensions[d_i][f_i][r_i])):
                    neighbor_active = calculate_hyper_neighbor_active(original, d_i, f_i, r_i, c_i)
                    if dimensions[d_i][f_i][r_i][c_i] == '#':
                        if 2 <= neighbor_active <= 3:
                            dimensions[d_i][f_i][r_i][c_i] = '#'
                        else:
                            dimensions[d_i][f_i][r_i][c_i] = '.'
                    else:
                        if neighbor_active == 3:
                            dimensions[d_i][f_i][r_i][c_i] = '#'
                        else:
                            dimensions[d_i][f_i][r_i][c_i] = '.'


def part_one():
    flats = [raw]
    for _ in range(6):
        height = len(flats[0])
        width = len(flats[0][0])
        flats.insert(0, grid.create_grid(width, height, '.'))
        flats.append(grid.create_grid(width, height, '.'))
        for i in range(len(flats)):
            flats[i] = grid.expand_grid(flats[i], '.')
        calculate_next(flats)
    print(f'The final active cubes number is {calculate_active(flats)}.')


def part_two():
    dimensions = [[raw]]
    for _ in range(6):
        height = len(dimensions[0][0])
        width = len(dimensions[0][0][0])
        for flats in dimensions:
            flats.insert(0, grid.create_grid(width, height, '.'))
            flats.append(grid.create_grid(width, height, '.'))
        depth = len(dimensions[0])
        dimensions.insert(0, [grid.create_grid(width, height, '.') for _ in range(depth)])
        dimensions.append([grid.create_grid(width, height, '.') for _ in range(depth)])
        for i in range(len(dimensions)):
            for j in range(len(dimensions[i])):
                dimensions[i][j] = grid.expand_grid(dimensions[i][j], '.')
        calculate_hyper_next(dimensions)
    print(f'The final active cubes number is {sum([calculate_active(flats) for flats in dimensions])}.')


if __name__ == '__main__':
    part_one()
    part_two()
