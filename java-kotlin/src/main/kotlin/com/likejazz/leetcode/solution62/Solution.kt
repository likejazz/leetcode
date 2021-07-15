package com.likejazz.leetcode.solution62

class Solution {
    var m: Int = 0
    var n: Int = 0

    var paths: Int = 0

    fun dfs(r: Int, c: Int) {
        when {
            r == m -> return
            c == n -> return
            c == n - 1 && r == m - 1 -> paths++
        }

        dfs(r + 1, c) // down
        dfs(r, c + 1) // right
    }

    fun uniquePaths(m: Int, n: Int): Int {
        this.m = m
        this.n = n

        dfs(0, 0)

        return paths
    }
}