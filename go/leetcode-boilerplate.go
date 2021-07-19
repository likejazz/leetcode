package solution

type ListNode struct {
	Val  int
	Next *ListNode
}

// TreeNode ...
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func insertLevelOrder(arr []int, root *TreeNode, i int, n int) *TreeNode {
	// Base case for recursion
	if i >= n {
		return root
	}
	// NOTE : for empty nodes leetcode will
	// use 'null' in the test spec [1,2,null,3,4]
	// This implementation substitutes -2147483648 for null
	// so an input slice would be [1,2,-2147483648,3,4] instead
	// terms with -2147483648 will be nil in the
	// constructed tree. since this whole implementation is only used locally
	// it doesn't affect your solution.
	if arr[i] == -2147483648 {
		return nil
	}
	root = newNode(arr[i])
	// insert left child
	root.Left = insertLevelOrder(arr, root.Left, 2*i+1, n)
	// insert right child
	root.Right = insertLevelOrder(arr, root.Right, 2*i+2, n)
	return root
}
func newNode(v int) *TreeNode {
	return &TreeNode{Val: v, Left: nil, Right: nil}
}
func buildLeetCodeTree(a []int) *TreeNode {
	var root *TreeNode
	root = insertLevelOrder(a, root, 0, len(a))
	return root
}

/*
   inserts in LeetCode level order, not sorted order

   input:
     a := []int{1, 2, 3, 4, 5}
   tree structure:

               1
             /    \
            /      \
           2        3
         /  \
        4    5
*/
