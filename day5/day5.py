
def solution1(cmds, n, m):
    vent_map = []
    # initialise
    for i in range(n):
        vent_map.append([0] * m)
    for cmd in cmds:
        start, end = cmd
        # ignore diagonals
        if not (start[0] == end[0] or start[1] == end[1]):
            continue
        if start[0] == end[0]:
            r = sorted([start[1], end[1]])
            r[1] += 1
            for i in range(*r):
                vent_map[i][start[0]] += 1
        else:
            r = sorted([start[0], end[0]])
            r[1] += 1
            for i in range(*r):
                vent_map[start[1]][i] += 1

    num_points = 0
    for x in vent_map:
        for y in x:
            if y > 1:
                num_points += 1
    return num_points


def solution2(cmds, n, m):
    vent_map = []
    # initialise
    for i in range(n):
        vent_map.append([0] * m)
    for cmd in cmds:
        start, end = cmd
        # ignore diagonals
        if start[0] == end[0]:
            r = sorted([start[1], end[1]])
            r[1] += 1
            for i in range(*r):
                vent_map[i][start[0]] += 1
        elif start[1] == end[1]:
            r = sorted([start[0], end[0]])
            r[1] += 1
            for i in range(*r):
                vent_map[start[1]][i] += 1
        else:
            stepx = 1
            x = start[0]
            if start[0] > end[0]:
                stepx = -1
            stepy = 1
            y0, y1 = start[1], end[1] + 1
            if start[1] > end[1]:
                stepy = -1
                y0, y1 = start[1], end[1] - 1

            for y in range(y0, y1, stepy):
                vent_map[y][x] += 1
                x += stepx

    num_points = 0
    for x in vent_map:
        for y in x:
            if y > 1:
                num_points += 1
    return num_points


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = []
        n = 0
        m = 0
        for line in f:
            start, end = line.split(' -> ')
            start = list(map(int, start.split(',')))
            n = max(n, start[0])
            m = max(m, start[1])
            end = list(map(int, end.split(',')))
            n = max(n, end[0])
            m = max(m, end[1])
            data.append([start, end])

    res1 = solution1(data, n+1, m+1)
    print(f'Solution Part 1: {res1}')

    res2 = solution2(data, n+1, m+1)
    print(f'Solution Part 2: {res2}')
