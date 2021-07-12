package com.likejazz.leetcode.kotlin.solution1614

import java.lang.Integer.max

class Solution {
    fun maxDepth(s: String): Int {
        var nested = 0
        var nestedMax = 0

        for (element in s) {
            when (element) {
                '(' -> nested++
                ')' -> nested--
            }
            nestedMax = max(nestedMax, nested)
        }

        return nestedMax
    }
}