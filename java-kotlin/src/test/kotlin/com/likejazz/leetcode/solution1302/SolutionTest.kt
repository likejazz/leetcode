package com.likejazz.leetcode.solution1302

import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.BeforeEach
import org.junit.jupiter.api.Test

internal class SolutionTest {
    private lateinit var s: Solution
    var r: Int = 0

    @BeforeEach
    fun setUp() {
        s = Solution()
    }

    @Test
    fun t1() {
        val data: IntArray = intArrayOf(1, 2, 3, 4, 5, -1, 6, 7, -1, -1, -1, -1, -1, -1, 8)
        var t = createBTree(data, 0)

        r = s.deepestLeavesSum(t)

        assertEquals(15, r)
    }
}