package main

import (
	"fmt"
	_ "strings"
)

func computeDistance(a, b string) bool {
	var x, y int = -1, -1
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			if x == -1 {
				x = i
			} else {
				y = i
			}
		}
	}

	if x != -1 && y != -1 {
		if a[x] == b[y] && a[y] == b[x] {
			return true
		}
	}
	return false
}

func numSimilarGroups(strs []string) int {
	type result struct {
		str []string
	}
	var results []result

	for _, s := range strs {
		for _, r := range results {
			fmt.Println(s, r.str)
			for _, rs := range r.str {
				if computeDistance(s, rs) {
					fmt.Println("true")
					r.str = append(r.str, s)
					break
				}
			}
		}
		results = append(results, result{str: []string{s}})
	}
	return len(results)
}

// 839

func main() {
	r := numSimilarGroups([]string{"tars", "rats", "arts", "star"})
	fmt.Println(r)
}

// $ go run test_leetcode.go
