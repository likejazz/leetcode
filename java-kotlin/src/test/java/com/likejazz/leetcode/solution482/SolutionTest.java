package com.likejazz.leetcode.solution482;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    Solution s;
    String r;

    @BeforeEach
    void setUp() {
        s = new Solution();
    }

    @Test
    void t1() {
        r = s.licenseKeyFormatting("5F3Z-2e-9-w", 4);
        assertEquals("5F3Z-2E9W", r);
    }

    @Test
    void t2() {
        r = s.licenseKeyFormatting("2-4A0r7-4k", 4);
        assertEquals("24A0-R74K", r);
    }

    @Test
    void t3() {
        r = s.licenseKeyFormatting("2-5g-3-J", 2);
        assertEquals("2-5G-3J", r);
    }

    @Test
    void t4() {
        r = s.licenseKeyFormatting("2-4A0r7-4k", 3);
        assertEquals("24-A0R-74K", r);
    }

    @Test
    void t5() {
        r = s.licenseKeyFormatting("---", 3);
        assertEquals("", r);
    }
}