# 101-symmetric-tree.py
#
# Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.
class Solution:
    def __init__(self):
        # Represents tree as array from linked list.
        self.g = [[]]

    def isSymmetric(self, root: TreeNode) -> bool:
        def make_tree_array(node, level):
            # Create empty array if it doesn't exist.
            if len(self.g) < level + 1:
                self.g.append([])
            if node is None:
                self.g[level].append(None)
                return
            else:
                self.g[level].append(node.val)

            make_tree_array(node.left, level + 1)
            make_tree_array(node.right, level + 1)

        make_tree_array(root, 0)

        # Check whether or not is palindrome except root node.
        for g in self.g[1:]:
            while g:
                if g.pop(0) != g.pop(-1):
                    return False
        return True
