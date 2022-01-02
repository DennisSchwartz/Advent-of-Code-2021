CORRUPT_COST = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

MATCHES = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>',
}

CLOSING_SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def match(closing, opening):
    return MATCHES.get(opening) == closing


def solution1(cmds):
    score = 0
    for cmd in cmds:
        opened_brackets = []
        for char in cmd:
            if char in MATCHES:  # is opening
                opened_brackets.append(char)
            else:  # is closing
                if len(opened_brackets) < 1:
                    score += CORRUPT_COST[char]
                    break
                else:
                    last_opened = opened_brackets.pop()
                    if not match(char, last_opened):
                        score += CORRUPT_COST[char]
                        break

        if len(opened_brackets) == 0:
            pass # ignore incomplete sequences for now

    return score


def solution2(cmds):
    scores = []
    for cmd in cmds:
        opened_brackets = []
        corrupt = False
        for char in cmd:
            if char in MATCHES:  # is opening
                opened_brackets.append(char)
            else:  # is closing
                if len(opened_brackets) < 1:
                    corrupt = True
                    break  # ignore corrupt lines
                else:
                    last_opened = opened_brackets.pop()
                    if not match(char, last_opened):
                        corrupt = True
                        break  # ignore corrupt lines

        if not corrupt and len(opened_brackets) > 0:
            closing_score = 0
            closing_seq = []
            for b in opened_brackets:
                closing_bracket = MATCHES.get(b)
                # The opened_brackets is a stack - the list is backwards which affects the score
                closing_seq.insert(0, closing_bracket)
            for b in closing_seq:
                char_score = CLOSING_SCORES[b]
                closing_score = (5 * closing_score) + char_score
            scores.append(closing_score)

    srt_scores = sorted(scores)

    return srt_scores[len(srt_scores)//2]


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f]

    res1 = solution1(data)
    print(f'Solution Part 1: {res1}')

    res2 = solution2(data)
    print(f'Solution Part 2: {res2}')
