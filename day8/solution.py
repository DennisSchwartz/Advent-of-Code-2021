from typing import List


def solution1(lines):
    unique_lengths = [2, 3, 4, 7]
    count = 0
    for line in lines:
        signals, codes = line.split(' | ')
        for code in codes.split():
            if len(set(code)) in unique_lengths:
                count += 1
    return count


def sort_string(s):
    return ''.join(sorted(s))


def get_strings_w_length(lis: List[str], n: int) -> set:
    res = []
    for el in lis:
        if len(el) == n:
            res.append(set(el))
    return res


def assign(inputs):
    mapping = {
        'a': set(),
        'b': set(),
        'c': set(),
        'd': set(),
        'e': set(),
        'f': set(),
        'g': set(),
    }
    # len 2
    # c & f
    one = get_strings_w_length(inputs, 2)[0]
    mapping['c'] = one
    mapping['f'] = one
    # len 3
    seven = get_strings_w_length(inputs, 3)[0]
    mapping['a'] = seven - mapping['c']
    # len 4
    four = get_strings_w_length(inputs, 4)[0]
    mapping['b'] = four - mapping['c']
    mapping['d'] = four - mapping['c']
    # len 5
    len5 = get_strings_w_length(inputs, 5)
    inter = set.intersection(*len5)
    mapping['g'] = inter - mapping['a']
    mapping['d'] = mapping['d'].intersection(inter)
    mapping['g'] = mapping['g'] - mapping['g'].intersection(mapping['d'])
    mapping['b'] = mapping['b'] - mapping['b'].intersection(mapping['d'])
    reduced_len5 = [el-inter for el in len5]
    five = [el for el in reduced_len5 if len(mapping['b'].intersection(el)) > 0]
    five = five[0] - mapping['b']
    mapping['f'] = five
    mapping['c'] = mapping['c'] - mapping['c'].intersection(mapping['f'])
    two = [el for el in reduced_len5 if len(mapping['f'].intersection(el)) == 0]
    mapping['e'] = two[0] - mapping['c']

    return {list(v)[0]: k for k, v in mapping.items()}


def translate_string(mapping, s: str) -> str:
    res = [mapping[char] for char in s]
    return ''.join(sorted(res))


def solution2(lines):
    numbers_map = {
        'abcefg': '0',
        'cf': '1',
        'acdeg': '2',
        'acdfg': '3',
        'bcdf': '4',
        'abdfg': '5',
        'abdefg': '6',
        'acf': '7',
        'abcdefg': '8',
        'abcdfg': '9',
    }

    total = 0
    for line in lines:
        inputs, outputs = line.split(' | ')
        mapping = assign(inputs.split())
        res = ''
        for o in outputs.split():
            translated = translate_string(mapping, o)
            res += numbers_map[translated]
        num = int(res)
        total += num
    return total


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f]

    res1 = solution1(data)
    print(f'Solution Part 1: {res1}')

    res2 = solution2(data)
    print(f'Solution Part 2: {res2}')


