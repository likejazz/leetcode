# 704-binary-search.py
#
# Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.
class Solution:
    # Solution: Recursive Approach.
    def binary_search(self, keys, l, r, target):
        if r >= l:
            m = int(l + (r - l) / 2)

            if keys[m] == target:
                return m  # We've found the target!
            else:
                if keys[m] > target:
                    return self.binary_search(keys, l, m - 1, target)
                else:
                    return self.binary_search(keys, m + 1, r, target)
        else:
            # If you could't find it.
            return -1

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)
