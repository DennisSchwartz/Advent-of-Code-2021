from functools import reduce
from operator import mul
from typing import List


def get_adjacent_no_diagonal(m: List[List[int]], row: int, col: int) -> List[int]:
    adj = []
    # vertical
    if row > 0:
        adj.append((int(m[row - 1][col]), [row - 1, col]))
    if row < len(m) - 1:
        adj.append((int(m[row + 1][col]), [row + 1, col]))
    # horizontal
    if col > 0:
        adj.append((int(m[row][col - 1]), [row, col - 1]))
    if col < len(m[row]) - 1:
        adj.append((int(m[row][col + 1]), [row, col + 1]))
    return adj


def get_basin(m: List[List[int]], row: int, col: int) -> List[int]:
    basin = [(m[row][col], [row, col])]
    adj = get_adjacent_no_diagonal(m, row, col)
    basin += adj
    pool = adj
    visited = []
    while pool:
        tup = pool.pop()
        val, pos = tup
        if val < 9 and pos not in visited:
            if pos not in [n[1] for n in basin]:
                basin.append(tup)
            pool += get_adjacent_no_diagonal(m, *pos)
            visited.append(pos)

    return basin


def solution1(grid):
    low_points = []
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            neighbours = get_adjacent_no_diagonal(grid, i, j)
            if min([n[0] for n in neighbours]) > int(num):
                low_points.append((int(num), [i, j]))

    return low_points, sum(map(lambda x: int(x[0]) + 1, low_points))


def solution2(grid, low_points):
    basins = []
    for lp in low_points:
        basins.append(get_basin(grid, *lp[1]))

    srt_basins = sorted(basins, reverse=True, key=len)
    biggest_size = list(map(len, srt_basins[:3]))
    return reduce((lambda x, y: x * y), biggest_size)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [list(line.strip()) for line in f]

    lps, lpsum = solution1(data)
    print(f'Solution Part 1: {lpsum}')

    res2 = solution2(data, lps)
    print(f'Solution Part 2: {res2}')
