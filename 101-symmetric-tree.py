# ==============================================================================
# Copyright 2019 Sang-Kil Park <likejazz@gmail.com> All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
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
