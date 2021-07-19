/* 1-two-sum.go
 *
 * Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
 * All rights reserved.
 *
 * This software may be modified and distributed under the terms
 * of the BSD license.  See the LICENSE file for details.
 */
package solution

func twoSum(nums []int, target int) []int {
	numsMap := make(map[int]int)

	for i, num := range nums {
		numsMap[num] = i
	}

	for i, num := range nums {
		// Find the key immediately rather than the whole search.
		if j, ok := numsMap[target-num]; ok && i != j {
			return []int{i, j}
		}
	}
	// Prevent error, it doesn't mean anything.
	return []int{}
}
