# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
if __name__ == "__main__":
    tn = TreeNode(3)
    tn.left = TreeNode(9)
    tn.right = TreeNode(20)
    tn.right.left = TreeNode(15)
    tn.right.right = TreeNode(7)
    sol = Solution()
    print(sol.maxDepth(tn))