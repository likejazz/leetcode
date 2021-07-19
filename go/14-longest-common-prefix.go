/* 14-longest-common-prefix.go
 *
 * Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
 * All rights reserved.
 *
 * This software may be modified and distributed under the terms
 * of the BSD license.  See the LICENSE file for details.
 */
package solution

import "strings"

func longestCommonPrefix(strs []string) string {
	if strs == nil || len(strs) == 0 {
		return ""
	}
	var pre = strs[0]
	// Traverse the strings by comparing the prefix.
	for i := 1; i < len(strs); i++ {
		for !strings.HasPrefix(strs[i], pre) {
			pre = pre[:len(pre)-1]
		}
	}
	return pre
}
