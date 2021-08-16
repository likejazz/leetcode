import bisect
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sorted_intervals = []
        for index, i in enumerate(intervals):
            bisect.insort(sorted_intervals, [i[0], index])

        keys = [x[0] for x in sorted_intervals]
        answers = []

        for j in intervals:
            bisected_index = bisect.bisect_left(keys, j[1])
            if bisected_index == len(sorted_intervals):
                answers.append(-1)
            else:
                answers.append(sorted_intervals[bisected_index][1])

        return answers
