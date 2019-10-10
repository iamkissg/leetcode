from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        20191010
        236 ms	88.2 MB	Python3

        递归地处理, 太方便了.
        '''
        if not preorder:
            return []

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:root_index+1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])
        return root


if __name__ == "__main__":
    sol = Solution()
    tree = sol.buildTree(
        preorder = [3,9,20,15,7],
        inorder = [9,3,15,20,7]
    )
    print(tree)