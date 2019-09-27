# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return None

        paths = self.DFS(root)
        path_strings = ['->'.join(map(str, p)) for p in paths]
        return path_strings
        
    
    def DFS(self, root):
        # 不能这么算, 会多出路径来的, 指向了空
        # if not root:
        #     return [[]]

        if not root.left and not root.right:
            return [[root.val]]

        paths = []
        if root.left:
            paths.extend([[root.val]+p for p in self.DFS(root.left)])
        if root.right:
            paths.extend([[root.val]+p for p in self.DFS(root.right)])
        return paths