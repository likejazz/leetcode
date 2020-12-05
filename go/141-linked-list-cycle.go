func hasCycle(head *ListNode) bool {
	var l []*ListNode

	for head != nil && head.Next != nil {
		for _, n := range l {
			if n == head {
				return true
			}
		}

		l = append(l, head)
		head = head.Next
	}

	return false
}
