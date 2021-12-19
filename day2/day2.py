
def solution1(cmds):
    depth = 0
    pos = 0
    for cmd in cmds:
        direction, val = cmd.split(' ')
        val = int(val)
        if direction == 'forward':
            pos += val
        if direction == 'down':
            depth += val
        if direction == 'up':
            depth -= val

    return depth * pos


def solution2(cmds):
    aim = 0
    depth = 0
    pos = 0
    for cmd in cmds:
        direction, val = cmd.split(' ')
        val = int(val)
        if direction == 'forward':
            pos += val
            depth += aim * val
        if direction == 'down':
            aim += val
        if direction == 'up':
            aim -= val

    return depth * pos


if __name__ == '__main__':
    with open('day2_input.txt', 'r') as f:
        data = [line.strip() for line in f]

    res1 = solution1(data)
    print(f'Solution Part 1: {res1}')

    res2 = solution2(data)
    print(f'Solution Part 2: {res2}')
