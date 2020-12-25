from utils import read_input, grid
import math

raw = read_input.read_input_strings_groups('day20')


def calculate_binary(row):
    result = []
    for element in row:
        if element == '#':
            result.append('1')
        else:
            result.append('0')
    str1 = ''.join(result)
    str2 = ''.join(reversed(result))
    return int(str1, 2), int(str2, 2)


def parse_tile(raw_tile):
    tile_id = raw_tile[0][5:9]
    tile_grid = grid.parse_grid(raw_tile[1:])
    return int(tile_id), tile_grid


def calculate_single_edges_count(current_index, all_edges):
    found1 = False
    found2 = False
    found3 = False
    found4 = False
    tile_id, (num1, _), (num2, _), (num3, _), (num4, _) = all_edges[current_index]
    for i in range(len(all_edges)):
        if i != current_index:
            c_id, (c11, c12), (c21, c22), (c31, c32), (c41, c42) = all_edges[i]
            if num1 in [c11, c12, c21, c22, c31, c32, c41, c42]:
                found1 = True
            if num2 in [c11, c12, c21, c22, c31, c32, c41, c42]:
                found2 = True
            if num3 in [c11, c12, c21, c22, c31, c32, c41, c42]:
                found3 = True
            if num4 in [c11, c12, c21, c22, c31, c32, c41, c42]:
                found4 = True
    return len([1 for found in [found1, found2, found3, found4] if found is False])


def part_one():
    tiles = [parse_tile(raw_tile) for raw_tile in raw]
    tile_edges = []
    for tile_id, tile_grid in tiles:
        first_row_num1, first_row_num2 = calculate_binary(tile_grid[0])
        last_row_num1, last_row_num2 = calculate_binary(tile_grid[-1])
        left_row_num1, left_row_num2 = calculate_binary([tile_grid[i][0] for i in range(len(tile_grid))])
        right_row_num1, right_row_num2 = calculate_binary([tile_grid[i][-1] for i in range(len(tile_grid))])
        tile_edges.append((tile_id,
                           (first_row_num1, first_row_num2),
                           (last_row_num1, last_row_num2),
                           (left_row_num1, left_row_num2),
                           (right_row_num1, right_row_num2)))
    result = []
    for i in range(len(tile_edges)):
        tile_id, _, _, _, _ = tile_edges[i]
        result.append((tile_id, calculate_single_edges_count(i, tile_edges)))
    corner_ids = [tile_id for (tile_id, single_edges) in result if single_edges == 2]
    print(corner_ids)
    print(f'The ids multiply to be {math.prod(corner_ids)}.')


def part_two():
    pass


if __name__ == '__main__':
    part_one()
    part_two()
