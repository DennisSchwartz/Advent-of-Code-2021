from collections import defaultdict


def tick(t0):
    t1 = t0 - 1
    if t1 < 0:
        return 6, 8
    else:
        return t1, None


def solution1(input, gens):
    population = [p for p in input]
    for _ in range(gens):
        offspring = []
        for i, t in enumerate(population):
            t, o = tick(t)
            population[i] = t
            if o:
                offspring.append(o)
        population += offspring
    return len(population)


def solution2(population, gens):
    counts = {k: 0 for k in range(0, 9)}
    for p in population:
        counts[p] += 1
    for _ in range(gens):
        next_gen = defaultdict(int)
        for k in counts:
            if k == 0:
                next_gen[6] += counts[k]
                next_gen[8] = counts[k]
            else:
                next_gen[k - 1] += counts[k]
        counts = next_gen

    return sum(counts.values())


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        # load as list of ints
        data = list(map(int, f.readline().strip().split(',')))

    res1 = solution1(data, 80)
    print(f'Solution Part 1: {res1}')

    res2 = solution2(data, 256)
    print(f'Solution Part 2: {res2}')
