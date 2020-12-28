import math
import re


def transposed(tile):
    return list(''.join(row) for row in zip(*tile))


def reversed_tile(tile):
    return [''.join(reversed(row)) for row in tile]


def rotations(tile):
    ans = [tile]
    for _ in range(3):
        ans.append(reversed_tile(transposed(ans[-1])))
    return ans


def group(tile):
    return rotations(tile) + rotations(transposed(tile))


tiles = {}
for tile in open('../inputs/day20').read().split('\n\n'):
    lines = tile.strip().split('\n')
    tile_id = int(re.fullmatch(r'Tile (\d+):', lines[0]).group(1))
    rows = lines[1:]
    tiles[tile_id] = group(rows)

n = int(math.sqrt(len(tiles)))
arranged = [[0] * n for _ in range(n)]
stack = list(reversed(list((r, c) for c in range(n) for r in range(n))))


def solve():
    if not stack:
        print(arranged[0][0][0] * arranged[-1][0][0] * arranged[0][-1][0] *
              arranged[-1][-1][0])
        return True
    (r, c) = stack.pop()
    for tile_id in list(tiles):
        tile_group = tiles[tile_id]
        del tiles[tile_id]
        for tile in tile_group:
            if r > 0:
                if arranged[r - 1][c][1][-1] != tile[0]:
                    continue
            if c > 0:
                if list(row[-1] for row in arranged[r][c - 1][1]) != list(
                        row[0] for row in tile):
                    continue
            arranged[r][c] = (tile_id, tile)
            if solve():
                return True
        tiles[tile_id] = tile_group
    stack.append((r, c))


solve()


def remove_border(tile):
    return [row[1:-1] for row in tile[1:-1]]


board = [[remove_border(tile[1]) for tile in row] for row in arranged]
tile_n = len(board[0][0])


def get(r, c):
    return board[r // tile_n][c // tile_n][r % tile_n][c % tile_n]


board = [
    ''.join(get(r, c) for c in range(n * tile_n)) for r in range(n * tile_n)
]
for pattern in group(
        ['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']):
    matches = 0
    for dr in range(len(board) - len(pattern) + 1):
        for dc in range(len(board[0]) - len(pattern[0]) + 1):
            matches += all(pattern[r][c] == ' ' or board[r + dr][c + dc] == '#'
                           for r in range(len(pattern))
                           for c in range(len(pattern[0])))
    if matches:
        print(''.join(board).count('#') -
              ''.join(pattern).count('#') * matches)
        break
