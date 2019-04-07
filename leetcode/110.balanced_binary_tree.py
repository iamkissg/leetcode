# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTreeDepth(self, root):
        if root is None:
            return 0
        else:
            return 1+max(self.getTreeDepth(root.left), self.getTreeDepth(root.right))

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        elif not (root.left or root.right):
            return True
        else:
            # from queue import Queue
            # Q = Queue()
            # Q.put(root)
            # while Q.qsize():
            #     node = Q.get_nowait()
            #     if node:
            #         print(node, node.left, node.right)
            #         Q.put(node.left)
            #         Q.put(node.right)
            #     else:
            #         print('None')
            """子树也要是平衡树"""
            return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.getTreeDepth(root.left)-self.getTreeDepth(root.right)) <= 1


if __name__ == "__main__":
    tn = TreeNode(1)
    tn.left = TreeNode(2)
    tn.right = TreeNode(2)
    tn.left.left = TreeNode(3)
    tn.right.right = TreeNode(3)
    tn.left.left.left = TreeNode(4)
    tn.right.right.right = TreeNode(4)

    sol = Solution()
    print(sol.isBalanced(tn))