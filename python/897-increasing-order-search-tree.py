# 897. Increasing Order Search Tree
#
# Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.
class Solution:
    vals: List = []

    def increasingBST(self, root: TreeNode) -> TreeNode:
        # Extract the vals out in-order.
        self.vals = []
        self.dfs(root)

        # Build a result tree.
        res = cur = TreeNode(None)
        for v in self.vals:
            cur.right = TreeNode(v)
            cur = cur.right

        return res.right

    def dfs(self, root: TreeNode):
        if root:
            self.dfs(root.left)
            self.vals.append(root.val)
            self.dfs(root.right)