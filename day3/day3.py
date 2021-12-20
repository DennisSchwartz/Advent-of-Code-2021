from typing import List
import pandas as pd

def get_bit_counts(nums: List[str]) -> List[List[int]]:
    bitcounts = []
    for i in range(len(nums[0])):
        bitcounts.append([0, 0])
    for bin in nums:
        for j, bit in enumerate(bin):
            bitcounts[j][int(bit)] += 1
    return bitcounts

def solution1(cmds):
    bitcounts = get_bit_counts(cmds)
    gamma = ''
    epsilon = ''
    for b in bitcounts:
        if b[0] > b[1]:
            gamma += '0'
            epsilon += '1'
        if b[0] < b[1]:
            gamma += '1'
            epsilon += '0'
        assert b[0] != b[1], f'Not most common bit? {bitcounts}'
    return int(gamma, 2) * int(epsilon, 2)


def df2int(df: pd.DataFrame) -> int:
    assert len(df) == 1
    return int(''.join(list(df.iloc[0])), 2)


def solution2(cmds):
    ox = pd.DataFrame([list(cmd) for cmd in cmds])
    co2 = ox.copy()

    for col in range(ox.shape[1]):
        if len(ox) > 1:
            mode_ox = ox[col].mode()
            ox = ox[ox[col] == mode_ox.max()]
        if len(co2) > 1:
            mode_co2 = co2[col].mode()
            co2 = co2[co2[col] != mode_co2.max()]

    ox.reset_index(inplace=True, drop=True)
    co2.reset_index(inplace=True, drop=True)
    return df2int(ox) * df2int(co2)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f]

    res1 = solution1(data)
    print(f'Solution Part 1: {res1}')

    res2 = solution2(data)
    print(f'Solution Part 2: {res2}')
