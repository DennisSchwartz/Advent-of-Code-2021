from operator import add
from functools import reduce


def solution1(positions):
    # naive
    lowest = min(positions)
    highest = max(positions)
    lowest_cost = float('inf')
    for line in range(lowest, highest + 1):
        cost = 0
        for p in positions:
            cost += abs(line - p)
            if cost > lowest_cost:
                break
        if cost < lowest_cost:
            lowest_cost = cost
    return lowest_cost


def solution2(positions):
    lowest = min(positions)
    highest = max(positions)
    lowest_cost = float('inf')
    for line in range(lowest, highest + 1):
        cost = 0
        for p in positions:
            diff = abs(line - p)
            prod = reduce(add, list(range(1, diff + 1)), 0)
            cost += prod
            if cost > lowest_cost:
                break
        if cost < lowest_cost:
            lowest_cost = cost
    return lowest_cost


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = list(map(int, f.readline().strip().split(',')))

    res1 = solution1(data)
    print(f'Solution Part 1: {res1}')

    res2 = solution2(data)
    print(f'Solution Part 2: {res2}')
