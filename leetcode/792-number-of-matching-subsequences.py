# 792-number-of-matching-subsequences.py
#
# Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        matched_count = 0
        
        for word in words:
            pos = 0
            for i in range(len(word)):
                # Find matching position for each character.
                found_pos = S[pos:].find(word[i])
                if found_pos < 0:
                    matched_count -= 1
                    break
                else: # If found, take step position forward.
                    pos += found_pos + 1
            matched_count += 1

        return matched_count

