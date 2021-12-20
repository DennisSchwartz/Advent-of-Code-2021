from typing import List

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


def solution2(cmds):
    bitcounts = get_bit_counts(cmds)
    print(bitcounts)
    ox = cmds
    co2 = cmds
    res_ox = None
    res_co2 = None
    for bit, counts in enumerate(bitcounts):
        most_common = '1' if counts[1] >= counts[0] else '0'
        if not res_ox:
            ox = [b for b in ox if b[bit] == most_common]
        if not res_co2:
            co2 = [b for b in co2 if b[bit] != most_common]
        if len(ox) == 1:
            res_ox = ox[0]
        if len(co2) == 1:
            res_co2 = co2[0]
        if res_ox and res_co2:
            break
    print(res_ox, res_co2)
    print(int(res_ox, 2) * int(res_co2, 2), int(res_ox, 2), int(res_co2, 2))
    return int(res_ox, 2) * int(res_co2, 2)



if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        data = [line.strip() for line in f]

    res1 = solution1(data)
    print(f'Solution Part 1: {res1}')

    res2 = solution2(data)
    print(f'Solution Part 2: {res2}')
