/* 994-rotting-oranges.cpp
 *
 * Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
 * All rights reserved.
 *
 * This software may be modified and distributed under the terms
 * of the BSD license.  See the LICENSE file for details.
 */
class Solution {
    int changedCount;
    bool changed;

public:
    void change(int r, int c, vector<vector<int>> &grid) {
        if (grid.at(r).at(c) == 1) {
            // Be careful! The operator `==` is not the same as the operator `=`.
            grid.at(r).at(c) = 2;

            this->changed = true;
        }
    }

    int orangesRotting(vector<vector<int>> &grid) {

        std::vector<vector<int>> snapshot;
        this->changedCount = 0;
        this->changed = false;

        do {
            this->changed = false;
            // Deep copy for the next comparison.
            snapshot = grid;

            int r = 0, c;
            for (vector<int> rows : snapshot) {
                c = 0;
                for (int el : rows) {
                    if (el == 2) {
                        if (r > 0)
                            this->change(r - 1, c, grid);
                        if (c < grid.at(0).size() - 1)
                            this->change(r, c + 1, grid);
                        if (r < grid.size() - 1)
                            this->change(r + 1, c, grid);
                        if (c > 0)
                            this->change(r, c - 1, grid);
                    }
                    c++;
                }
                r++;
            }
            if (this->changed)
                this->changedCount++;
        } while (this->changed);

        // Find an orange that is rotten and returns -1 if found.
        for (auto rows : grid) {
            for (auto el : rows) {
                if (el == 1)
                    return -1;
            }
        }

        return this->changedCount;
    }
};
