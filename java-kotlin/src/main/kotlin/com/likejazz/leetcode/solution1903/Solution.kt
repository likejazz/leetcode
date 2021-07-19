package com.likejazz.leetcode.solution1903

class Solution {
    fun largestOddNumber(num: String): String {
        for (i in num.length - 1 downTo 0) {
            if (num.substring(i, i + 1).toInt() % 2 == 1) {
                return num.substring(0, i + 1)
            }
        }
        return ""
    }
}