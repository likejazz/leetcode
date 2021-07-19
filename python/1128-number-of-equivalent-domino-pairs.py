from typing import List, Dict, Tuple


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
