class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    if root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)
    elif root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root

# Test cases
# Example 1
root1 = TreeNode(6)
root1.left = TreeNode(2)
root1.right = TreeNode(8)
root1.left.left = TreeNode(0)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(7)
root1.right.right = TreeNode(9)
root1.left.right.left = TreeNode(3)
root1.left.right.right = TreeNode(5)

p1 = TreeNode(2)
q1 = TreeNode(8)
print(lowestCommonAncestor(root1, p1, q1).val)  # Output: 6

# Example 2
root2 = TreeNode(6)
root2.left = TreeNode(2)
root2.right = TreeNode(8)
root2.left.left = TreeNode(0)
root2.left.right = TreeNode(4)
root2.right.left = TreeNode(7)
root2.right.right = TreeNode(9)
root2.left.right.left = TreeNode(3)
root2.left.right.right = TreeNode(5)

p2 = TreeNode(2)
q2 = TreeNode(4)
print(lowestCommonAncestor(root2, p2, q2).val)  # Output: 2

# Example 3
root3 = TreeNode(2)
root3.left = TreeNode(1)

p3 = TreeNode(2)
q3 = TreeNode(1)
print(lowestCommonAncestor(root3, p3, q3).val)  # Output: 2
