package main

import "fmt"

//leetcode submit region begin(Prohibit modification and deletion)
func kidsWithCandies(candies []int, extraCandies int) []bool {
	var greatest int
	for _, v := range candies {
		if v > greatest {
			greatest = v
		}
	}

	var ret []bool
	for _, v := range candies {
		if v+extraCandies >= greatest {
			ret = append(ret, true)
		} else {
			ret = append(ret, false)
		}
	}
	return ret
}

//leetcode submit region end(Prohibit modification and deletion)

// 1431

func main() {
	r := kidsWithCandies([]int{2, 3, 5, 1, 3}, 3)
	fmt.Println(r)
}

// $ go run test_leetcode.go
