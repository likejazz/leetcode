func sortArrayByParity(A []int) []int {
	var ret []int
	for _, a := range A {
		if a % 2 == 0 {
			ret = append([]int{a}, ret...)
		} else {
			ret = append(ret, a)
		}
	}
	return ret
}
