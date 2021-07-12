/* 14-longest-common-prefix.java
 *
 * Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
 * All rights reserved.
 *
 * This software may be modified and distributed under the terms
 * of the BSD license.  See the LICENSE file for details.
 */
package com.likejazz.leetcode.java.solution14;

public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0)
            return "";
        String pre = strs[0];
        // Traverse the strings by comparing the prefix.
        for (int i = 1; i < strs.length; i++) {
            while (!strs[i].startsWith(pre))
                pre = pre.substring(0, pre.length() - 1);
        }
        return pre;
    }
}