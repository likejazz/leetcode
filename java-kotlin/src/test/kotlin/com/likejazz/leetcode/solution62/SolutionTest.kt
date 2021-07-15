package com.likejazz.leetcode.solution62

import org.junit.jupiter.api.BeforeEach

import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

internal class SolutionTest {
    private lateinit var s: Solution

    @BeforeEach
    fun setUp() {
        s = Solution()
    }

    @Test
    fun t1() {
        assertEquals(3, s.uniquePaths(3, 2))
    }

    @Test
    fun t2() {
        assertEquals(28, s.uniquePaths(7, 3))
    }

    @Test
    fun t3() {
        assertEquals(6, s.uniquePaths(3, 3))
    }
}