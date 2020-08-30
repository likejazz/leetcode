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
