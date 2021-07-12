package com.likejazz.leetcode.kotlin.solution1302

import java.lang.Integer.max

/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

fun createBTree(data: IntArray, index: Int): TreeNode? {
    var pNode: TreeNode? = null
    if (index < data.size) {
        if (data[index] == -1)
            return pNode
        pNode = TreeNode(data[index])
        pNode.left = createBTree(data, 2 * index + 1)
        pNode.right = createBTree(data, 2 * index + 2)
    }
    return pNode
}

// --

class Solution {
    private var sumMap: HashMap<Int, Int> = HashMap()

    private fun dfs(node: TreeNode?, level: Int) {
        if (node == null)
            return

        if (node?.left == null && node?.right == null) {
            var intermediate = sumMap[level]
            if (intermediate == null) intermediate = 0

            sumMap[level] = intermediate + node.`val`
        }

        dfs(node?.left, level + 1)
        dfs(node?.right, level + 1)
    }

    fun deepestLeavesSum(root: TreeNode?): Int {
        dfs(root?.left, 1)
        dfs(root?.right, 1)

        var maxKey = 0
        for (k in sumMap.keys)
            maxKey = max(maxKey, k)

        return sumMap[maxKey]!!
    }
}