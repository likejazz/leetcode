package main

import (
	"container/list"
	"fmt"
	"strings"
)

//leetcode submit region begin(Prohibit modification and deletion)
func removeOuterParentheses(S string) string {
	var stack = list.New()
	var new []string

	for _, ch := range S {

		if stack.Len() == 0 {
			stack.PushBack(ch)
			continue
		} else if string(ch) == "(" {
			stack.PushBack(ch)
		} else if string(ch) == ")" {
			stack.Remove(stack.Back())
			if stack.Len() == 0 {
				continue
			}
		}

		new = append(new, string(ch))
	}
	return strings.Join(new, "")
}
//leetcode submit region end(Prohibit modification and deletion)

func main() {
	r := removeOuterParentheses("(()())()")
	fmt.Println(r)
}

// $ go run test_leetcode.go
