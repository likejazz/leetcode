package main

import (
	"fmt"
	"strconv"
	_ "strings"
)

//leetcode submit region begin(Prohibit modification and deletion)
func addToArrayForm(A []int, K int) []int {
	vv := ""
	for _, v := range A {
		vv += strconv.Itoa(v)
	}
	vvv, _ := strconv.Atoi(vv)
	vvv += K

	vvvv := strconv.Itoa(vvv)
	fmt.Println(vvvv[2])
	for _, v := range vvvv {
		fmt.Println(v)
	}


	return []int{}
}

//leetcode submit region end(Prohibit modification and deletion)

// 989

func main() {
	r := addToArrayForm([]int{1,2,3,0}, 34)
	fmt.Println(r)
}

// $ go run test_leetcode.go
