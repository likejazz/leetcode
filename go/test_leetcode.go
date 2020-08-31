package main

import (
	"fmt"
)

//leetcode submit region begin(Prohibit modification and deletion)
func firstUniqChar(s string) int {
	var m = make(map[int32]int)
	for _, v := range s {
		m[v]++
	}

	for i, v := range s {
		fmt.Println(v, m[v])
		if m[v] == 1 {
			return i
		}
	}
	return -1
}

//leetcode submit region end(Prohibit modification and deletion)

// 938

func main() {
	//s = "leetcode"
	//return 0.
	//
	//s = "loveleetcode"
	//return 2.

	r := firstUniqChar("loveleetcode")
	fmt.Println(r)
}

// $ go run test_leetcode.go
