from copy import deepcopy


def check_bingo(called, size):
    for row_col in range(size):
        start_row = row_col * size
        end_row = (row_col * size) + size
        for pos in range(start_row, end_row):
            is_called = called[pos]
            if not is_called:
                break
            if pos == end_row - 1:
                return True
        start_col = row_col
        for pos in range(start_col, len(called), size):
            is_called = called[pos]
            if not is_called:
                break
            if pos == len(called) - size + row_col:
                return True
    return False


def update_boards(call, boards, called):
    for i, b in enumerate(boards):
        for j, val in enumerate(b):
            if val == call:
                called[i][j] = True
                break


def calculate_result(winner, called, winning_call):
    sum_of_remains = 0
    for pos, value in enumerate(winner):
        if not called[pos]:
            sum_of_remains += int(value)
    print(winner, sum_of_remains, winning_call)
    return sum_of_remains * int(winning_call)


def solution1(calls, boards, size):
    seen = set()
    called = []
    for b in boards:
        called.append([False] * len(b))
    for call in calls:
        if call in seen:
            continue
        update_boards(call, boards, called)
        for i, c in enumerate(called):
            if check_bingo(c, size):
                return calculate_result(boards[i], c, call)


def solution2(calls, boards, size):
    seen = set()
    called = []
    for b in boards:
        called.append([False] * len(b))
    winners = set()
    last_winning_state = None
    for call in calls:
        if call in seen:
            continue
        update_boards(call, boards, called)
        for i, c in enumerate(called):
            if check_bingo(c, size):
                if i not in winners:
                    winners.add(i)
                    last_winning_state = deepcopy(c)
                    if len(winners) == len(boards):
                        return calculate_result(boards[i], last_winning_state, call)
        seen.add(call)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        calls = f.readline().strip().split(',')
        f.readline()
        boards = []
        current = []
        for line in f:
            line = line.strip()
            if line == '':
                boards.append(current)
                current = []
                continue
            current.extend(line.split())
        boards.append(current)
        size = len(line.split())
    res1 = solution1(calls, boards, size)
    print(f'Solution Part 1: {res1}')

    res2 = solution2(calls, boards, size)
    print(f'Solution Part 2: {res2}')
