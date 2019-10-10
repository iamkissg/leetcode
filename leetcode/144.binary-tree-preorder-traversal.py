from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def preorderTraversal_iteratively(self, root: TreeNode) -> List[int]:
        '''
        20191009
        52 ms	13.7 MB	Python3

        使用 stack 来进行树的 DFS
        前序遍历相对中序遍历更容易些, 不必两次访问非叶节点
        '''
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)

            left = node.left
            right = node.right

            if right:
                stack.append(right)
            if left:
                stack.append(left)
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    
    sol = Solution()
    print(sol.inorderTraversal(root))
    print(sol.inorderTraversal_iteratively(root))