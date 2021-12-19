
def solution1(cmds):
    return 0


def solution2(cmds):
    return 0


if __name__ == '__main__':
    with open('day3_input.txt', 'r') as f:
        data = [line.strip() for line in f]

    res1 = solution1(data)
    print(f'Solution Part 1: {res1}')

    res2 = solution2(data)
    print(f'Solution Part 2: {res2}')
