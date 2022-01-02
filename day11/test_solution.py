import unittest

from solution import do_step, get_adjacent_w_diagonal, tick, propagate_flash, reset


class TestAdjacent(unittest.TestCase):
    def test_get_adjacent_w_diagonal(self):
        m = [
            [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
            [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
            [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]
        ]
        res = get_adjacent_w_diagonal(m, row=0, col=0)
        self.assertEqual(sorted([1, 3, 9]), sorted([n[0] for n in res]))

        res = get_adjacent_w_diagonal(m, row=3, col=0)
        self.assertEqual(sorted([7, 8, 8, 9, 9]), sorted([n[0] for n in res]))

        res = get_adjacent_w_diagonal(m, row=3, col=3)
        self.assertEqual(sorted([5, 6, 7, 6, 8, 9, 9, 9]), sorted([n[0] for n in res]))

        res = get_adjacent_w_diagonal(m, row=3, col=9)
        self.assertEqual(sorted([2, 7, 8, 8, 9]), sorted([n[0] for n in res]))

        res = get_adjacent_w_diagonal(m, row=4, col=9)
        self.assertEqual(sorted([7, 8, 9]), sorted([n[0] for n in res]))


class TestTick(unittest.TestCase):
    def test_tick(self):
        initial = [
            [1, 1, 1, 1, 1],
            [1, 9, 9, 9, 1],
            [1, 9, 1, 9, 1],
            [1, 9, 9, 9, 1],
            [1, 1, 1, 1, 1],
        ]
        step1 = [
            [2, 2, 2, 2, 2],
            [2, 10, 10, 10, 2],
            [2, 10, 2, 10, 2],
            [2, 10, 10, 10, 2],
            [2, 2, 2, 2, 2],
        ]
        res = tick(initial)
        self.assertEqual(res, step1)


class TestPropagateFlashes(unittest.TestCase):
    def test_propagate_flashes(self):
        initial = [
            [1, 1, 1, 1, 1],
            [1, 9, 9, 9, 1],
            [1, 9, 1, 9, 1],
            [1, 9, 9, 9, 1],
            [1, 1, 1, 1, 1],
        ]
        step1 = [
            [3, 4, 5, 4, 3],
            [4, 0, 0, 0, 4],
            [5, 0, 0, 0, 5],
            [4, 0, 0, 0, 4],
            [3, 4, 5, 4, 3],
        ]
        res = propagate_flash(initial)
        self.assertEqual(initial, res)
        ticked = tick(initial)
        flashed = propagate_flash(ticked)
        res, _ = reset(flashed)
        self.assertEqual(step1, res)


class TestStep(unittest.TestCase):
    def test_do_step(self):
        initial = [
            [1, 1, 1, 1, 1],
            [1, 9, 9, 9, 1],
            [1, 9, 1, 9, 1],
            [1, 9, 9, 9, 1],
            [1, 1, 1, 1, 1],
        ]
        step1 = [
            [3, 4, 5, 4, 3],
            [4, 0, 0, 0, 4],
            [5, 0, 0, 0, 5],
            [4, 0, 0, 0, 4],
            [3, 4, 5, 4, 3],
        ]
        step2 = [
            [4, 5, 6, 5, 4],
            [5, 1, 1, 1, 5],
            [6, 1, 1, 1, 6],
            [5, 1, 1, 1, 5],
            [4, 5, 6, 5, 4],
        ]
        res, num_flashes = do_step(initial)
        self.assertEqual(res, step1)
        self.assertEqual(num_flashes, 9)

        res, num_flashes = do_step(res)
        self.assertEqual(res, step2)
        self.assertEqual(num_flashes, 0)

    def test_multiple_steps(self):
        initial = [
            [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
            [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
            [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
            [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
            [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
            [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
            [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
            [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
            [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
            [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
        ]
        after1 = [
            [6, 5, 9, 4, 2, 5, 4, 3, 3, 4],
            [3, 8, 5, 6, 9, 6, 5, 8, 2, 2],
            [6, 3, 7, 5, 6, 6, 7, 2, 8, 4],
            [7, 2, 5, 2, 4, 4, 7, 2, 5, 7],
            [7, 4, 6, 8, 4, 9, 6, 5, 8, 9],
            [5, 2, 7, 8, 6, 3, 5, 7, 5, 6],
            [3, 2, 8, 7, 9, 5, 2, 8, 3, 2],
            [7, 9, 9, 3, 9, 9, 2, 2, 4, 5],
            [5, 9, 5, 7, 9, 5, 9, 6, 6, 5],
            [6, 3, 9, 4, 8, 6, 2, 6, 3, 7],
        ]
        after2 = [
            [8, 8, 0, 7, 4, 7, 6, 5, 5, 5],
            [5, 0, 8, 9, 0, 8, 7, 0, 5, 4],
            [8, 5, 9, 7, 8, 8, 9, 6, 0, 8],
            [8, 4, 8, 5, 7, 6, 9, 6, 0, 0],
            [8, 7, 0, 0, 9, 0, 8, 8, 0, 0],
            [6, 6, 0, 0, 0, 8, 8, 9, 8, 9],
            [6, 8, 0, 0, 0, 0, 5, 9, 4, 3],
            [0, 0, 0, 0, 0, 0, 7, 4, 5, 6],
            [9, 0, 0, 0, 0, 0, 0, 8, 7, 6],
            [8, 7, 0, 0, 0, 0, 6, 8, 4, 8],
        ]
        after3 = [
            [0, 0, 5, 0, 9, 0, 0, 8, 6, 6],
            [8, 5, 0, 0, 8, 0, 0, 5, 7, 5],
            [9, 9, 0, 0, 0, 0, 0, 0, 3, 9],
            [9, 7, 0, 0, 0, 0, 0, 0, 4, 1],
            [9, 9, 3, 5, 0, 8, 0, 0, 6, 3],
            [7, 7, 1, 2, 3, 0, 0, 0, 0, 0],
            [7, 9, 1, 1, 2, 5, 0, 0, 0, 9],
            [2, 2, 1, 1, 1, 3, 0, 0, 0, 0],
            [0, 4, 2, 1, 1, 2, 5, 0, 0, 0],
            [0, 0, 2, 1, 1, 1, 9, 0, 0, 0],
        ]
        total = 0
        grid, num_flashes = do_step(initial)
        total += num_flashes
        self.assertEqual(after1, grid)

        grid, num_flashes = do_step(initial)
        total += num_flashes
        self.assertEqual(after2, grid)

        grid, num_flashes = do_step(initial)
        total += num_flashes
        # self.assertEqual(81, total)
        self.assertEqual(after3, grid)


if __name__ == '__main__':
    unittest.main()
