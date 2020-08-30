package main

import "fmt"

//leetcode submit region begin(Prohibit modification and deletion)
/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rangeSumBST(root *TreeNode, L int, R int) int {
	if root == nil {
		return 0
	}
	if root.Val < L {
		return rangeSumBST(root.Right, L, R)
	} else if root.Val > R {
		return rangeSumBST(root.Left, L, R)
	}

	return root.Val +
		rangeSumBST(root.Left, L, R) +
		rangeSumBST(root.Right, L, R)
}

//leetcode submit region end(Prohibit modification and deletion)

// 938

func main() {
	//Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
	//Output: 32
	//
	//Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
	//Output: 23

	root := &TreeNode{10,
		&TreeNode{5,
			&TreeNode{3, nil, nil},
			&TreeNode{7, nil, nil}},
		&TreeNode{15, nil, nil}}
	L := 7
	R := 15

	r := rangeSumBST(root, L, R)
	fmt.Println(r)
}

// $ go run test_leetcode.go
