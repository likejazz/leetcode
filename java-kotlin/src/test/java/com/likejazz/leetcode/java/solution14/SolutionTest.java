package com.likejazz.leetcode.java.solution14;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    @Test
    void longestCommonPrefix() {
        Solution s = new Solution();
        String[] a = {"flower", "flow", "flight"};
        String r = s.longestCommonPrefix(a);

        assertEquals("fl", r);
    }
}