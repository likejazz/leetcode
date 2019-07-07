/* left-rotation.cpp
 *
 * Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
 * All rights reserved.
 *
 * This software may be modified and distributed under the terms
 * of the BSD license.  See the LICENSE file for details.
 */
#include <map>
#include <queue>
#include <string>
#include <bitset>
#include <fstream>
#include <iostream>

using namespace std;

vector<int> array_left_rotation(vector<int> a, int n, int k) {
    for (int i = 0; i < k; i++) {
        int vv = *(a.begin());
        a.erase(a.begin());
        a.push_back(vv);
    }

    return a;
}

int main() {
    // reads from input
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    for (int a_i = 0; a_i < n; a_i++)
        cin >> a[a_i];

    // rotation
    vector<int> output = array_left_rotation(a, n, k);

    // print the output
    for (auto &n:output)
        cout << n << " ";

    return 0;
}
