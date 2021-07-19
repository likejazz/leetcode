package com.likejazz.leetcode.solution1903

class Solution {
    private fun isOdd(n: String): Boolean {
        if (n.toInt() % 2 == 1) {
            return true
        }
        return false
    }

    fun largestOddNumber(num: String): String {
        var oddPos: Int = -1
        for (i in num.length - 1 downTo 0) {
            if (isOdd(num.substring(i, i + 1))) {
                oddPos = i
                break
            }
        }
        return if (oddPos == -1) "" else num.substring(0, oddPos + 1)
    }
}