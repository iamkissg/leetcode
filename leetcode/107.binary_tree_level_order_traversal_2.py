# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        from queue import Queue

        if not root:
            return []
        elif root and not root.left and not root.right:
            return [[root.val]]

        
        Q = Queue()
        Q.put(root)
        L = []
        count = 1
        while Q.qsize():
            l = []
            for i in range(min(count, Q.qsize())):
                node = Q.get_nowait()
                if not node:
                    continue
                else:
                    l.append(node.val)
                    Q.put(node.left)
                    Q.put(node.right)
            count *= 2
            L.append(l)
        return L[:-1][::-1]


if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    sol = Solution()
    print(sol.levelOrderBottom(tree))
    
