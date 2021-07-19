package solution

import (
	"strconv"
)

func largestOddNumber(num string) string {
	for i := len(num) - 1; i >= 0; i-- {
		n, err := strconv.Atoi(num[i : i+1])
		if err == nil && n%2 == 1 {
			return num[:i+1]
		}
	}
	return ""
}
