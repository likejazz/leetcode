import bisect
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for index, i in enumerate(intervals):
            intervals[index] = [i[0], i[1], index]

        sorted_intervals = sorted(intervals)
        keys = [r[0] for r in sorted_intervals]

        answers = []
        for j in intervals:
            if bisect.bisect_left(keys, j[1]) == len(sorted_intervals):
                answers.append(-1)
            else:
                answers.append(sorted_intervals[bisect.bisect_left(keys, j[1])][2])

        return answers
