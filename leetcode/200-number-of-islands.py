# 200-number-of-islands.py
#
# Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Depth-first Search until reaching the end.
        def dfs(i, j):
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
                    return
            
            grid[i][j] = 0
            
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        count = 0
        for i in range(len(grid)):        # rows
            for j in range(len(grid[0])): # cols
                if grid[i][j] == '1':
                    # Start dfs when it meet the land.
                    dfs(i, j)
                    count += 1
        return count
