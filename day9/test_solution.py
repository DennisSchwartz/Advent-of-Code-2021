import unittest

from solution import get_adjacent_no_diagonal, get_basin


class TestLowPoints(unittest.TestCase):
    def test_get_adjacent_no_diagonal(self):
        m = [
            [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
            [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
            [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]
        ]
        res = get_adjacent_no_diagonal(m, row=0, col=0)
        self.assertEqual(set([n[0] for n in res]), set([1, 3]))

        res = get_adjacent_no_diagonal(m, row=3, col=0)
        self.assertEqual(set([n[0] for n in res]), set([9, 9, 7]))

        res = get_adjacent_no_diagonal(m, row=3, col=3)
        self.assertEqual(set([n[0] for n in res]), set([6, 6, 9, 8]))

        res = get_adjacent_no_diagonal(m, row=3, col=9)
        self.assertEqual(set([n[0] for n in res]), set([2, 8, 8]))


class TestBasins(unittest.TestCase):
    def test_get_basin(self):
        m = [
            [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
            [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
            [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]
        ]

        res = get_basin(m, row=0, col=9)
        self.assertEqual(sorted([4, 3, 2, 1, 0, 4, 2, 1, 2]), sorted([n[0] for n in res]))

        basin = [8, 7, 8, 8, 5, 6, 7, 8, 8, 7, 6, 7, 8, 8]
        res = get_basin(m, row=2, col=2)
        self.assertEqual(sorted(basin), sorted([n[0] for n in res]))


if __name__ == '__main__':
    unittest.main()
