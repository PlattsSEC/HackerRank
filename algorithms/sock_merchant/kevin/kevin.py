#!usr/bin/env python3
# Kevin Boyette
import unittest
from collections import Counter


def sockMerchant(_num_socks: int, sock_colors: list[int]) -> int:
    color_counts = Counter(sock_colors)
    return sum((color_counts[color] // 2 for color in color_counts))


class TestHackerRank(unittest.TestCase):
    def test_given_case(self):
        given = [10, 20, 20, 10, 10, 30, 50, 10, 20]
        n = 9

        want = 3
        got = sockMerchant(n, given)
        self.assertEqual(want, got)


if __name__ == "__main__":
    unittest.main()
