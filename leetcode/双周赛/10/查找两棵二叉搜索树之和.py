from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        arr1 = set(self.inorder(root1))
        arr2 = set(self.inorder(root2))

        for a1 in arr1:
            if target-a1 in arr2:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()

    root1 = TreeNode(1)
    root1.left = TreeNode(0)
    root2 = TreeNode(1)
    root2.right = TreeNode(3)
    print(sol.twoSumBSTs(root1, root2, 3))