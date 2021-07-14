package com.likejazz.leetcode.solution704

import org.junit.jupiter.api.BeforeEach

import org.junit.jupiter.api.Assertions.*
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
        r = s.search(intArrayOf(-1, 0, 3, 5, 9, 12), 9)
        assertEquals(4, r)
    }

    @Test
    fun t2() {
        r = s.search(intArrayOf(-1, 0, 3, 5, 9, 12), 2)
        assertEquals(-1, r)
    }

    @Test
    fun t3() {
        r = s.search(intArrayOf(2, 5), 5)
        assertEquals(1, r)
    }

    @Test
    fun t4() {
        r = s.search(intArrayOf(-1, 0, 5), -1)
        assertEquals(0, r)
    }
}