# 590. N-ary Tree Postorder Traversal
#
# Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.
class Solution:
    vals: List = []

    def postorder(self, root: 'Node') -> List[int]:
        self.vals = []
        self.dfs(root)

        return self.vals

    def dfs(self, root: 'Node'):
        if root:
            for c in root.children:
                self.dfs(c)
            self.vals.append(root.val)
