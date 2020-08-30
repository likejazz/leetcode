from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            # Searches are much more faster than brute-force comparisons.
            if complement in nums[i + 1:]:
                return nums.index(n), nums[i + 1:].index(complement) + (i + 1)


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([1, 5, 2, 9, 4], 13))
