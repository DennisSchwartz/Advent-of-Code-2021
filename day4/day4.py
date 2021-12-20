import pandas as pd


def solution1(calls, boards):
    print(calls)
    for call in calls
    for b in boards:
        print(len(b))
    return 0


def solution2(calls, boards):
    return 0


if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        calls = f.readline().strip().split(',')
        f.readline()
        boards = []
        current = []
        for line in f:
            line = line.strip()
            if line == '':
                df = pd.DataFrame(current)
                boards.append(df)
                current = []
                continue
            current.append(line.split())
        boards.append(pd.DataFrame(current))

    res1 = solution1(calls, boards)
    print(f'Solution Part 1: {res1}')

    res2 = solution2(calls, boards)
    print(f'Solution Part 2: {res2}')
