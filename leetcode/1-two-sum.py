# 1-two-sum.py
#
# Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            # Searches are much more faster than brute-force comparisons.
            if complement in nums[i + 1:]:
                return nums.index(n), nums[i + 1:].index(complement) + (i + 1)
