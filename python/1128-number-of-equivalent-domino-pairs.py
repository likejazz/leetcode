from typing import List, Dict, Tuple
import unittest


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        equalities: int = 0
        fallen_dominoes: Dict[Tuple[int], int] = {}

        for d in dominoes:
            t = tuple(sorted(d))
            if t in fallen_dominoes:
                fallen_dominoes[t] += 1
                equalities += fallen_dominoes[t]
            else:
                fallen_dominoes[t] = 0

        return equalities


class MyTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_t1(self):
        self.assertEqual(self.s.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]), 1)

    def test_t2(self):
        self.assertEqual(3, self.s.numEquivDominoPairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))

    def test_t3(self):
        self.assertEqual(15,
                         self.s.numEquivDominoPairs([[2, 1], [1, 2], [1, 2], [1, 2], [2, 1], [1, 1], [1, 2], [2, 2]]))


if __name__ == '__main__':
    unittest.main()
