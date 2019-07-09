/* 101-symmetric-tree.cpp
 *
 * Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
 * All rights reserved.
 *
 * This software may be modified and distributed under the terms
 * of the BSD license.  See the LICENSE file for details.
 */
class Solution {
public:
    bool isSymmetric(TreeNode *root) {
        if (!root)
            return true;

        std::stack<TreeNode *> nodes;
        nodes.push(root->left);
        nodes.push(root->right);

        while (!nodes.empty()) {
            TreeNode *right = nodes.top();
            nodes.pop();
            TreeNode *left = nodes.top();
            nodes.pop();

            if (!left && !right) {
                // Child node does not exist.
                continue;
            } else {
                // Child nodes are not symmetrical.
                if (!left || !right || left->val != right->val) {
                    return false;
                }
            }

            nodes.push(left->right);
            nodes.push(right->left);
            nodes.push(left->left);
            nodes.push(right->right);
        }
        return true;
    }
};
