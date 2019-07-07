# 125-valid-palindrome.py
#
# Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Leave only alphanumeric characters and ignore cases.
        a = []
        for ss in s:
            if ss.isalnum():
                a.append(ss)

        # Check whether or not is palindrome.
        while len(a) > 1:
            if a.pop(0).lower() != a.pop(-1).lower():
                return False
        
        return True
