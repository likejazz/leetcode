/* simple-array-sum.cpp
 *
 * Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
 * All rights reserved.
 *
 * This software may be modified and distributed under the terms
 * of the BSD license.  See the LICENSE file for details.
 */
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iterator>

using namespace std;

int main() {
    vector<int> v;
    int sum = 0;

    int n;
    cin >> n;

    copy_n(istream_iterator<int>(cin), n, back_inserter(v));

    for (auto &n : v)
        sum += n;

    cout << sum << endl;

    return 0;
}
