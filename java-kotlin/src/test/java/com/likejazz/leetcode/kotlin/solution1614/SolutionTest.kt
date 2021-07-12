package com.likejazz.leetcode.kotlin.solution1614

import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.BeforeEach

internal class SolutionTest {
    private lateinit var s: Solution
    var r: Int = 0

    @BeforeEach
    fun setUp() {
        s = Solution()
    }

    @Test
    fun t1() {
        r = s.maxDepth("(1+(2*3)+((8)/4))+1")
        assertEquals(3, r)
    }
}