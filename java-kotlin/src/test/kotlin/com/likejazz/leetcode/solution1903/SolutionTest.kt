package com.likejazz.leetcode.solution1903

import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.BeforeEach
import org.junit.jupiter.api.Test

internal class SolutionTest {
    private lateinit var s: Solution

    @BeforeEach
    fun setUp() {
        s = Solution()
    }

    @Test
    fun t1() {
        assertEquals("5", s.largestOddNumber("52"))
        assertEquals("", s.largestOddNumber("4206"))
        assertEquals("35427", s.largestOddNumber("35427"))
        assertEquals("35", s.largestOddNumber("3542"))
    }
}