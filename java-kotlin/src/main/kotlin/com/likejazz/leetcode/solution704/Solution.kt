package com.likejazz.leetcode.solution704


class Solution {
    fun search(nums: IntArray, target: Int): Int {
        var left = 0
        var right = nums.size - 1

        var current: Int

        while (left <= right) {
            current = left + (right - left) / 2

            when {
                nums[current] > target -> right = current - 1
                nums[current] < target -> left = current + 1
                nums[current] == target -> return current
            }
        }

        return -1
    }
}
