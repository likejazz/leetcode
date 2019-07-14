# 14-longest-common-prefix.py
#
# Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""
        pre = strs[0]
        # Traverse the strings by comparing the prefix.
        for i in range(1, len(strs)):
            while not (strs[i].startswith(pre)):
                pre = pre[:-1]
        return pre

