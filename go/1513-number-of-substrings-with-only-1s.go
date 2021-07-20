package solution

import (
	"math"
)

func numSub(s string) int {
	var total int = 0
	var contiguous int = 0

	for _, ch := range s {
		if string(ch) == "1" {
			contiguous++
		} else {
			for i := 1; i <= contiguous; i++ {
				total += i
			}
			contiguous = 0
		}
	}
	if contiguous != 0 {
		for i := 1; i <= contiguous; i++ {
			total += i
		}
	}

	return total % int(math.Pow(10, 9)+7)
}
