from copy import deepcopy
from typing import List


def get_adjacent_w_diagonal(m: List[List[int]], row: int, col: int) -> List[int]:
    adj = []
    # vertical
    if row > 0:
        adj.append((int(m[row - 1][col]), [row - 1, col]))
        # diagonal
        if col > 0:
            adj.append((int(m[row - 1][col - 1]), [row - 1, col - 1]))
        if col < len(m[row]) - 1:
            adj.append((int(m[row - 1][col + 1]), [row - 1, col + 1]))
    if row < len(m) - 1:
        adj.append((int(m[row + 1][col]), [row + 1, col]))
        if col > 0:
            adj.append((int(m[row + 1][col - 1]), [row + 1, col - 1]))
        if col < len(m[row]) - 1:
            adj.append((int(m[row + 1][col + 1]), [row + 1, col + 1]))
    # horizontal
    if col > 0:
        adj.append((int(m[row][col - 1]), [row, col - 1]))
    if col < len(m[row]) - 1:
        adj.append((int(m[row][col + 1]), [row, col + 1]))
    return adj


def tick(grid: List[List[int]]) -> List[List[int]]:
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            grid[i][j] += 1
    return grid


def propagate_flash(grid: List[List[int]]) -> List[List[int]]:
    flashed = []
    queue = []
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col > 9:  # flash
                flashed.append([i, j])
                queue.extend(get_adjacent_w_diagonal(grid, i, j))
    while queue:
        n = queue.pop(0)
        val, pos = n
        grid[pos[0]][pos[1]] += 1
        if grid[pos[0]][pos[1]] > 9 and pos not in flashed:  # flash neighbors
            flashed.append(pos)
            neighbours = get_adjacent_w_diagonal(grid, pos[0], pos[1])
            queue += neighbours

    return grid


def reset(grid):
    flashes = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col > 9:
                grid[i][j] = 0
                flashes += 1
    return grid, flashes


def do_step(grid: List[List[int]]) -> List[List[int]]:
    grid = tick(grid)
    grid = propagate_flash(grid)
    grid, num_flashes = reset(grid)
    return grid, num_flashes


def solution1(grid: List[List[int]], iterations: int):
    score = 0
    for _ in range(iterations):
        grid, num_flashes = do_step(grid)
        score += num_flashes
    return score


def solution2(grid):
    steps = 0
    while True:
        grid, num_flashes = do_step(grid)
        steps += 1
        if all([all([val == 0 for val in row]) for row in grid]):
            break
    return steps


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
        data = []
        for line in f:
            data.append([int(n) for n in line.strip()])

    res1 = solution1(deepcopy(data), 100)
    print(f'Solution Part 1: {res1}')

    res2 = solution2(deepcopy(data))
    print(f'Solution Part 2: {res2}')
