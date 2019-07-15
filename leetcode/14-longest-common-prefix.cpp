/* 14-longest-common-prefix.cpp
 *
 * Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
 * All rights reserved.
 *
 * This software may be modified and distributed under the terms
 * of the BSD license.  See the LICENSE file for details.
 */
class Solution {
public:
    string longestCommonPrefix(vector<string> &strs) {
        if (strs.size() == 0)
            return "";
        std::string pre = strs.front();
        // Traverse the strings by comparing the prefix.
        for (int i = 1; i < strs.size(); i++) {
            while (strs[i].find(pre) != 0)
                pre = pre.substr(0, pre.size() - 1);
        }
        return pre;
    }
};